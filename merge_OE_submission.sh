#!/bin/bash

#$ -S /bin/bash
#$ -cwd
#$ -r y
#$ -j y
#$ -l mem_free=8G
#$ -o /netapp/home/gkreder/Fischbach/mass_spec/std_out
#$ -e /netapp/home/gkreder/Fischbach/mass_spec/std_err
#$ -l arch=linux-x64
#$ -l netapp=16G,scratch=16G
#$ -l h_rt=48:00:00

source activate fischbach
python fast_merge.py -n OE data/input/
