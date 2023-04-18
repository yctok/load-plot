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
shift = 'org'
series = ['try & error','p4_d6_11', 'p4_d6_11',
          '1ex_input0.1%_ts6_series', '4ex_n_decay0.06_ts6_series',
          '5ex_n_decay0.03_ts6_series', '6ex_input0.2%_ts6_series',
          'p4_d6_7', 'no_flux_false']
ex1 = '1ex_p4_input0.1%_'
ex4 = '4ex_p4_d6'
ex5 = '5ex_p4_d3'
ex6 = '6ex_p4_input0.2%_'
ex7 = '7ex_p4_d6'
s_choose = 1

basedrt, topdrt = tl.set_wdir()

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
        
elif s_choose == 7:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[2]))
    # a_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[8], ex7))
    a_list.sort(key=tl.a_number)
    # a_list.sort(key=tl.ex1_number)


n_dir = len(a_list)

attempt_name = []

for j in range(n_dir):
    name = a_list[j]
    attempt_name.append(name.split('\\',1)[1])

file='b2.transport.inputfile'
fd_list = []
for i in range(n_dir):
    fd_list.append('{}/{}'.format(a_list[i], file))



trans_dic = {}
trans_list = ['1', '3', '4']

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
    plt.figure(nn)
    plt.yscale('log')
    for e in range(n_dir):
        plt.plot(trans_dic[attempt_name[e]][d][0,:], trans_dic[attempt_name[e]][d][1,:], label= attempt_name[e])
    plt.xlabel('radial coordinate: ', fontdict={"family":"Times New Roman","size": 20})
    plt.ylabel(plot_dic[d][1], fontdict={"family":"Times New Roman","size": 20})
    plt.title(plot_dic[d][0],fontdict={"family":"Times New Roman","size": 20})
    plt.legend()
    nn = nn + 1

plt.show()

    



# trans_co = trans_list['1']
# x= trans_co[0,:]  #the coordinate here is R-R_sep