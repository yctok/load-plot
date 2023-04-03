# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 19:00:32 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from equilibrium import equilibrium
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'org'
series = ['p4_d6_11', '1ex_input0.1%_ts6_series']
ex1 = '1ex_p4_input0.1%_'
a_list = []
b_list = []
basedrt, topdrt = tl.set_wdir()

a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[0]))
b_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[1], ex1))
# print(b_list)
# print(len(a_list))

a_list.sort(key=tl.a_number)

b_list.sort(key=tl.ex1_number)
# print(b_list)


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
last10_list = ['ne3da.last10', 'te3da.last10', 'an3da.last10']
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
        R_sep = b2tp.PsiN2R(eq, 1.0)
        new_R = []
        for R in Attempt[0]:
                A = R + R_sep
                B = b2tp.R2PsiN(eq,A)
                new_R.append(float(B))
        Attempt[0]= new_R
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

ii = 90
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
nn = 1

for c in last10_list:
    plt.figure(nn)
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