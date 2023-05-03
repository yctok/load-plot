# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:27:38 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from equilibrium import equilibrium
import tools as tl
import fit_density as fd
import glob

dev = 'mast'
shot = '027205'
shift_a = 'one_LS'
series_a = ['lsts5_tw_17_one_a']
shift_b = 'org_new_series'
series_b = ['24l_u_25_nts5_a']

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

# a, b = fd.dat_fit()


n_dir = len(a_list)

attempt_name = []


for j in range(n_dir):
    name = a_list[j]
    attempt_name.append(name.split("/",-1)[-2])

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


psi_fit = data['an3da.last10']['24l_u_25_nts5_a'][0,:]
r_rsep = tl.psi_to_dsa(psi_fit)
an3da = data['an3da.last10']['24l_u_25_nts5_a'][1,:]
xam = len(psi_fit)
x_fit = []
an_sh = []
for i in range(xam - 1):
    if r_rsep[i+ 1] <= 0:
        x_fit.append(r_rsep[i +1])
        an_sh.append(an3da[i +1])
shift_x = np.zeros(len(x_fit))
norm_an = np.zeros(len(x_fit))
for ii in range(len(x_fit)):
    shift_x[ii] = x_fit[ii]
    norm_an[ii] = an_sh[ii]/max(an_sh)

# psi_ax = shift_x + 1

pn = [1, 50]


popt_an, pcov_an = curve_fit(tl.expfit, shift_x, norm_an, pn)
print(popt_an)

# coe = max(an_sh)/popt_an[0]

new_x = []
for i in range(xam - 1):
    if r_rsep[i] <= 0.007:
        new_x.append(r_rsep[i])
new_x = np.array(new_x)
# shift_x = np.zeros(len(x_fit))
# norm_an = np.zeros(len(x_fit))
# for ii in range(len(x_fit)):
#     shift_x[ii] = x_fit[ii]
#     norm_an[ii] = an_sh[ii]/max(an_sh)


exp_an_fit = tl.expfit(new_x, popt_an[0], popt_an[1])*max(an_sh)
g1_an_fit = tl.expfit(new_x, popt_an[0], popt_an[1]*1.5)*max(an_sh)
g2_an_fit = tl.expfit(new_x, popt_an[0], popt_an[1]*0.5)*max(an_sh)

xv = 1/popt_an[1]


# one_trandic = {'1': tanh_ne_fit, '3':tanh_ti_fit, '4': tanh_te_fit}       

    



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

rsep_d = tl.psi_to_dsa(ne_sh)
rd = tl.psi_to_dsa(psi_sh)
dn, dt = fd.dat_fit()
# dn_r = tl.psi_to_dsa(dn)


plot_dic = tl.unit_dic()
log_flag = False
nn = 1


# plt.figure(1)

x = [-xv, 0]
y = [max(an_sh), max(an_sh)]
xd = [-dn, dn]
yd = [ne_sh[100], ne_sh[100]]


ax1 = plt.subplot(212)
plt.rcParams.update({'font.size': 20})
plt.plot(r_rsep, an3da,'o-', color = 'green', label= 'solps simulation')
plt.plot(new_x, exp_an_fit, color='r',lw=5, label= 'exponential fit')
plt.plot(new_x, g1_an_fit, color='b', lw=5, ls='--')
plt.plot(new_x, g2_an_fit, color='b', lw=5, ls='--')
plt.axvline(x=0, color='orange',lw=3)
plt.plot(x,y, color='orange', lw=3, label= 'Neutral penetration length [m]: $\lambda_{n_D}$')
plt.axvline(x=-xv, color='orange',lw=3)
plt.axvline(x=dn, color='black',lw=3, ls='--')
plt.axvline(x=-dn, color='black',lw=3, ls='--')
plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Calibri","size": 20})
plt.ylabel(plot_dic['an3da.last10'][1], fontdict={"family":"Calibri","size": 20})
# plt.title(plot_dic['an3da.last10'][0],fontdict={"family":"Calibri","size": 20})
plt.legend()

ax2 = plt.subplot(211, sharex= ax1)
plt.rcParams.update({'font.size': 20})
plt.plot(rd, ne_sh,'o-', color = 'r', label= 'experimental density fit')
plt.plot(xd, yd, color='black', lw=3, label= 'Pedestal width [m]: $\Delta$')
plt.axvline(x=dn, color='black',lw=3)
plt.axvline(x=-dn, color='black',lw=3)
plt.axvline(x=0, color='orange',lw=3, ls='--')
plt.axvline(x=-xv, color='orange',lw=3, ls='--')
# plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Calibri","size": 20})
plt.ylabel(plot_dic['ne3da.last10'][1], fontdict={"family":"Calibri","size": 20})
# plt.title(plot_dic['ne3da.last10'][0],fontdict={"family":"Calibri","size": 20})
plt.legend()

plt.show()




# plt.figure(1)
# plt.rcParams.update({'font.size': 20})
# plt.plot(r_rsep, an3da,'o-', color = 'green', label= 'solps simulation')
# plt.plot(new_x, exp_an_fit, color='r',lw=5, label= 'exponential fit')
# plt.plot(new_x, g1_an_fit, color='b', lw=5, ls='--')
# plt.plot(new_x, g2_an_fit, color='b', lw=5, ls='--')
# plt.plot(x,y, color='black', lw=3, label= 'Neutral penetration length [m]: $\lambda_{n_D}$')
# plt.axvline(x=0, color='orange',lw=3)
# plt.axvline(x=-xv, color='orange',lw=3)
# # plt.axhline(y= float(an_sh[17]),xmin= -0.01, color='orange', lw=3)
# plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Calibri","size": 20})
# plt.ylabel(plot_dic['an3da.last10'][1], fontdict={"family":"Calibri","size": 20})
# plt.title(plot_dic['an3da.last10'][0],fontdict={"family":"Calibri","size": 20})
# plt.legend()




plt.show()







# for c in last10_list:
#     plt.figure(nn)
#     plt.rcParams.update({'font.size': 20})
#     if log_flag:
#         plt.yscale('log')
#     for m in range(n_dir):
#         # plt.plot(data[c][attempt_name[m]][0], data[c][attempt_name[m]][1],'o-', color = 'green', label= attempt_name[m])
#         plt.plot(data[c][attempt_name[m]][0], data[c][attempt_name[m]][1],'o-', color = 'green', label= 'solps simulation')
#     if c == 'ne3da.last10':
#         plt.scatter(psi_sh, ne_sh, color = 'orange', label= 'electron density experiment fit')
#     if c == 'te3da.last10':
#         plt.scatter(psi_sh, te_sh, color = 'orange', label= 'electron temperature experiment fit')
#     if c == 'an3da.last10':
#         plt.plot(new_x, exp_an_fit, color='r',lw=5, label= 'exponential fit')
#         plt.plot(new_x, g1_an_fit, color='b', lw=5, ls='--')
#         plt.plot(new_x, g2_an_fit, color='b', lw=5, ls='--')
#         plt.axvline(x=1, color='orange',lw=3)
#         plt.axvline(x=1- xv, color='orange',lw=3)
#     plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Calibri","size": 20})
#     plt.ylabel(plot_dic[c][1], fontdict={"family":"Calibri","size": 20})
#     plt.title(plot_dic[c][0],fontdict={"family":"Calibri","size": 20})
#     plt.legend()
#     nn = nn + 1