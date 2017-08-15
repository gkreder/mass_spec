import sys
import os

top_dir = os.getcwd()
transformation_file = './mass_spec_shared/transformations.xlsx'
data_files = ['./mass_spec_shared/BioAge_spQC_miss0.5.MzRtInfo.txt', './mass_spec_shared/MCDS_spQC_miss0.5.MzRtInfo.txt', './mass_spec_shared/OE_spQC_miss0.25.MzRtInfo.txt']
out_names = ['BioAge_found_transformations.csv', 'MCDS_found_transformations.csv', 'QE_found_transformations.csv']


num_tasks = 7000
tolerance = 0.01
if len([x for x in os.listdir() if '_submission.sh' in x]) > 0:
	os.system('rm *_submission.sh')

for i , data_file in enumerate(data_files):
	out_name = out_names[i]

	submission_fname = out_name.replace('_transformations.csv', str(num_tasks) + '_submission.sh').replace('found', '')
	with open(submission_fname, 'w') as f:
		out_name = out_name.replace('transformations.csv', '$SGE_TASK_ID.csv')
		print('''#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=4G
#$ -o /netapp/home/gkreder/Fischbach/mass_spec/std_out
#$ -e /netapp/home/gkreder/Fischbach/mass_spec/std_err
#$ -l arch=linux-x64
#$ -l netapp=4G,scratch=4G
#$ -l h_rt=00:29:00''', file = f)
		print("#$ -t 1-" + str(num_tasks), file=f)
		print('''
# echo $((SGE_TASK_ID-1))
task_id=$SGE_TASK_ID
source activate fischbach''', file = f)
		s = 'python find_transformation_matches.py --num_tasks '
		s += str(num_tasks) + ' --current_task $((SGE_TASK_ID)) --in_file '
		s += data_file + ' --out_file '
		s += out_name + ' --trans_file ' 
		s += transformation_file
		s += ' --tolerance ' + str(tolerance)
		print(s, file = f)


# os.system('mkdir submission_scripts')
# os.system('mv *_submission.sh submission_scripts/')