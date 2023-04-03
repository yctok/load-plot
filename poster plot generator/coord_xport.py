# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:25:47 2023

@author: Yi-Cheng
"""

import SOLPSutils as sut

class SOLPSxport:

    def __init__(self, workdir, gfile_loc, impurity_list=[]):
        """
        Inputs:
          workdir         Directory with the SOLPS outputs
          gfile_loc       location of corresponding g file
          impurity_list   List of all the impurity species included in the plasma simulation
        """

        # Try parsing gfile name
        workdir_short = None
        shot = None
        try:
            shot_loc_in_gfile_string = gfile_loc.rfind('g')
            shot = int(gfile_loc[shot_loc_in_gfile_string+1 : shot_loc_in_gfile_string+7])

            shot_ind_in_workdir = workdir.rfind(str(shot))
            if shot_ind_in_workdir > 0:
                workdir_short = workdir[shot_ind_in_workdir:]
        except:
            pass

        self.data = {'workdir':workdir, 'workdir_short':workdir_short, 'gfile_loc': gfile_loc,
                     'expData':{'fitProfs':{}}, 'solpsData':{'profiles':{}},
                     'impurities':[imp.lower() for imp in impurity_list], 'shot':shot}

    # ----------------------------------------------------------------------------------------
    
    def readMastData(self, mastfile_loc):
        self.timeid = mastfile_loc[mastfile_loc.rfind('_')+1:mastfile_loc.rfind('.')]

        mastfile_dict = sut.read_mastfile(mastfile_loc)
        self.data['expData']['fitPsiProf'] = mastfile_dict['psi_normal']
        self.data['expData']['fitProfs']['neprof'] = mastfile_dict['electron_density(10^20/m^3)']
        self.data['expData']['fitProfs']['teprof'] = mastfile_dict['electron_temperature(KeV)']

        try:
            self.data['expData']['fitProfs']['tipsi'] = mastfile_dict['psi_normal']
            self.data['expData']['fitProfs']['tiprof'] = mastfile_dict['ion_temperature(KeV)']
        except:
            print('No Ti data in pfile, defaulting to Ti = Te')
            self.data['expData']['fitProfs']['tiprof'] = self.data['expData']['fitProfs']['teprof']

    # ----------------------------------------------------------------------------------------    
    
    

    def calcPsiVals(self, plotit = False, dsa = None, b2mn = None, geo = None, verbose=True, shift=0):
        """
        Call b2plot to get the locations of each grid cell in psin space
    
        Saves the values to dictionaries in self.data['solpsData']
    
        Find grid corners first:
          0: lower left
          1: lower right
          2: upper left
          3: upper right
    
        Average location of cells 0 and 2 for middle of 'top' surface, 
        which is the top looking at outboard midplane
        Don't average over whole cell, dR << dZ at outboard midplane 
        and surface has curvature, so psin will be low
    
        jxa = poloidal cell index for the outer midplane
        crx = radial coordinate corner of grid [m]
        cry = vertical coordinate corner of grid [m]
        writ = write b2plot.write file
        f.y = plot against y
        """
    
        wdir = self.data['workdir']
    
        try:
            if dsa is None:
                dsa = sut.read_dsa('dsa')
            if geo is None:
                geo = sut.read_b2fgmtry('../baserun/b2fgmtry')
            if b2mn is None:
                b2mn = sut.scrape_b2mn("b2mn.dat")                
    
            crLowerLeft = geo['crx'][b2mn['jxa']+1,:,0]
            crUpperLeft = geo['crx'][b2mn['jxa']+1,:,2]
            czLowerLeft = geo['cry'][b2mn['jxa']+1,:,0]
            czUpperLeft = geo['cry'][b2mn['jxa']+1,:,2]               
        except:
            if verbose:
                print('  Failed to read geometry files directly, trying b2plot')
            if not self.b2plot_ready:
                sut.set_b2plot_dev(verbose=verbose)
                self.b2plot_ready = True
    
            try:
                dsa, crLowerLeft = sut.B2pl('0 crx writ jxa f.y', wdir = wdir)
            except Exception as err:
                print('Exiting from calcPsiVals')
                raise err
        
            # Only 2 unique psi values per cell, grab 0 and 2
            dummy, crUpperLeft = sut.B2pl('2 crx writ jxa f.y', wdir = wdir)  # all x inds are the same
            dummy, czLowerLeft = sut.B2pl('0 cry writ jxa f.y', wdir = wdir)
            dummy, czUpperLeft = sut.B2pl('2 cry writ jxa f.y', wdir = wdir)
            
        ncells = len(czLowerLeft)
    
        g = sut.loadg(self.data['gfile_loc'])
        d = float(shift)
        psiN = (g['psirz'] - g['simag']) / (g['sibry'] - g['simag'])
    
        dR = g['rdim'] / (g['nw'] - 1)
        dZ = g['zdim'] / (g['nh'] - 1)
    
        gR = []
        for i in range(g['nw']):
            gR.append(g['rleft'] + i * dR + d)
    
        gZ = []
        for i in range(g['nh']):
            gZ.append(g['zmid'] - 0.5 * g['zdim'] + i * dZ)
    
        gR = np.array(gR)
        gZ = np.array(gZ)
    
        R_solps_top = 0.5 * (np.array(crLowerLeft) + np.array(crUpperLeft))
        Z_solps_top = 0.5 * (np.array(czLowerLeft) + np.array(czUpperLeft))
    
        psiNinterp = interpolate.interp2d(gR, gZ, psiN, kind = 'cubic')
    
        psi_solps = np.zeros(ncells)
        for i in range(ncells):
            psi_solps_LL = psiNinterp(crLowerLeft[i], czLowerLeft[i])
            psi_solps_UL = psiNinterp(crUpperLeft[i], czUpperLeft[i])
            psi_solps[i] = np.mean([psi_solps_LL,psi_solps_UL])
    
        self.data['solpsData']['crLowerLeft'] = np.array(crLowerLeft)
        self.data['solpsData']['czLowerLeft'] = np.array(czLowerLeft)
        self.data['solpsData']['dsa'] = np.array(dsa)
        self.data['solpsData']['psiSOLPS'] = np.array(psi_solps)