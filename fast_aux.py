################################################################################
# Gabe Reder - gkreder@gmail.com
# 08/2017
################################################################################
import math
import time
import sys
################################################################################
# Helper function/variable definitions
################################################################################
def get_mz(line):
	return line.split('\t')[2]

def get_rt(line):
	return line.split('\t')[3]

def get_method(line):
	return line.split('\t')[1]

def get_metabolite(line):
	return line.split('\t')[0]

def join_trans_lines(closest_match, line_from, line_to, \
	transformations, delimiter):

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

def get_header(delimiter):
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

def check_time(i, lines, start_time):
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