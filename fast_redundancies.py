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
					-t: tolerance in RT units (default 0.01)
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





# # Save mz vals and reaction names
# mz_list = [x.value for x in transformation_sheet.col(7)[2 : ]]
# names = [x.value for x in transformation_sheet.col(0)[2 : ]]
# # Save transformations - NOTE dict keys are mz values and the values
# # are the reaction names
# transformations = dict(zip(mz_list, names))
# max_diff = max([abs(x) for x in transformations.keys()])