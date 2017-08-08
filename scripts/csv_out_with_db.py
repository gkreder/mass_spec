import sys
import os
import pandas as pd
import time
start_time = time.time()

TOLERANCE = 1.0
for i, arg in enumerate(sys.argv):
	if arg == '-t':
		if len(sys.argv) > i + 1:
			TOLERANCE = float(sys.argv[i + 1])
		else:
			sys.exit('Error: hanging -t flag in call')

# os.chdir('../data/HirschhornLab_MetabolomicsData/')
# mzrt_files = [x for x in os.listdir() if '.MzRtInfo.txt' in x]
BioAge_file = '/Users/student/mass_spec/data/HirschhornLab_MetabolomicsData/BioAge_spQC_miss0.5.MzRtInfo.txt'
MCDS_file = '/Users/student/mass_spec/data/HirschhornLab_MetabolomicsData/MCDS_spQC_miss0.5.MzRtInfo.txt'
OE_file = '/Users/student/mass_spec/data/HirschhornLab_MetabolomicsData/OE_spQC_miss0.25.MzRtInfo.txt'


# Matrix of chemical transformations
df_trans = pd.read_excel('/Users/student/mass_spec/data/transformations.xlsx', sheetname = 'Common chemical relationships')
df_trans = df_trans.drop(0)
df_trans.set_index('Element', inplace = True)
df_trans.index.name = 'Reaction'
df_trans_mz = df_trans['Δm/z']
df_trans_mz = pd.DataFrame(df_trans_mz)
df_trans_mz.rename(columns = {'Δm/z' : 'delta_mz'}, inplace = True)
df_trans_mz = df_trans_mz.sort_values('delta_mz')
max_diff = max(abs(df_trans_mz['delta_mz'].values))




current_file = BioAge_file
out_file = 'temp_out.csv'

df_current = pd.DataFrame.from_csv(current_file, sep = '\t')
df_current = df_current.sort_values('m.z')
metabolites = df_current.index.values


# First pass - for every metabolite, make a slice matrix consisting of metabolites
# only within mz range as determined by the max possible mz difference dictated by
# the chemical transformation list
print_rows = []
out_cols = ['possible_transformation','transformation_diff_abs','delta_mz','method_1', 'mz_1', 'rt_1', 'method_2', 'mz_2', 'rt_2']
print_rows.append(','.join(out_cols))
# for index, metabolite in enumerate(metabolites):
current_range = range(0, 10)
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
				row = transformation + ',' + str(abs(df_trans_mz.loc[transformation]['delta_mz'] - current_delta_mz)) + ','
				for value in df_slice.loc[mapping].values:
					row += str(value) + ','
				row = row[ : -1]
				print_rows.append(row)




for row in print_rows:
	print(row)

end_time = time.time()
print('time elapsed - ' + str(end_time - start_time))
