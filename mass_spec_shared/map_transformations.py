###########################################
# Gabe Reder - 7/2017 - gkreder@gmail.com #
###########################################
import os
import sys
import numpy as np
import pandas as pd
import datetime
top_dir = os.getcwd()
# top_dir = '~/Fischbach/mass_spec/mass_spec_shared/'
# os.chdir(top_dir)


TOLERANCE = 1.0
if '-t' in sys.argv:
	if sys.argv.index("-t") == len(sys.argv) - 1:
		sys.exit("Error: -t flag passed without argument")
	else:
		TOLERANCE = float(sys.argv[sys.argv.index("-t") + 1])

tasks = False
if '--task' in sys.argv:
	if sys.argv.index("--task") == len(sys.argv) - 1:
		sys.exit("Error: --task flag passed without argument")
	else:
		tasks = True
		task_num = int(sys.argv[sys.argv.index("--task") + 1])

test_run = False
if '--test' in sys.argv:
	test_run = True

def write_cyto_csv(df_data, fname_out):
	print("")
	print("Starting " + fname_out + " at " + str(datetime.datetime.now()))
	df_diffs = pd.DataFrame()
	df_diffs_temp = pd.DataFrame()
	df_diffs = pd.DataFrame(df_data['m.z'].copy())
	df_diffs_temp = df_diffs.copy()
	
	if test_run:
		loop_range = range(0, 30)
	else:
		loop_range = range(df_diffs.shape[0])
	# for i in range(df_diffs.shape[0]):
	# for i in range(0, 5):
	for i in loop_range:
	    kwargs = {df_data['m.z'].index[i] : lambda df : df['m.z']}
	    kwargs_temp = {df_data['m.z'].index[i] : lambda df : np.repeat(df['m.z'][i], df['m.z'].shape[0])}
	    df_diffs = df_diffs.assign(**kwargs)
	    df_diffs_temp = df_diffs_temp.assign(**kwargs_temp)
	    
	df_diffs = df_diffs.subtract(df_diffs_temp)
	df_diffs = df_diffs.drop('m.z', axis = 1)
	df_list = []
	for i in range(len(df_diffs.columns)):
	    diff_col = df_diffs[df_diffs.index[i]]
	    index = pd.Index([x + ' - ' + df_diffs.index[i] for x in diff_col.index], name = 'Transformation')
	    columns = df_trans_mz.index
	    df_mask = pd.DataFrame(np.isclose(diff_col.values[ : , None], df_trans_mz.values.transpose(), atol=TOLERANCE), 
	                           index = index, columns = columns)
	    df_list.append(df_mask)

	df_mask = pd.concat(df_list)
	    
	    # https://stackoverflow.com/questions/39602004/can-i-use-pandas-dataframe-isin-with-a-numeric-tolerance-parameter
	    # pd.DataFrame(np.isclose(df_diffs['1'].values[:, None], df_trans_test.values.transpose(), atol=1.0))
	df_sum = df_mask.sum(axis = 1)
	df_found = pd.DataFrame(df_sum[df_sum > 0], columns = ['Number Hits'])
	df_found = df_found[df_found.index.map(lambda x : x.split('-')[0].replace(' ', '') != x.split('-')[1].replace(' ', ''))]
	df_weights = pd.DataFrame(float('nan'), index = df_diffs.index, columns = df_diffs.columns)

	for transformation in df_found.index:
	    reaction = df_mask.columns[df_mask.loc[transformation].values.flatten().tolist().index(True)]
	    df_trans_mz.loc[reaction]

	    # transformation_1 - transformation_2
	    transformation_1 = transformation.split(' - ')[0]
	    transformation_2 = transformation.split(' - ')[1]
	    diff = df_diffs[transformation_2][transformation_1]
	    reaction_diff = df_trans_mz.loc[reaction]
	    weight = abs(diff - reaction_diff).values[0]
	    df_weights.set_value(transformation_1, transformation_2, 1.0 - weight)

	df_weights = df_weights.fillna(value = 0.0)
	df_cyto = pd.melt(df_weights.reset_index(), id_vars = ['Metabolite'])
	df_cyto = df_cyto.rename(columns = {'Metabolite' : 'Metabolite_from', 'variable' : 'Metabolite_to', 'value' : 'Weight'})
	df_cyto.to_csv(fname_out + '.csv', index = False)
	df_cyto_pruned = df_cyto[df_cyto['Weight'] != 0.0]
	df_cyto_pruned.to_csv(fname_out + '_pruned.csv', index = False)
	print("...Finished at" + str(datetime.datetime.now()))



if __name__ == '__main__':
	MzRt_files = [x for x in os.listdir() if '.MzRtInfo' in x]
	[BioAge_file, MCDS_file, OE_file] = MzRt_files

	df_b = pd.DataFrame.from_csv(BioAge_file, sep = '\t')
	df_m = pd.DataFrame.from_csv(MCDS_file, sep = '\t')
	df_o = pd.DataFrame.from_csv(OE_file, sep = '\t')

	df_trans = pd.read_excel('transformations.xlsx', sheetname = 'Common chemical relationships')
	df_trans = df_trans.drop(0)
	df_trans.set_index('Element', inplace = True)
	df_trans.index.name = 'Reaction'
	# df_trans = df_trans.reset_index(drop = True)
	df_trans_mz = df_trans['Δm/z']
	# df_trans_mz.rename(columns = {'Δm/z' : 'a'}, inplace = True)
	df_trans_mz = pd.DataFrame(df_trans_mz)
	df_trans_mz.rename(columns = {'Δm/z' : 'delta_m.z'}, inplace = True)

	if not tasks:
		write_cyto_csv(df_b, 'BioAge')
		write_cyto_csv(df_m, 'MCDS')
		write_cyto_csv(df_o, 'OE')
	else:
		df_files = [df_b, df_m, df_o]
		names_out = ['BioAge', 'MCDS', 'OE']
		write_cyto_csv(df_files[task_num - 1], names_out[task_num - 1])
