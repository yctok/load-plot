# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:59:51 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
import numpy as np
import tools as tl
# import glob


a_list, n , filename, shift = tl.mast_tranco_dir('org')
print(a_list)


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
    if j<= 24:
        mod_y[j] = cod[j,1]
    else:
        mod_y[j] = 8.0
cod[:,1] = mod_y

mod_yki = np.zeros(m)
for j in range(m):
    if j<= 30:
        mod_yki[j] = coki[j,1]  
    else:
        mod_yki[j] = 10.0
coki[:,1] = mod_yki

mod_yke = np.zeros(m)
for j in range(m):
    if j<= 24:
        mod_yke[j] = coke[j,1]  
    else:
        mod_yke[j] = 18.0
coke[:,1] = mod_yke

b = b2tp.Generate(cod, CoeffID=1, SpeciesID=2, M=[1])
c = b2tp.WriteInputfile(file='b2.transport.inputfile_mod_{}{}'.format(shift, n), points= trans_list ,M_1 = True, M=[1])

log_flag = False
specieslist = ['1','3','4']
d = tl.unit_dic()
i = 0

for k in specieslist:
    if log_flag:
        plt.yscale('log')
        plt.figure(i + 1)
        plt.plot(trans_list[k][0,:], trans_list[k][1,:], 'o-', color = 'orange', label ='{} transport coefficient'.format(filename))
        plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
        plt.ylabel(d[k][1], fontdict={"family":"Times New Roman","size": 20})
        plt.title(d[k][0],fontdict={"family":"Times New Roman","size": 20})
        plt.legend()
    else:
        plt.figure(i + 1)
        plt.plot(trans_list[k][0,:], trans_list[k][1,:], 'o-', color = 'orange', label ='{} transport coefficient'.format(filename))
        plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
        plt.ylabel(d[k][1], fontdict={"family":"Times New Roman","size": 20})
        plt.title(d[k][0],fontdict={"family":"Times New Roman","size": 20})
        plt.legend()
    i = i + 1

plt.show()