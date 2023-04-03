# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 05:01:31 2023

@author: user
"""

psi_solps =[0.56591402, 0.59635553, 0.65365526, 0.70507622, 0.75083496,
        0.79132874, 0.82698182, 0.85806206, 0.88490369, 0.90789432,
        0.92738632, 0.94367313, 0.95706941, 0.96795829, 0.97677538,
        0.9838775 , 0.98955578, 0.99415907, 0.99803803, 1.002408  ,
        1.00753157, 1.01263476, 1.01772166, 1.02279374, 1.02785249,
        1.03288158, 1.03794617, 1.04306613, 1.04817989, 1.05328886,
        1.05838546, 1.06347049, 1.06855367, 1.07363646, 1.07872032,
        1.08380671, 1.08889011, 1.09145489]

import numpy as np
import matplotlib.pyplot as plt
from equilibrium import equilibrium
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'org'
series = ['try & error','p4_d6']
s_choose = 1

a_list = []
# b_list = []
basedrt, topdrt = tl.set_wdir()

if s_choose == 0:
    a_list = glob.glob('{}/{}/{}/{}/{}/p4_*'.format(basedrt, dev, shot, shift, series[0]))
elif s_choose == 1:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[1]))
    
# b_list = glob.glob('{}/{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[1], ex1))
# print(b_list)
# print(len(a_list))

a_list.sort(key=tl.a_number)

# b_list.sort(key=tl.ex1_number)
# print(b_list)


# for ii in range(len(b_list)):
#     a_list.append(b_list[ii])

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
        Attempt[0]= psi_solps
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

plt.show()