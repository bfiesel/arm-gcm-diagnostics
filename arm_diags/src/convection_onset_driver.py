import cdms2, MV2
import cdtime
import numpy as np
import numpy.ma as ma
import glob
import matplotlib.pyplot as plt
import os
import scipy.io
# Convective onset metrics generated by the Neelin group, UCLA
# Original code: Kathleen Schiro, python version 22 Dec 2016, references privided in detail from convective_onset_statistics_ARM_Diagnostics.py 
from convection_onset_statistics import convection_onset_statistics

def convection_onset(parameter):
    """Calculate """
    variables = parameter.variables
    #seasons = parameter.season
    test_path = parameter.test_data_path
    obs_path = parameter.obs_path
    cmip_path = parameter.cmip_path
    output_path = parameter.output_path
    sites = parameter.sites
   
    test_model = parameter.test_data_set 
    #ref_models = parameter.ref_models
    
    #Read in observation data
    for index, site in enumerate(sites):
        for va in variables:
            filename = glob.glob(os.path.join(obs_path,'ARMdiag_'+va+'_1hr_*_'+site))
            with open(filename[0]) as f:
                content = f.readlines()
            content = [float(x.strip()) for x in content]
            pr = np.squeeze(content)
            #pr = pr[~np.isnan(pr)]
            if va == 'pr':
                precip = pr
            if va == 'prw':
                prw = pr
           
        convection_onset_statistics(prw, precip,'ARM',output_path, sites)
    
    pr_prw_mod = []
    for va in variables:
        filename = glob.glob(os.path.join(test_path, '*'+va+'_cfSites_'+test_model+'*'+site+'.nc'))[0]
        f_in=cdms2.open(filename)
        pr=f_in(va)#,time=('1979-01-01','1979-12-31')) #Read in the variable 
        if va == 'pr':
            pr = pr *3600.           #'kg m-2 s-1' to 'mm/hr'
        pr_prw_mod.append(pr)
    convection_onset_statistics(pr_prw_mod[1], pr_prw_mod[0],test_model,output_path, sites)
 
           
            

#    #Read in model data
#    
#    #models = ['CNRM-CM5']
#    ##models = ['CNRM-CM5','CanAM4','bcc-csm1-1']
#    #vas = ['pr','prw']
#    #basedir='/Users/zhang40/Documents/cfSite/' #Kathleen, you will only need to change this..
#    #output_path = parameter.output_path
#    #sites = parameter.sites
#
#    #for imod in range(len(models)):
#    #    #Read in Precipitation 
#    #    filename = glob.glob(os.path.join(basedir+'*'+vas[0]+'_cfSites_'+models[imod]+'*'))[0]
#    #    f_in=cdms2.open(filename)
#    #    pr=f_in(vas[0],time=('1979-01-01','1979-12-31')) #Read in the variable 
#
#    #    #Read in CWV
#    #    filename = glob.glob(os.path.join(basedir+'*'+vas[1]+'_cfSites_'+models[imod]+'*'))[0]
#    #    f_in=cdms2.open(filename)
#    #    prw=f_in(vas[1],time=('1979-01-01','1979-12-31')) 
#
#    #    #Nauru ARM site 31
#    #    pr_site=pr[:,30]*3600.           #'kg m-2 s-1' to 'mm/hr'
#    #    prw_site=prw[:,30]               #'kg m-2' to 'mm'
#
#        #Call calculation and plotting function 
#        convection_onset_statistics(prw_site, pr_site,models[imod], output_path, sites)
#    ##
#
#    #Read in Obs data
#    file_path = '/Users/zhang40/Documents/ARM_LLNL/ConvectionMetrics_UCLA/shared_ARM_diagnostics/Nauru_data/'
#    precip_filename = 'precip_nauru_1hravg_matchedtosondes_Apr2001_Aug2006.mat'
#    cwv_filename = 'cwv_nauru_sondes_Apr2001_Aug2006.mat'
#
#    precip_file1 = scipy.io.loadmat(file_path + precip_filename)
#    cwv_file1 = scipy.io.loadmat(file_path + cwv_filename)
#    #precip_file1 = scipy.io.loadmat(precip_filename)
#    #cwv_file1 = scipy.io.loadmat(cwv_filename)
#
#    cwv = cwv_file1['cwv_nauru_sondes_Apr2001_Aug2006']
#    precip = precip_file1['precip_nauru_1hravg_matchedtosondes_Apr2001_Aug2006']
#    cwv = np.squeeze(cwv)
#    precip = np.squeeze(precip)
#    convection_onset_statistics(cwv, precip,'sondes',output_path, sites)
