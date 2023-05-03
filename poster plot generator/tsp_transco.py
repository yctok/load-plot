# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:58:14 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from scipy.optimize import curve_fit
import numpy as np
import tools as tl
import glob



trans_list = b2tp.InputfileParser('b2.transport.inputfile_20tw', plot= False)
cod = trans_list['1'].T
coki = trans_list['3'].T
coke = trans_list['4'].T
x= cod[:,0]  #the coordinate here is R-R_sep
yd= cod[:,1]
yki = coki[:,1]
yke = coke[:,1]

pn = [0.13, 2.37, 0.00001]
pe = [1.81, 1.69, 0.00001]
pi = [0.88, 1.12, 0.00001]


popt_ne, pcov_ne = curve_fit(tl.flat_tanh, x, yd, pn)
print(popt_ne)
popt_te, pcov_te = curve_fit(tl.flat_tanh, x, yke, pe)
print(popt_te)
popt_ti, pcov_ti = curve_fit(tl.flat_tanh, x, yki, pi)
print(popt_ti)


one_trans_list = b2tp.InputfileParser('b2.transport.inputfile_one', plot= False)
one_x= trans_list['1'][0,:].T

tanh_ne_fit = tl.flat_tanh(one_x, popt_ne[0], popt_ne[1], popt_ne[2])
tanh_te_fit = tl.flat_tanh(one_x, popt_te[0], popt_te[1], popt_te[2])
tanh_ti_fit = tl.flat_tanh(one_x, popt_ti[0], popt_ti[1], popt_ti[2])

one_trandic = {'1': tanh_ne_fit, '3':tanh_ti_fit, '4': tanh_te_fit}

b = b2tp.Generate(cod, CoeffID=1, SpeciesID=2, M=[1])
# c = b2tp.WriteInputfile(file='b2.transport.inputfile_{}'.format(n), points= trans_list ,M_1 = True, M=[1])



log_flag = True
specieslist = ['1','3','4']
d = tl.unit_dic()
i = 0

for k in specieslist:
    if log_flag:
        plt.yscale('log')
        plt.figure(i + 1)
        plt.plot(trans_list[k][0,:], trans_list[k][1,:], label ='{} transport coefficient'.format('20tw'))
        plt.plot(one_x, one_trandic[k], label ='fit transport coefficient'.format('20tw'))
        plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
        plt.ylabel(d[k][1], fontdict={"family":"Times New Roman","size": 20})
        plt.title(d[k][0],fontdict={"family":"Times New Roman","size": 20})
        plt.legend()
    i = i + 1

plt.show()