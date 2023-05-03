# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:20:33 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
import numpy as np
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift_a = 'one_LS'
series_a = ['lsts5_tw_17_one_a']
shift_b = 'org_new_series'
series_b = ['24l_tw_27_nts5_a']

s_choose = 1

basedrt, topdrt = tl.set_wdir()

if s_choose == 0:
    a_list = glob.glob('{}/{}/{}/{}/{}/'.format(basedrt, dev, shot, shift_a, series_a[0]))
    a_list.sort(key=tl.new_number)
elif s_choose == 1:
    a_list = glob.glob('{}/{}/{}/{}/{}/'.format(basedrt, dev, shot, shift_b, series_b[0]))
    a_list.sort(key=tl.new_number)
      
key = tl.new_number(a_list[0])
print(key)

# name = a_list[0]
# t = name.split("/",-1)[-2]
# print(t)


n_dir = len(a_list)

attempt_name = []


for j in range(n_dir):
    name = a_list[j]
    attempt_name.append(name.split("/",-1)[-2])


file='b2.transport.inputfile'
fd_list = []
for i in range(n_dir):
    fd_list.append('{}/{}'.format(a_list[i], file))



trans_dic = {}
# trans_list = ['1','3', '4']
trans_list = ['1', '4']

for k in range(n_dir):
    trans_dic[attempt_name[k]] = b2tp.InputfileParser(fd_list[k], plot= False)
    for m in trans_list:
        trans_dic[attempt_name[k]][m][0,:] = tl.dsa_to_psi(trans_dic[attempt_name[k]][m][0,:])
    
   
# psi = tl.dsa_to_psi(trans_dic[attempt_name[0]]['1'][0,:])
# plt.plot(trans_dic[attempt_name[0]]['1'][0,:], trans_dic[attempt_name[0]]['1'][1,:], label= attempt_name[0])
# plt.plot(psi, trans_dic[attempt_name[0]]['1'][1,:], label= attempt_name[0])

# plt.show()


plot_dic = tl.unit_dic()
nn = 0


for d in trans_list:
    # plt.figure(nn)
    # plt.yscale('log')
    for e in range(n_dir):
        plt.rcParams.update({'font.size': 20})
        # plt.plot(trans_dic[attempt_name[e]][d][0,:], trans_dic[attempt_name[e]][d][1,:], label= attempt_name[e])
        plt.plot(trans_dic[attempt_name[e]][d][0,:], trans_dic[attempt_name[e]][d][1,:],'o-', label= plot_dic[d][0])
    plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Calibri","size": 20})
    plt.ylabel(plot_dic[d][1], fontdict={"family":"Calibri","size": 20})
    # plt.title(plot_dic[d][0],fontdict={"family":"Times New Roman","size": 20})
    plt.title('Transport coefficient',fontdict={"family":"Calibri","size": 20})
    plt.legend()
    nn = nn + 1

plt.show()

    



# trans_co = trans_list['1']
# x= trans_co[0,:]  #the coordinate here is R-R_sep