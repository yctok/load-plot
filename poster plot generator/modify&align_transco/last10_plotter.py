# -*- coding: utf-8 -*-
"""
Created on Mon May  1 01:37:11 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from equilibrium import equilibrium
import tools as tl
import glob

# dev = 'mast'
# shot = '027205'
# shift_a = 'one_LS'
# series_a = ['lsts5_tw_17_one_a']
# shift_b = 'org_new_series'
# series_b = ['ch_hh_30_nts5_a']

# s_choose = 1

# basedrt, topdrt, tpdrt= tl.set_wdir()

# if s_choose == 0:
#     a_list = glob.glob('{}/{}/{}/{}/{}/'.format(basedrt, dev, shot, shift_a, series_a[0]))
#     a_list.sort(key=tl.new_number)
# elif s_choose == 1:
#     a_list = glob.glob('{}/{}/{}/{}/{}/'.format(basedrt, dev, shot, shift_b, series_b[0]))
#     a_list.sort(key=tl.new_number)
      
# key = tl.new_number(a_list[0])
# print(key)




# n_dir = len(a_list)

# attempt_name = []


# for j in range(n_dir):
#     name = a_list[j]
#     attempt_name.append(name.split("/",-1)[-2])

# print(attempt_name)


a_list, attempt_name, shift = tl.mast_multi_dir('org')
n_dir = len(a_list)
print(a_list)

basedrt, topdrt, tpdrt= tl.set_wdir()
d = tl.mast_dir_dic()


gtr = glob.glob('{}/{}/{}/g{}*'.format(topdrt, d['dev'], d['shot'], d['shot']))
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
filename = 'wsh_027205_275.dat'
fitfile_loc = '{}/{}/{}'.format(basedrt, d['dev'], filename)
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
log_flag = False
nn = 1

for c in last10_list:
    plt.figure(nn)
    plt.rcParams.update({'font.size': 20})
    if log_flag:
        plt.yscale('log')
    for m in range(n_dir):
        plt.plot(data[c][attempt_name[m]][0], data[c][attempt_name[m]][1],'o-', label= attempt_name[m])
        # plt.plot(data[c][attempt_name[m]][0], data[c][attempt_name[m]][1],'o-', color = 'green', label= 'solps simulation')
    if c == 'ne3da.last10':
        plt.scatter(psi_sh, ne_sh, color = 'orange', label= 'electron density experiment fit')
    if c == 'te3da.last10':
        plt.scatter(psi_sh, te_sh, color = 'orange', label= 'electron temperature experiment fit')
    plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Calibri","size": 20})
    plt.ylabel(plot_dic[c][1], fontdict={"family":"Calibri","size": 20})
    plt.title(plot_dic[c][0],fontdict={"family":"Calibri","size": 20})
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

for x in div_last10:
    plt.figure(nn)
    if log_flag:
        plt.yscale('log')
    for e in range(n_dir):
        plt.plot(data[x][attempt_name[e]][0], data[x][attempt_name[e]][1], label= attempt_name[e])
    plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Calibri","size": 20})
    plt.ylabel(plot_dic[x][1], fontdict={"family":"Calibri","size": 20})
    plt.title(plot_dic[x][0],fontdict={"family":"Calibri","size": 20})
    plt.legend()
    nn = nn + 1

plt.show()
    

