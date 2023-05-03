# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:16:14 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
import numpy as np
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'org_new_series'
series = ['h7d5orgb_del0.1%sp_15_nts5_a']
n = '16spsh'
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

m = len(yd)
mod_y = np.zeros(m)
for j in range(m):
    if j< 13:
        mod_y[j] = 22
    elif j>= 13 and j <= 23:
        mod_y[j] = cod[j,1]
    
    else:
        mod_y[j] = 22
mod_y = mod_y*0.6

cod[:,1] = mod_y

mod_yki = np.zeros(m)
for j in range(m):
    if j< 13:
        mod_yki[j] = 6.00
    elif j>= 13 and j <= 17:
        mod_yki[j] = coki[j,1]
    
    else:
        mod_yki[j] = 2.58
        
coki[:,1] = mod_yki

mod_yke = np.zeros(m)
for j in range(m):
    if j< 14:
        mod_yke[j] = 7.00
    elif j>= 14 and j <= 16:
        mod_yke[j] = coke[j,1]
    
    else:
        mod_yke[j] = 3.50
        
coke[:,1] = mod_yke


b = b2tp.Generate(cod, CoeffID=1, SpeciesID=2, M=[1])
c = b2tp.WriteInputfile(file='b2.transport.inputfile_{}'.format(n), points= trans_list ,M_1 = True, M=[1])



log_flag = True
specieslist = ['1','3','4']
d = tl.unit_dic()
i = 0

for k in specieslist:
    if log_flag:
        plt.yscale('log')
        plt.figure(i + 1)
        plt.plot(trans_list[k][0,:], trans_list[k][1,:], 'o-', color = 'orange', label ='{} transport coefficient'.format(series[0]))
        plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
        plt.ylabel(d[k][1], fontdict={"family":"Times New Roman","size": 20})
        plt.title(d[k][0],fontdict={"family":"Times New Roman","size": 20})
        plt.legend()
    i = i + 1

plt.show()