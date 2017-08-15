#!/bin/bash

submit_files=(*submission.sh)

for i in "${submit_files[@]}"
do
   qsub $i
done