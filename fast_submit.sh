#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=8G
#$ -o /netapp/home/gkreder/Fischbach/mass_spec/std_out
#$ -e /netapp/home/gkreder/Fischbach/mass_spec/std_err
#$ -l arch=linux-x64
#$ -l netapp=8G,scratch=8G
#$ -l h_rt=48:00:00
#$ -t 1-3

# echo $((SGE_TASK_ID-1))
task_id=$SGE_TASK_ID
mzrt_files=(data/*_MzRtInfo.txt)

source activate fischbach
python fast_transform.py  "${mzrt_files[task_id-1]}"



