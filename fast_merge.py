################################################################################
# Gabe Reder - gkreder@gmail.com
# 08/2017
################################################################################
import sys
import os
import time
from fast_aux import *
start_time = time.time()
################################################################################
# Read Input Arguments and setup folder tree
################################################################################
adduct_tolerance = 0.1
top_dir = os.getcwd() + '/'
test = False
if len(sys.argv) < 2:
	sys.exit('''\t Error: must specify input directory

				USAGE: python [-d adduct_tolerance] ''' + \
				'fast_merge.py directory_name')
for i, arg in enumerate(sys.argv[1 : -1]):
	if arg[0] == '-':
		if sys.argv[i + 2][0] == '-' or i == len(sys.argv[1 : -1]) - 1:
			if arg[0 : 2] != '--':
				sys.exit('Error: Hanging argument flag')
	if arg == '-d':
		adduct_tolerance = float(sys.argv[i + 2])
	if arg == '--test':
		test = True

if sys.argv[-2][0] == '-' and sys.argv[-2][0 : 2] != '--':
	sys.exit('''Error: must specify input file''')

in_folder = top_dir + sys.argv[-1]
out_folder = in_folder + '/../output/'
if 'output' not in os.listdir(in_folder + '/../'):
	os.system('mkdir ' + out_folder)
################################################################################
# Initialize file lists and header
################################################################################
os.chdir(in_folder)
trans_files = [x for x in os.listdir() if x[0] != '.' \
	and '_transformations.csv' in x \
	and 'merged' not in x]
adduct_files = [x for x in os.listdir() if x[0] != '.' \
	and '_adducts.csv' in x \
	and 'merged' not in x]
cohorts = {}

# check to make sure every transformation file has a coresponding
# adduct file
adduct_check = [x.split('_adducts.csv')[0] for x in adduct_files]
for i, x in enumerate(trans_files):
	name = x.split('_transformations.csv')[0]
	if name not in adduct_check:
		sys.exit('Error: Couldn\'t find corresponding adduct file for \
			transformation file ' + name)
if len(adduct_files) != len(trans_files):
	sys.exit('Error: Each transformation file must have an adduct file and \
		vice versa')
# Save cohort names and header line
for f in trans_files:
	if f.split('_')[0] not in cohorts:
		cohorts[f.split('_')[0]] = []
with open(f, 'r') as f:
	header = f.readline().strip()
################################################################################
# Helper functions for reading/storing redundant adducts
################################################################################
# Get redundant adducts according to adducts dict
def get_redun_adducts(metab, adducts):
	redun = []
	if metab in adducts:
		redun = adducts[metab]
	return redun

# Given trans_from metabolite and trans_to metabolite, and dictionary of found
# transformations, and adducts dictionary - checks if the proposed reaction
# trans_from ---> trans_to is redundant (according to adducts dict)
def is_redun(trans_from, trans_to, adducts, found_trans):
	found = False
	redun_from_list = get_redun_adducts(trans_from, adducts)
	redun_to_list = get_redun_adducts(trans_to, adducts)
	redun_from_list.append(trans_from)
	redun_to_list.append(trans_to)
	for x_from in redun_from_list:
		if x_from in found_trans:
			for x_to in redun_to_list:
				if x_to in found_trans[x_from]:
					found = True
	return found
# Record the new transformation trans_from--->trans_to and all redundant ones 
# too according to adducts
def update_transformations(trans_from, trans_to, adducts, found_trans):
	redun_from_list = get_redun_adducts(trans_from, adducts)
	redun_to_list = get_redun_adducts(trans_to, adducts)
	redun_from_list.append(trans_from)
	redun_to_list.append(trans_to)
	for x_from in redun_from_list:
		for x_to in redun_to_list:
			if x_from in found_trans:
				found_trans[x_from].append(x_to)
			else:
				found_trans[x_from] = [x_to]
	return found_trans
