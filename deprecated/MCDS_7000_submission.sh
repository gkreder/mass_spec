#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=4G
#$ -o /netapp/home/gkreder/Fischbach/mass_spec/std_out
#$ -e /netapp/home/gkreder/Fischbach/mass_spec/std_err
#$ -l arch=linux-x64
#$ -l netapp=4G,scratch=4G
#$ -l h_rt=00:29:00
#$ -t 1-7000

# echo $((SGE_TASK_ID-1))
task_id=$SGE_TASK_ID
source activate fischbach
python find_transformation_matches.py --num_tasks 7000 --current_task $((SGE_TASK_ID)) --in_file ./mass_spec_shared/MCDS_spQC_miss0.5.MzRtInfo.txt --out_file MCDS_found_$SGE_TASK_ID.csv --trans_file ./mass_spec_shared/transformations.xlsx --tolerance 0.01
