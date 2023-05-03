# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 22:44:30 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from scipy.optimize import curve_fit
import numpy as np
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'org_new_series'
series = ['orgb_tw_17_nts5_a']
n = '20tw'
s_choose = 0

basedrt, topdrt = tl.set_wdir()

if s_choose == 0:
    a_list = glob.glob('{}/{}/{}/{}/{}/b2.transport.inputfile_new'.format(basedrt, dev, shot, shift, series[0]))


xport_list = b2tp.InputfileParser(a_list[0], plot= False)


trans_list = b2tp.InputfileParser('b2.transport.inputfile_18tw', plot= False)
cod = trans_list['1'].T
coki = trans_list['3'].T
coke = trans_list['4'].T
x= cod[:,0]  #the coordinate here is R-R_sep
yd= cod[:,1]
yki = coki[:,1]
yke = coke[:,1]


log_flag = True
specieslist = ['1','3','4']
d = tl.unit_dic()
i = 0

for k in specieslist:
    if log_flag:
        plt.rcParams.update({'font.size': 20})
        plt.yscale('log')
        plt.figure(i + 1)
        if k == '1':
            plt.axvline(x=trans_list[k][0,12], color='black',lw=3)
            plt.axvline(x=trans_list[k][0,19], color='black',lw=3)
        if k == '4':
            plt.axvline(x=trans_list[k][0,13], color='black',lw=3)
            plt.axvline(x=trans_list[k][0,17], color='black',lw=3)
        plt.plot(trans_list[k][0,:], trans_list[k][1,:],'o-', color = 'green', label ='adjust transport coefficient')
        plt.plot(xport_list[k][0,:], xport_list[k][1,:],'o-', color = 'orange', label ='xport code generate transport coefficient')
        plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Calibri","size": 20})
        plt.ylabel(d[k][1], fontdict={"family":"Calibri","size": 20})
        plt.title(d[k][0],fontdict={"family":"Calibri","size": 20})
        plt.legend()
    i = i + 1

plt.show()