################################################################################
# Main filtering and storing script
################################################################################
# Filter each transformation file using corresponding adduct file and keep
# non-redundant transformations
cohort_summaries = {}
for cohort_i, cohort in enumerate(cohorts):
	cohort_summaries[cohort] = []
	file_summaries = []
	print(cohort + ' (' + str(cohort_i + 1) + ' of ' + str(len(cohorts)) +')')
	cohorts[cohort].append(header)
	# sort to make sure the indices are common between the two
	cohort_trans = sorted([x for x in trans_files if cohort in x])
	cohort_adducts = sorted([x for x in adduct_files if cohort in x])
	for file_index, file in enumerate(cohort_trans):
		summary_name = file.split('_transformations.csv')[0]
		print('\t***' + summary_name + '***')
		num_redun = 0
		num_recorded = 0
		adducts = {}
		found_trans = {}
		# Save adducts for given cohort-method adduct file
		with open(cohort_adducts[file_index], 'r') as f:
			print('\tSaving Adducts...')
			loop_lines = f.readlines()[1 : ]
			if test:
				loop_lines = loop_lines[ : 100]
			for x in loop_lines:
				# Only keep adduct lines within tolerance
				if get_adduct_err(x) <= adduct_tolerance:
					if get_adduct_from(x) in adducts:
						adducts[get_adduct_from(x)].append(get_adduct_to(x))
					else:
						adducts[get_adduct_from(x)] = [get_adduct_to(x)]
		print('\t...done')
		trans_lines = []
		# Save list of non-redundant found transformations in cohort-method
		# transformation file
		with open(file, 'r') as f:
			print('\tFiltering candidate transformations...')
			loop_lines = f.readlines()[1 : ]
			if test:
				loop_lines = loop_lines[ : 100]
			for trans_index, x in enumerate(loop_lines):
				check_time(trans_index, loop_lines, start_time, tabs = 1)
				trans_from = get_trans_from(x)
				trans_to = get_trans_to(x)
				# check if redundant transformation
				if is_redun(trans_from, trans_to, adducts, found_trans):
					num_redun += 1
					continue
				# If gets to here, then non-redundant
				trans_lines.append(x.strip())
				num_recorded += 1
				# Add transformation and redunant transformations to found_trans
				found_trans = update_transformations(trans_from, trans_to, \
					adducts, found_trans)
		for line in trans_lines:
			cohorts[cohort].append(line)
		# save file summary
		summary_files = file + ', ' + cohort_adducts[file_index]
		cohort_summaries[cohort].append((summary_name, summary_files, \
			num_recorded, num_redun))
	# write outfile (merged.csv file) for each cohort
	out_file = cohort + '_merged.csv'
	with open(out_file, 'w') as f:
		for line in cohorts[cohort]:
			print(line, file = f)
	print('...done --- ' + str(time.time() - start_time) + ' seconds elapsed')
################################################################################
# Print summary files
################################################################################
print('Writing summary files')
for cohort in cohorts:
	summary_file = cohort + '_' + '_merged_summary.txt'
	with open(summary_file, 'w') as f:
		print('-------------------------------------------------------', file=f)
		print('Input directory --- ' + in_folder, file = f)
		print('System call --- ' + ' '.join(sys.argv), file = f)
		print('Adduct tolerance --- ' + str(adduct_tolerance), file = f)
		print('-------------------------------------------------------', file=f)
		for (summary_name, summary_files, num_recorded, num_redun) \
			in cohort_summaries[cohort]:
			print('', file = f)
			print('*' + summary_name +'*', file = f)
			print('Files --- ' + summary_files, file = f)
			print('Transformations kept --- ' + str(num_recorded), file = f)
			print('Transformations discarded --- ' + str(num_redun), file = f)
			print('', file= f)
print('...done --- ' + str(time.time() - start_time) + ' seconds elapsed')
################################################################################
# Move output files to output directory
################################################################################
# for x in os.listdir():
# 	if '.csv' in x or 'summary' in x:
# 		sys_call = 'mv ' + x + ' ' + out_folder
# 		os.system(sys_call)