#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=32G
#$ -o /netapp/home/gkreder/Fischbach/mass_spec/std_out
#$ -e /netapp/home/gkreder/Fischbach/mass_spec/std_err
#$ -l arch=linux-x64
#$ -l netapp=32G,scratch=32G
#$ -l h_rt=48:00:00
#$ -t 1-3


# echo $((SGE_TASK_ID-1))
source activate fischbach
python map_transformations.py -task $((SGE_TASK_ID-1))
