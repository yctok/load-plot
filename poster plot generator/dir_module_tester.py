# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 21:02:35 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from equilibrium import equilibrium
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'org'
series = ['try & error','p4_d6', 'p4_d6_11',
          '1ex_input0.1%_ts6_series', '4ex_n_decay0.06_ts6_series',
          '5ex_n_decay0.03_ts6_series', '6ex_input0.2%_ts6_series',
          'p4_d6_7', 'no_flux_false']
ex1 = '1ex_p4_input0.1%_'
ex4 = '4ex_p4_d6'
ex5 = '5ex_p4_d3'
ex6 = '6ex_p4_input0.2%_'
ex7 = '7ex_p4_d6'
s_choose = 5

basedrt, topdrt = tl.set_wdir()

a = '{}/{}/{}/{}/{}/{}'.format(basedrt, dev, shot, shift, series[7], ex7)
print(a)


if s_choose == 0:
    a_list = glob.glob('{}/{}/{}/{}/{}/p4_*'.format(basedrt, dev, shot, shift, series[0]))
    a_list.sort(key=tl.a_number)
    
    
elif s_choose == 1:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[1]))
    a_list.sort(key=tl.a_number)
    
elif s_choose == 2:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[2]))
    b_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[3], ex1))
    a_list.sort(key=tl.a_number)
    b_list.sort(key=tl.ex1_number)

    for ii in range(len(b_list)):
        a_list.append(b_list[ii])

elif s_choose == 3:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[2]))
    b_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[4], ex4))
    print(b_list)
    a_list.sort(key=tl.a_number)
    b_list.sort(key=tl.ex1_number)

    for ii in range(len(b_list)):
        a_list.append(b_list[ii])

elif s_choose == 4:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[2]))
    b_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[5], ex5))
    print(b_list)
    a_list.sort(key=tl.a_number)
    b_list.sort(key=tl.ex1_number)

    for ii in range(len(b_list)):
        a_list.append(b_list[ii])
        
elif s_choose == 5:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[2]))
    b_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[6], ex6))
    print(b_list)
    a_list.sort(key=tl.a_number)
    b_list.sort(key=tl.ex1_number)

    for ii in range(len(b_list)):
        a_list.append(b_list[ii])
        
elif s_choose == 6:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[7]))
    b_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[8], ex7))
    print(b_list)
    a_list.sort(key=tl.a_number)
    b_list.sort(key=tl.ex1_number)

    for ii in range(len(b_list)):
        a_list.append(b_list[ii])