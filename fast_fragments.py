################################################################################
# Gabe Reder - gkreder@gmail.com
# 08/2017
################################################################################
import sys
import os
import time
import math
from xlrd import open_workbook
from fast_aux import *
start_time = time.time()
################################################################################
# Read Input Arguments
################################################################################
delimiter = ','
tolerance = 0.1
test = False
if len(sys.argv) < 2:
	sys.exit('''\t Error: must specify input file
				USAGE: python fast_fragments.py [args] input_file
				args:
					-t: tolerance in RT units (default 0.1)
					-d: delimiter for output files (default ',' )''')
for i, arg in enumerate(sys.argv[1 : -1]):
	if arg[0] == '-':
		if sys.argv[i + 2][0] == '-' or i == len(sys.argv[1 : -1]) - 1:
			if arg[0 : 2] != '--':
				sys.exit('Error: Hanging argument flag')
	if arg == '-t':
		tolerance = float(sys.argv[i + 2])
	if arg == '-d':
		delimiter = sys.argv[i + 2]
	if arg == '--test':
		test = True

if sys.argv[-2][0] == '-' and sys.argv[-2][0 : 2] != '--':
	sys.exit('''Error: must specify input file''')
in_file = sys.argv[-1]
################################################################################
# Main Script
################################################################################
# Transformations dictionary for searching reactions
# open transformations worksheet
wb = open_workbook('data/transformations.xlsx')
transformation_sheet = wb.sheet_by_name('Common adducts')
# Save mz vals and adduct names (removing blank rows)
mz_list = [x.value for x in transformation_sheet.col(1)[1 : ] if x.value != '']
names = [x.value for x in transformation_sheet.col(0)[1 : ] if x.value != '']
if len(mz_list) != len(names):
	sys.exit('Error: Column length mismatch in transformation excel input...'\
	+ 'does every adduct have both a name and mz value?')
# Save transformations (adducts) - NOTE dict keys are mz values and the values
# are the reaction names
transformations = dict(zip(mz_list, names))
max_diff = max([abs(x) for x in transformations.keys()])

# Open data file and readlines (ignoring NA lines)
with open(in_file, 'r') as f:
	lines = [line.strip() for line in f if 
				get_mz(line).upper() != 'NA' and get_rt(line).upper() != 'NA']
# Throw away header line
lines = lines[1 : ]
# Sort lines by rt value (smallest to largest)
lines = sorted(lines, key = lambda line : float(line.split('\t')[3]))
# Testing subsets of the data for timing
if test:
	lines = lines[0 : 500]
saved_lines = {}
# For sliding window to not check metabolites that you shouldn't have to
j_start = 0
# For counting number of metabolites per method
method_counts = {}
for i, line_outer in enumerate(lines):
	check_time(i, lines, start_time)
	method = get_method(line_outer)
	if method in method_counts:
		method_counts[method] = method_counts[method] + 1
	else:
		method_counts[method] = 1
	# for j, line_inner in enumerate(lines):
	j_temp = j_start
	for j in range(j_start, len(lines)):
		line_inner = lines[j]
		delta_rt = float(get_rt(line_inner)) - float(get_rt(line_outer))
		if abs(delta_rt) > abs(max_diff) + tolerance:
			if j >= i:
				break
			else:
				if j > j_start:
					j_temp = j
				continue
		if method == get_method(line_inner):
			delta_mz = float(get_mz(line_inner)) - float(get_mz(line_outer))
			closest_match = min(mz_list, key = \
										 lambda x : min(
										 	abs(x - delta_mz),
										 	abs(x + delta_mz))
										 )
			dist_current = abs(closest_match - delta_mz)
			dist_reverse = abs(closest_match + delta_mz)
			if min(dist_current, dist_reverse) <= tolerance:
				line_to = line_inner
				line_from = line_outer
				if dist_reverse < dist_current:
					line_to = line_outer
					line_from = line_inner
				if method in saved_lines:
					saved_lines[method].append(join_trans_lines(closest_match, 
										 				 line_from,
										 				 line_to,
										 				 transformations,
										 				 delimiter))
				else:
					saved_lines[method] = [join_trans_lines(closest_match,
													 line_from,
													 line_to,
													 transformations,
													 delimiter)]
	j_start = j_temp
num_found_transformations = 0
for method in saved_lines:
	num_found_transformations += len(saved_lines[method])
	out_file = in_file.split('_')[0].split('.')[0] + '_' + method+'_adducts.csv'
	with open(out_file, 'w') as f:
		print(get_header(delimiter), file = f)
		for line in saved_lines[method]:
			print(line, file = f)
summary_file = in_file.split('_')[0].split('.')[0] + '_' + \
	str(tolerance).replace('.', '-') + '_adduct_summary.txt'
with open(summary_file, 'w') as f:
	print('-----------------------------------------------------------', file=f)
	print('Input file --- ' + in_file, file = f)
	print('System Call --- ' + ' '.join(sys.argv), file = f)
	print('Tolerance (rt) --- ' + str(tolerance), file = f)
	print('-----------------------------------------------------------', file=f)
	print('*Total*', file = f)
	print('Total Metabolites (no NA) --- ' + str(len(lines)), file = f)
	print('Total found adducts --- ' + \
		str(num_found_transformations), file=f)
	print('', file = f)
	for method in saved_lines:
		print('*' + method + '*', file = f)
		print('Number metabolites (' + method + ') --- ' + \
			str(method_counts[method]), file = f)
		print('Found adducts (' + method + ') --- ' + \
			str(len(saved_lines[method])), file = f)
		print('', file = f)
end_time = time.time()
print('Total time elapsed - ' + str(end_time - start_time))