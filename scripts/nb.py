import os
import sys
from pathlib import Path
from objects import Compound, CompoundGraph

script_dir = Path('.')
top_dir = script_dir / '..'
data_dir = top_dir / 'data'
h_dir = data_dir / 'HirschhornLab_MetabolomicsData'

imp_fname = h_dir / 'BioAge_spQC_miss0.5_medianMiceImp.txt'
mz_rt_fname = h_dir / 'BioAge_spQC_miss0.5.MzRtInfo.txt'


with open(mz_rt_fname) as f:
    lines = f.readlines()


# for line in lines[1 : ]:
    # [name, method, mz, rt] = line.strip().split('\t')
    # c = Compound(name, method, mz, rt)

cg = CompoundGraph()
