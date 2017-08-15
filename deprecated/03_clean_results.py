import sys
import os
import time

datasets = []
files = []
os.chdir('./data/')

for x in os.listdir():
	if '_found' in x:
		files.append(x)
		dataset = x.split('_')[0]
		if dataset not in datasets:
			datasets.append(x.split('_')[0])
if 'job_files' in os.listdir():
	os.system('rm -r job_files')
	os.system('mkdir job_files')


for dataset in datasets:
	start_time = time.time()
	print(dataset + '...')
	dataset_files = [x for x in files if x.split('_')[0] == dataset]
	print_lines = []
	# Grab header line
	first_file = dataset_files[0]
	with open(first_file, 'r') as f:
		header = f.readline().strip()
	for x in dataset_files:
		with open(x, 'r') as f:
			lines = f.readlines()
		for i, line in enumerate(lines):
			lines[i] = line.strip()
		lines = lines[1 : ]
		for line in lines:
			print_lines.append(line)
		sys_call = 'mv ' + x + ' job_files/'
		os.system(sys_call)

	method_names = []
	method_data = {}

	for line in print_lines:
		method = line.split(',')[4]
		if method not in method_names:
			method_names.append(method)
			method_data[method] = [line]
		else:
			method_data[method].append(line)

	for method in method_names:
		out_file = dataset + '_' + method + '_merged.csv'
		with open(out_file, 'w') as f:
			print(header, file=f)
			for line in method_data[method]:
				print(line, file=f)


	end_time = time.time()
	print('\t\tdone (' + str(end_time - start_time) + ') seconds')


