# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:25:32 2023

@author: user
"""

import os
import sys
import json
import numpy as np
import coord_sutils as cs
import coord_plot as cp



def main(gfile_loc = None, verbose=False, shift= 1):
    
    newbase, tbase, drt, Attempt, i = cs.mast_coord_dir('org')
    
    print("Initializing SOLPSxport")
    xp = cp.SOLPSplot(workdir=newbase, gfile_loc=gfile_loc)
    print(newbase)
    
    
    # from IPython import embed; embed()
    
    print("Running calcPsiVals")
    try:
        xp.calcPsiVals(sname='org', geo=None, b2mn=None, dsa=None, shift=shift)
    except Exception as err:
        print('Exiting from SOLPSxport_dr\n')
        sys.exit(err)
        
    return xp


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate new b2.transport.inputfile files for SOLPS',
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('-g', '--gfileloc', help='location of profs_*.pkl saved profile file', type=str, default=None)
    # parser.add_argument('-p', '--profilesloc', help='location of profs_*.pkl saved profile file', type=str, default=None)
    # parser.add_argument('-s', '--shotnum', help='shot number; default = None', type=str, default=None)
    # parser.add_argument('-t', '--timeid', help='time of profile run; default = None', type=str, default=None)
    # parser.add_argument('-r', '--runid', help='profile run id; default = None', type=str, default=None)
    # parser.add_argument('-i', '--tiratiofile', help='File location for Ti/TD ratio; default = None', type=str, default=None)
    # parser.add_argument('-d', '--tdfileloc', help='File location for TD; default = None', type=str, default=None)
    # parser.add_argument('-f', '--fractional_change', help='Fractional change to transport coefficients; default = 1',
    #                     type=float, default=1)
    parser.add_argument('-sh', '--shift', help='shift of major radius; default = 1', type=float, default=1)
    
    args = parser.parse_args()
    
    x = main(gfile_loc=args.gfileloc, shift=args.shift)
    
    
    
    print("You are so great!")
    