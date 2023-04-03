# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:53:11 2023

@author: Yi-Cheng
"""

import numpy as np


def loadg(filename):
    infile = open(filename, 'r')
    lines = infile.readlines()

    # read first line for case string and grid size
    line = lines[0]
    words = line.split()

    nw = int(words[-2])
    nh = int(words[-1])
    psi = np.linspace(0, 1, nw)

    # read in scalar parameters
    #   note: word size of 16 characters each is assumed for all of the data to be read

    # line 1
    line = lines[1]
    rdim = float(line[0:16])
    zdim = float(line[16:32])
    rcentr = float(line[32:48])
    rleft = float(line[48:64])
    zmid = float(line[64:80])

    # line 2
    line = lines[2]
    rmaxis = float(line[0:16])
    zmaxis = float(line[16:32])
    simag = float(line[32:48])
    sibry = float(line[48:64])
    bcentr = float(line[64:80])

    # line 3
    line = lines[3]
    current = float(line[0:16])

    # read in profiles
    #   start by reading entire file into single list then split into individual profiles
    #   first block has 5 profiles of length nw and one array of length nh*nw

    temp = []
    count = 0
    lnum = 5
    terms = 5 * nw + nw * nh
    while count < terms:
        line = lines[lnum]
        numchar = len(line)
        nwords = numchar // 16
        count1 = 0
        while count1 < nwords:
            i1 = count1 * 16
            i2 = i1 + 16
            temp.append(float(line[i1:i2]))
            count1 += 1
            count += 1
        lnum += 1

    fpol = temp[0:nw]
    pres = temp[nw:2 * nw]
    ffprime = temp[2 * nw:3 * nw]
    pprime = temp[3 * nw:4 * nw]
    psirz_temp = temp[4 * nw:(4 + nh) * nw]
    qpsi = temp[(4 + nh) * nw:]

    # split psirz up into 2D matrix
    count = 0
    psirz = []
    while count < nh:
        ind1 = count * nw
        ind2 = ind1 + nw
        psirz.append(psirz_temp[ind1:ind2])
        count += 1

    # scalars for length of boundary and limiter arrays
    line = lines[lnum]
    words = line.split()
    nbbbs = int(words[0])
    limitr = int(words[1])

    # read boundary and limiter points into temp array

    temp = []
    count = 0
    terms = 2 * (nbbbs + limitr)
    lnum += 1
    while count < terms:
        line = lines[lnum]
        numchar = len(line)
        nwords = numchar // 16
        count1 = 0
        while count1 < nwords:
            i1 = count1 * 16
            i2 = i1 + 16
            temp.append(float(line[i1:i2]))
            count1 += 1
            count += 1
        lnum += 1
    bdry_temp = temp[0:(2 * nbbbs)]
    limit_temp = temp[(2 * nbbbs):]

    # split boundary into (R,Z) pairs
    count = 0
    rbdry = []
    zbdry = []
    while count < len(bdry_temp) - 1:
        rbdry.append(bdry_temp[count])
        zbdry.append(bdry_temp[count + 1])
        count += 2

    # split limiter into (R,Z) pairs
    count = 0
    rlim = []
    zlim = []
    while count < len(limit_temp) - 1:
        rlim.append(limit_temp[count])
        zlim.append(limit_temp[count + 1])
        count += 2

    g = dict(nw=nw, nh=nh, rdim=rdim, zdim=zdim, rcentr=rcentr, rleft=rleft, zmid=zmid,
             rmaxis=rmaxis, zmaxis=zmaxis, simag=simag, sibry=sibry, current=current,
             fpol=np.array(fpol),
             ffprime=np.array(ffprime), pprime=np.array(pprime), psirz=np.array(psirz),
             qpsi=np.array(qpsi), nbbbs=nbbbs, bcentr=bcentr,
             pres=np.array(pres), limitr=limitr, rbdry=np.array(rbdry),
             zbdry=np.array(zbdry), rlim=np.array(rlim), zlim=np.array(zlim))

    return g

