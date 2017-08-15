################################################################################
# Gabe Reder - gkreder@gmail.com
# 08/2017
################################################################################
import sys
import os
import time
import math
from xlrd import open_workbook
start_time = time.time()
################################################################################
# Read Input Arguments
################################################################################
delimiter = ','
tolerance = 0.01
test = False
if len(sys.argv) < 2:
	sys.exit('''\t Error: must specify input file
				USAGE: python fast_transform.py [args] input_file
				args:
					-t: tolerance (in m/z units, default 0.01)
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
# Helper function/variable definitions
################################################################################

# Transformations dictionary for searching reactions
# open transformations worksheet
wb = open_workbook('data/transformations.xlsx')
transformation_sheet = wb.sheet_by_name('Common chemical relationships')
# Save mz vals and reaction names
mz_list = [x.value for x in transformation_sheet.col(7)[2 : ]]
names = [x.value for x in transformation_sheet.col(0)[2 : ]]
# Save transformations - NOTE dict keys are mz values and the values
# are the reaction names
transformations = dict(zip(mz_list, names))
max_diff = max([abs(x) for x in transformations.keys()])


def get_mz(line):
	return line.split('\t')[2]

def get_rt(line):
	return line.split('\t')[3]

def get_method(line):
	return line.split('\t')[1]

def get_metabolite(line):
	return line.split('\t')[0]

def join_lines(closest_match, line_from, line_to):
	delta_mz_obs = float(get_mz(line_to)) - float(get_mz(line_from))
	saved_line = [get_metabolite(line_from) + '--->' + 
								get_metabolite(line_to),
				  transformations[closest_match],
				  str(delta_mz_obs),
				  str(abs(closest_match - delta_mz_obs)),
				  get_metabolite(line_from),
				  get_mz(line_from),
				  get_rt(line_from),
				  get_metabolite(line_to),
				  get_mz(line_to),
				  get_rt(line_to),
				  get_method(line_to)]
	return(delimiter.join(saved_line))
def get_header():
	return delimiter.join(['transformation',
						   'closest_reaction',
						   'delta_mz_observed',
						   'delta_mz_error',
						   'metabolite_from',
						   'mz_from',
						   'rt_from',
						   'metabolite_to',
						   'mz_to',
						   'rt_to',
						   'method'])

def check_time(i, lines):
	index_1 = int(math.ceil((len(lines) / 100)))
	index_10 = int(index_1 * 10)
	index_25 = int(index_1 * 25)
	index_50 = int(index_1 * 50)
	index_75 = int(index_1 * 75)
	index_90 = int(index_1 * 90)

	if i == index_1:
		print('1% Complete --- ' + 
			  str(time.time() - start_time) + ' seconds elapsed')
		sys.stdout.flush()
	if i == index_10:
		print('10% Complete --- ' + 
			  str(time.time() - start_time) + ' seconds elapsed')
		sys.stdout.flush()
	if i == index_25:
		print('25% Complete --- ' + 
			  str(time.time() - start_time) + ' seconds elapsed')
		sys.stdout.flush()
	if i == index_50:
		print('50% Complete --- ' + 
			  str(time.time() - start_time) + ' seconds elapsed')
		sys.stdout.flush()
	if i == index_75:
		print('75% Complete --- ' + 
			  str(time.time() - start_time) + ' seconds elapsed')
		sys.stdout.flush()
	if i == index_90:
		print('90% Complete --- ' + 
			  str(time.time() - start_time) + ' seconds elapsed')
		sys.stdout.flush()
################################################################################


################################################################################
# Main Script
################################################################################

# Open data file and readlines (ignoring NA lines)
with open(in_file, 'r') as f:
	lines = [line.strip() for line in f if 
				get_mz(line).upper() != 'NA' and get_rt(line).upper() != 'NA']

# Throw away header line
lines = lines[1 : ]
# Sort lines by mz value (smallest to largest)
lines = sorted(lines, key = lambda line : float(line.split('\t')[2]))
# Testing subsets of the data for timing
if test:
	lines = lines[0 : 500]
# For saving lines of interest
saved_lines = {}
# For sliding window to not check metabolites that you shouldn't have to
j_start = 0
# For counting number of metabolites per method
method_counts = {}
for i, line_outer in enumerate(lines):
	check_time(i, lines)
	method = get_method(line_outer)
	if method in method_counts:
		method_counts[method] = method_counts[method] + 1
	else:
		method_counts[method] = 1
	# for j, line_inner in enumerate(lines):
	for j in range(j_start, len(lines)):
		j_temp = j_start
		line_inner = lines[j]
		delta_mz = float(get_mz(line_inner)) - float(get_mz(line_outer))
		if abs(delta_mz) > abs(max_diff) + tolerance:
			if j >= i:
				break
			else:
				if j > j_start:
					j_temp = j
				continue
		if method == get_method(line_inner):
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
					saved_lines[method].append(join_lines(closest_match, 
										 				 line_from,
										 				 line_to))
				else:
					saved_lines[method] = [join_lines(closest_match,
													 line_from,
													 line_to)]
	j_start = j_temp
num_found_transformations = 0
for method in saved_lines:
	num_found_transformations += len(saved_lines[method])
	out_file = in_file.split('_')[0].split('.')[0] + '_' + method + '.csv'
	with open(out_file, 'w') as f:
		print(get_header(), file = f)
		for line in saved_lines[method]:
			print(line, file = f)
summary_file = in_file.split('_')[0].split('.')[0] + '_' + \
	str(tolerance).replace('.', '-') + '_summary.txt'
with open(summary_file, 'w') as f:
	print('-----------------------------------------------------------', file=f)
	print('Input file --- ' + in_file, file = f)
	print('System Call --- ' + ' '.join(sys.argv), file = f)
	print('Tolerance (m/z) --- ' + str(tolerance), file = f)
	print('-----------------------------------------------------------', file=f)
	print('*Total*', file = f)
	print('Total Metabolites (no NA) --- ' + str(len(lines)), file = f)
	print('Total found transformations --- ' + \
		str(num_found_transformations), file=f)
	print('', file = f)
	for method in saved_lines:
		print('*' + method + '*', file = f)
		print('Number metabolites (' + method + ') --- ' + \
			str(method_counts[method]), file = f)
		print('Found transformations (' + method + ') --- ' + \
			str(len(saved_lines[method])), file = f)
		print('', file = f)
end_time = time.time()
print('Total time elapsed - ' + str(end_time - start_time))