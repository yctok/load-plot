# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:14:54 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
import numpy as np
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'dot5'
series = ['dn5hc7_1_ts5_dot5_a']
n = '36'
s_choose = 0

basedrt, topdrt = tl.set_wdir()

if s_choose == 0:
    a_list = glob.glob('{}/{}/{}/{}/{}/b2.transport.inputfile_new'.format(basedrt, dev, shot, shift, series[0]))


trans_list = b2tp.InputfileParser(a_list[0], plot= False)
cod = trans_list['1'].T
coki = trans_list['3'].T
coke = trans_list['4'].T
x= cod[:,0]  #the coordinate here is R-R_sep
yd= cod[:,1]
yki = coki[:,1]
yke = coke[:,1]

dot5_psi = tl.dsa_to_psi(x)


m = len(yd)