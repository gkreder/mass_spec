import sys
import os
import pandas as pd
import time
import math
start_time = time.time()

if len(sys.argv) <= 1:
	sys.exit('''
		REQUIRED ARGUMENTS:
			--in_file (-i):
				path to input file
			--trans_file (-t):
				path to chemical transformations file
		OPTIONAL ARGUMENTS:
			--current_task + --num_tasks:
				Must be used together, task_number (integer) for cluster parallel jobs (e.g. via SGE_TASK_ID variable) 
				and total numbero of tasks. If not passed, will default to running single job on the whole file 
				(this takes a very long time, maybe close to 48 hours and may exceed cluster/computer memory allocations).
				NOTE: task numbers start at 1
			--tolerance:
				tolerance (in m/z units, float) for difference between chemical transformation
				delta_m/z and observed delta_m/z. Defaults to 0.01
			--out_file (-o):
				output file name, defaults to transformation_matches.csv

		EXAMPLE CALL:
			python find_transformation_matches.py --in_file /path/to/input.txt --trans_file /path/to/transformations.xlsx --task 2 --tolerance 0.01
		''')

TOLERANCE = 0.01
found_input_file = False
found_trans_file = False
tasks = False
out_file = 'transformation_matches.csv'
for i, arg in enumerate(sys.argv):
	if arg == '--tolerance':
		if len(sys.argv) > i + 1:
			TOLERANCE = float(sys.argv[i + 1])
		else:
			sys.exit('Error: hanging --tolerance flag in call')
	if arg == '--current_task':
		if len(sys.argv) > i + 1:
			tasks = True
			task_num = int(sys.argv[i + 1])
		else:
			sys.exit('Error: hanging --current_task flag in call')
	if arg == '--num_tasks':
		if len(sys.argv) > i + 1:
			tasks = True
			num_tasks = int(sys.argv[i + 1])
		else:
			sys.exit('Error: hanging --num_tasks flag in call')
	if arg == '--in_file' or arg == '-i':
		if len(sys.argv) > i + 1:
			found_input_file = True
			input_file = sys.argv[i + 1]
		else:
			sys.exit('Error: hanging --in_file (-i) flag in call')
	if arg == '--trans_file' or arg == '-t':
		if len(sys.argv) > i + 1:
			found_trans_file = True
			trans_file = sys.argv[i + 1]
		else:
			sys.exit('Error: hanging --trans_file (-t) flag in call')
	if arg == '--out_file' or arg == '-o':
		if len(sys.argv) > i + 1:
			out_file = sys.argv[i + 1]
		else:
			sys.exit('Error: hanging --out_file (-o) flag in call')

if not found_input_file:
	sys.exit('Error: Must specify an input file using --in_file or -f flag')
if not found_trans_file:
	sys.exit('Error: Must specify a chemical transformations file using --trans_file or -t flag')
if not tasks:
	print('Warning: Running without task parallelization - this may take more than 48 hours. Recommend using --current_task/--num_tasks flag')
elif tasks:
	if not ('--num_tasks' in sys.argv and '--current_task' in sys.argv):
		sys.exit('Error: If using tasks, must specify both --num_tasks and --current_task')
	if task_num > num_tasks:
		sys.exit('Error: Current task number cannot be greater than total number of tasks')
	if task_num <= 0:
		sys.exit('Error: Task numbers must be greater than or equal to 1')


current_file = input_file

# Matrix of chemical transformations
df_trans = pd.read_excel(trans_file, sheetname = 'Common chemical relationships')
# df_trans = pd.read_excel('/Users/student/mass_spec/data/transformations.xlsx', sheetname = 'Common chemical relationships')
df_trans = df_trans.drop(0)
df_trans.set_index('Element', inplace = True)
df_trans.index.name = 'Reaction'
df_trans_mz = df_trans['Δm/z']
df_trans_mz = pd.DataFrame(df_trans_mz)
df_trans_mz.rename(columns = {'Δm/z' : 'delta_mz'}, inplace = True)
df_trans_mz = df_trans_mz.sort_values('delta_mz')
max_diff = max(abs(df_trans_mz['delta_mz'].values))

