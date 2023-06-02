# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 21:37:36 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from equilibrium import equilibrium
import tools as tl
import glob

# dev = 'mast'
# shot = '027205'
# shift_a = 'one_LS'
# series_a = ['lsts5_tw_17_one_a']
# shift_b = 'org_new_series'
# series_b = ['ch_hh_30_nts5_a']

# s_choose = 0

# basedrt, topdrt, tpdrt= tl.set_wdir()

# if s_choose == 0:
#     a_list = glob.glob('{}/{}/{}/{}/*_sh_nts5_a'.format(basedrt, dev, shot, shift_b))
#     a_list.sort(key=tl.s1_number)
#     print(a_list)
    
    
# key = tl.s1_number(a_list[0])
# print(key)

a_list, filename, shift = tl.mast_multi_dir('one')
n_dir = len(a_list)
print(a_list)

basedrt, topdrt, tpdrt= tl.set_wdir()
d = tl.mast_dir_dic()