# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:48:58 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from scipy import interpolate
import numpy as np
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'one_LS'
series = ['lsts5_19_tw_one_a']
n = '36'
one_n = '24'
s_choose = 0

basedrt, topdrt, tpdrt = tl.set_wdir()

if s_choose == 0:
    org_list = glob.glob('{}/b2.transport.inputfile_{}'.format(tpdrt, n))
    one_list = glob.glob('{}/{}/{}/{}/{}/b2.transport.inputfile_new'.format(basedrt, dev, shot, shift, series[0]))


trans_list = b2tp.InputfileParser(org_list[0], plot= False)
cod = trans_list['1'].T
coki = trans_list['3'].T
coke = trans_list['4'].T
x= cod[:,0]  #the coordinate here is R-R_sep
yd= cod[:,1]
yki = coki[:,1]
yke = coke[:,1]

m = len(yd)

one_trans = b2tp.InputfileParser(one_list[0], plot= False)
ond = one_trans['1'].T
onki = one_trans['3'].T
onke = one_trans['4'].T
onx= ond[:,0]  #the coordinate here is R-R_sep
fd = ond[:,1]
fki = onki[:,1]
fke = onke[:,1]

d_func = interpolate.interp1d(x, yd, fill_value = 'extrapolate')
ond[:,1] = d_func(onx)
ki_func = interpolate.interp1d(x, yki, fill_value = 'extrapolate')
onki[:,1] = ki_func(onx)
ke_func = interpolate.interp1d(x, yke, fill_value = 'extrapolate')
onke[:,1] = ke_func(onx)

# yd= cod[:,1]
# yki = coki[:,1]
# yke = coke[:,1]



b = b2tp.Generate(cod, CoeffID=1, SpeciesID=2, M=[1])
c = b2tp.WriteInputfile(file='b2.transport.inputfile_one{}'.format(one_n), points= one_trans ,M_1 = True, M=[1])



log_flag = True
specieslist = ['1','3','4']
d = tl.unit_dic()
i = 0

for k in specieslist:
    if log_flag:
        plt.yscale('log')
        plt.figure(i + 1)
        plt.plot(trans_list[k][0,:], trans_list[k][1,:], 'o-',color = 'blue', label ='{} transport coefficient'.format('orgin_case'))
        plt.plot(one_trans[k][0,:], one_trans[k][1,:], 'o-', color = 'orange', label ='{} transport coefficient'.format('one_case'))
        plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
        plt.ylabel(d[k][1], fontdict={"family":"Times New Roman","size": 20})
        plt.title(d[k][0],fontdict={"family":"Times New Roman","size": 20})
        plt.legend()
    i = i + 1

plt.show()


#     elif j>= 15 and j <= 16:
#         mod_y[j] = cod[j,1]

#     elif j>= 14 and j <= 17:
#         mod_yke[j] = coke[j,1]

#     elif j>= 14 and j <= 17:
#         mod_yki[j] = coki[j,1]