df_current = pd.DataFrame.from_csv(current_file, sep = '\t')
df_current = df_current.sort_values('m.z')
metabolites = df_current.index.values


# First pass - for every metabolite, make a slice matrix consisting of metabolites
# only within mz range as determined by the max possible mz difference dictated by
# the chemical transformation list
print_rows = []
out_cols = ['metabolites','possible_transformation','transformation_diff_abs','delta_mz','method_1', 'mz_1', 'rt_1', 'method_2', 'mz_2', 'rt_2']
print_rows.append(','.join(out_cols))

if not tasks:
	current_range = range(0, len(metabolites))
else:
	increment = math.ceil(len(metabolites) / num_tasks)
	start_range = (task_num - 1) * increment
	end_range = task_num * increment
	end_range = min(end_range, len(metabolites))
	current_range = range(start_range, end_range)

for index in current_range:
	metabolite = metabolites[index]
	current_mz = df_current['m.z'][metabolite]
	current_rt = df_current['RT'][metabolite]
	current_method = df_current['Method'][metabolite]
	start_index = index
	while(start_index > 0 and abs(current_mz - df_current['m.z'].iloc[[start_index]].values[0]) <= max_diff + TOLERANCE):
		start_index -= 1

	end_index = index
	while(end_index < len(metabolites) and abs(df_current['m.z'].iloc[[end_index]].values[0] - current_mz) <= max_diff + TOLERANCE):
		end_index += 1

	# print(str(index + 1) + ' of ' +  str(len(metabolites)) + ' (' + str(current_mz) + ') ' + ' ------ ' + str(start_index))
	# print('\t\t' + str(current_mz - df_current['m.z'].iloc[[start_index]].values[0]))
	# print('\t\t' + str(df_current['m.z'].iloc[[end_index]].values[0] - current_mz))

	# Take slice of original dataframe within mz range of interest
	df_slice = df_current.iloc[start_index : end_index]
	# Take difference between current metabolite mz and slice
	df_subtract = pd.DataFrame(current_mz - df_slice['m.z'])
	df_subtract.columns = ['delta_mz']
	# Concat back with slice to save slice metabolite info
	df_slice = pd.concat([df_slice, df_subtract], axis = 1)
	# Rename slice metabolite info columns
	df_slice = df_slice.rename(columns = {'Method' : 'method_2', 'm.z' : 'mz_2', 'RT' : 'rt_2'})
	# Insert original metabolite info columns
	df_slice['mz_1'] = current_mz
	df_slice['method_1'] = current_method
	df_slice['rt_1'] = current_rt
	# Reorder columns
	cols = ['delta_mz', 'method_1', 'mz_1', 'rt_1', 'method_2', 'mz_2', 'rt_2']
	df_slice = df_slice[cols]

	# Rename index to refer to both metabolites
	new_index = []
	for i, s in enumerate(df_slice.index):
		new_index.append(metabolite + '-----' + s)
	new_index = pd.Index(new_index)
	df_slice.index = new_index


	# Second pass - keep only slice metabolites whose delta_mz
	# values are close enough to one of the chemical transformations
	# save to print_rows
	for mapping in df_slice.index:
		current_delta_mz = df_slice.loc[mapping]['delta_mz']
		for transformation in df_trans_mz.index:
			if (abs(df_trans_mz.loc[transformation]['delta_mz'] - current_delta_mz)) <= TOLERANCE:
				if (df_slice.loc[mapping]['method_1'] == df_slice.loc[mapping]['method_2']):
					row = mapping + ',' + transformation + ',' + str(abs(df_trans_mz.loc[transformation]['delta_mz'] - current_delta_mz)) + ','
					for value in df_slice.loc[mapping].values:
						row += str(value) + ','
					row = row[ : -1]
					print_rows.append(row)


with open(out_file, 'w') as f:
	for row in print_rows:
		print(row, file = f)
sys_call = 'mv ' + out_file + ' data/'
os.system(sys_call)

end_time = time.time()
print('time elapsed - ' + str(end_time - start_time))
