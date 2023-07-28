# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 10:48:58 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from scipy import interpolate
import tools as tl

one_list, n , filename_a, shift_a = tl.mast_tranco_dir('one')
print(one_list)
org_list = tl.mast_std_dir()

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


b = b2tp.Generate(cod, CoeffID=1, SpeciesID=2, M=[1])
c = b2tp.WriteInputfile(file='b2.transport.inputfile_align_{}_{}'.format(shift_a, n), points= one_trans ,M_1 = True, M=[1])

log_flag = True
specieslist = ['1','3','4']
d = tl.unit_dic()
i = 0

for k in specieslist:
    if log_flag:
        plt.yscale('log')
        plt.figure(i + 1)
        plt.plot(trans_list[k][0,:], trans_list[k][1,:], 'o-',color = 'blue', label ='orgin_case transport coefficient')
        plt.plot(one_trans[k][0,:], one_trans[k][1,:], 'o-', color = 'orange', label ='{}_case transport coefficient'.format(shift_a))
        plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
        plt.ylabel(d[k][1], fontdict={"family":"Times New Roman","size": 20})
        plt.title(d[k][0],fontdict={"family":"Times New Roman","size": 20})
        plt.legend()
    i = i + 1

plt.show()


