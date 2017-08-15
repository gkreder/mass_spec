import os
import sys
import time
import pandas as pd

os.chdir('data')

cutoff = 0.01
for i, x in enumerate(sys.argv):
	if i == 1:
		cutoff = float(x)



merged_files = [x for x in os.listdir() if '_merged' in x]


for file in merged_files:
	start_time = time.time()
	print(file + '...')
	out_file = file.replace('_merged', '_filtered')
	out_lines = []
	with open(file, 'r') as f:
		lines = f.readlines()
	sys_call = 'mv ' + file + ' job_files/'
	for i, line in enumerate(lines):
		lines[i] = line.strip()
	for i, line in enumerate(lines):
		if i == 0:
			continue
		transformation_diff = line.split(',')[2]
		if float(transformation_diff) <= cutoff:
			out_lines.append(line)

	out_lines = sorted(out_lines, key = lambda x : float(x.split(',')[2]))
	out_lines.insert(0, lines[0])


	with open(out_file, 'w') as f:
		for line in out_lines:
			print(line, file=f) 
	print('\t\tdone (' + str(time.time() - start_time) + ') seconds')
