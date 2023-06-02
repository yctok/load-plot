# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 05:01:31 2023

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
ex7 = '7ex_p4_d6_'
s_choose = 1

basedrt, topdrt, tpdrt = tl.set_wdir()

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
        
      


n_dir = len(a_list)

attempt_name = []


for j in range(n_dir):
    name = a_list[j]
    attempt_name.append(name.split('\\',1)[1])

print(attempt_name)


gtr = glob.glob('{}/{}/{}/g{}*'.format(topdrt, dev, shot, shot))
print(gtr)

fd_list = []
last10_list = [
    'ne3da.last10', 'te3da.last10', 'an3da.last10']
fd_dic = {}


for jj in last10_list:
    fd_list = []
    for i in range(n_dir):
        fd_list.append('{}/{}'.format(a_list[i], jj))
    fd_dic[jj] = fd_list
    # print(fd_list[i])

# print(fd_list)


eq = equilibrium(gfile=gtr[-1])

data = {}
nest = {}
for kk in last10_list:
    nest = {}
    for k in range(n_dir):
        Attempt = np.loadtxt(fd_dic[kk][k])
        Attempt = Attempt.T
        Attempt[0]= tl.dsa_to_psi(Attempt[0])
        # Attempt = Attempt.T
        nest[attempt_name[k]] = Attempt
    data[kk] = nest

# color_list = 
filename = 'fit_027205_275.dat'
fitfile_loc = '{}/{}/{}'.format(basedrt, dev, filename)
mast_dat_dict = tl.read_fitfile(fitfile_loc)
psi = mast_dat_dict['psi_normal']
ne = mast_dat_dict['electron_density(m^(-3))']
te = mast_dat_dict['electron_temperature(eV)']

ii = 75
delta = len(ne) - ii
print(delta)
psi_sh = []
ne_sh = []
te_sh = []
for i in range(delta):
    # print(psi[ii])
    psi_sh.append(psi[ii])
    ne_sh.append(ne[ii])
    te_sh.append(te[ii])
    ii = ii + 1


plot_dic = tl.unit_dic()
log_flag = True
nn = 1

for c in last10_list:
    plt.figure(nn)
    if log_flag:
        plt.yscale('log')
    for m in range(n_dir):
        plt.plot(data[c][attempt_name[m]][0], data[c][attempt_name[m]][1], label= attempt_name[m])
    if c == 'ne3da.last10':
        plt.scatter(psi_sh, ne_sh, label= 'electron density experiment data')
    if c == 'te3da.last10':
        plt.scatter(psi_sh, te_sh, label= 'electron temperature experiment data')
    plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Times New Roman","size": 20})
    plt.ylabel(plot_dic[c][1], fontdict={"family":"Times New Roman","size": 20})
    plt.title(plot_dic[c][0],fontdict={"family":"Times New Roman","size": 20})
    plt.legend()
    nn = nn + 1

div_list = []
div_last10 = [
    'ne3dl.last10', 'te3dl.last10', 'an3dl.last10',
    'ne3dr.last10', 'te3dr.last10', 'an3dr.last10',
    'te3di.last10']
div_dic = {}


for w in div_last10:
    div_list = []
    for x in range(n_dir):
        div_list.append('{}/{}'.format(a_list[x], w))
    div_dic[w] = div_list


for a in div_last10:
    div_nest = {}
    for b in range(n_dir):
        div_data = np.loadtxt(div_dic[a][b])
        div_data = div_data.T
        # div_data[0]= tl.dsa_to_psi(div_data[0])
        div_nest[attempt_name[b]] = div_data
    data[a] = div_nest

for d in div_last10:
    plt.figure(nn)
    if log_flag:
        plt.yscale('log')
    for e in range(n_dir):
        plt.plot(data[d][attempt_name[e]][0], data[d][attempt_name[e]][1], label= attempt_name[e])
    plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
    plt.ylabel(plot_dic[d][1], fontdict={"family":"Times New Roman","size": 20})
    plt.title(plot_dic[d][0],fontdict={"family":"Times New Roman","size": 20})
    plt.legend()
    nn = nn + 1

plt.show()
    

