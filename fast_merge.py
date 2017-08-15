################################################################################
# Gabe Reder - gkreder@gmail.com
# 08/2017
################################################################################
import sys
import os

################################################################################
# Read Input Arguments
################################################################################
top_dir = os.getcwd() + '/'
if len(sys.argv) < 2:
	sys.exit('''\t Error: must specify input directory

				USAGE: python fast_merge.py directory_name''')
in_folder = top_dir + sys.argv[-1]
################################################################################

################################################################################
os.chdir(in_folder)
in_files = [x for x in os.listdir() if x[0] != '.' and '.csv' in x \
	and 'merged' not in x]
cohort_data = {}

# Grab all cohort names and save header
for f in in_files:
	if f.split('_')[0] not in cohort_data:
		cohort_data[f.split('_')[0]] = []
with open(f, 'r') as f:
	header = f.readline().strip()

for i, cohort in enumerate(cohort_data):
	print(cohort + ' (' + str(i + 1) + ' of ' + str(len(cohort_data)) +')')
	cohort_data[cohort].append(header)
	cohort_files = [x for x in in_files if cohort in x]
	for file in cohort_files:
		with open(file, 'r') as f:
			lines = [x.strip() for x in f.readlines()[1 : ]]
		for line in lines:
			cohort_data[cohort].append(line)
	out_file = cohort + '_merged.csv'
	with open(out_file, 'w') as f:
		for line in cohort_data[cohort]:
			print(line, file = f)
	print('...done')