# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:23:24 2022

@author: Marc
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:47:00 2022

@author: Marc
"""

import os
import numpy as np
import pandas as pd
import csv
from operator import itemgetter
from math import sqrt
import scipy.stats as stats
# seed the pseudorandom number generator
import random




cwd = os.getcwd()

## Data extraction

file_name_SYN = "Synthetic_Data_No_Distinction_err.csv"
file_name_Step_0 = "Calibration_Data_No_Distinction_Step_0_all_Veh_with_CAV.csv"
file_name_Best_Step = "Calibration_Data_No_Distinction_Best_Step_all_Veh_with_HDV.csv"
file_name_vali_ref = "Validation_Synthetic_Data_No_Distinction_err.csv"
file_name_vali_sim = "Validation_Data_No_Distinction.csv"

dat_ref = np.genfromtxt(file_name_SYN, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
dat_step_0 = np.genfromtxt(file_name_Step_0, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
dat_best_step = np.genfromtxt(file_name_Best_Step, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
dat_vali_ref = np.genfromtxt(file_name_vali_ref, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
dat_vali_sim= np.genfromtxt(file_name_vali_sim, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))


array_count_ref = dat_ref[:,[0]]
array_count_step_0 = dat_step_0[:,[0]]
array_count_best_step = dat_best_step[:,[0]]
array_count_vali_ref = dat_vali_ref[:,[0]]
array_count_vali_sim = dat_vali_sim[:,[0]]

array_speed_ref = dat_ref[:,[1]]
array_speed_step_0 = dat_step_0[:,[1]]
array_speed_best_step = dat_best_step[:,[1]]
array_speed_vali_ref = dat_vali_ref[:,[1]]
array_speed_vali_sim = dat_vali_sim[:,[1]]


## Convert data to hourly intervals

def dat_hourly(data):
    l_dat_hourly = []
    
    for i in range(int(len(data)/6)):

        arr_temp = data[6*i:6*(i+1)]

        
        val_int_temp = np.array(sum(arr_temp))
        
        
        val_int_temp[1] = val_int_temp[1]/6
        
        
        l_dat_hourly.append(val_int_temp)
    
    return np.array(l_dat_hourly)

essai = dat_hourly(dat_ref)

def split_arr_hourl(GEH_array):
    arr_1 = GEH_array[:104]
    arr_2 = GEH_array[104:]
    return arr_1,arr_2

## Calibration analysis

def calculate_GEH(array_ref, array_simul):
    
    
    for i in range(int(len(array_ref))):
        
        array_temp_1 = 2*np.square(array_simul-array_ref)
        array_temp_2 = array_simul + array_ref

        array_GEH = np.sqrt(array_temp_1/array_temp_2)
    
 
    return array_GEH


GEH_step_0 = split_arr_hourl(calculate_GEH(dat_hourly(dat_ref),dat_hourly(dat_step_0)))
GEH_best_step = split_arr_hourl(calculate_GEH(dat_hourly(dat_ref),dat_hourly(dat_best_step)))
GEH_vali = calculate_GEH(dat_hourly(dat_vali_ref),dat_hourly(dat_vali_sim))

GEH_step_0_1st = GEH_step_0[0]
GEH_step_0_2nd = GEH_step_0[1]
GEH_best_step_1st = GEH_best_step[0]
GEH_best_step_2nd = GEH_best_step[1]

def fail_rate_GEH(array):
    l_nb=0
    nb_fail=0
    l_fail_val=[]
    l_fail_line=[]

    for line in array:
        for elt in line:
            if elt>5:
                nb_fail +=1
                l_fail_val.append(elt)
                l_fail_line.append(l_nb)
        l_nb+=1
        
    print("nb fail total:")
    print(nb_fail)
        
    print("Percentage good GEH:")
    print(round(((1-nb_fail/len(array))*100),2))
    
print("GEH step 0 1st hour")
fail_rate_GEH(GEH_step_0_1st)
print("")
print("GEH step 0 2nd hour")
fail_rate_GEH(GEH_step_0_2nd)
print("")
print("GEH best step 1st hour")
fail_rate_GEH(GEH_best_step_1st)
print("")
print("GEH best step 2nd hour")
fail_rate_GEH(GEH_best_step_2nd)
print("")
print("GEH validation")
fail_rate_GEH(GEH_vali)

#### count nub don't reach GEH


##############################################################
# Change the production of synthetic data with adding errors #
##############################################################

def readData():
	arrayData = [[9999,9999,9999,9999,9999,9999]]
	with open("AllAggregatedDataNoDistinction_Calibration.csv", "r") as f:
		reader = csv.reader(f, delimiter="\t")
		print(reader)
		for row in list(reader)[1:]:
			l = ', '.join(row)

			newRow = [x.strip() for x in l.split(',')]

			integer_map = map(float, newRow[:-1])

			newRow = list(integer_map)

			arrayData = np.append(arrayData, [newRow], axis = 0)

		arrayData = list(arrayData[1:])
		arrayData = sorted(arrayData,key=itemgetter(2,1,3))

		return(arrayData)
    
    
#array_Data_Vehicle = readData()
Number_of_Replications = 10


###############################################################################
def rand_err_prod():
    rd = random.random()
    if rd > 0.5:
        err_count = random.uniform(0.001,0.035)
        err_speed = random.uniform(0.012,0.033)
        
    else:
        err_count = -random.uniform(0.001,0.035)
        err_speed = -random.uniform(0.012,0.033)
        
    return err_count,err_speed
    
###############################################################################


    
def calculate_RMNSE(synthetic_Data, calibration_Data):
	file_name_SYN = str(synthetic_Data)+".csv"
	file_name_CAL = str(calibration_Data)+".csv"

	dat_syn = np.genfromtxt(file_name_SYN, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
	dat_cal = np.genfromtxt(file_name_CAL, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))

	N = len(dat_syn)

	array_temp = np.square((dat_cal-dat_syn)/dat_syn)

	RMNSE = np.sqrt((1/N) * np.sum(array_temp,axis=0))

	return RMNSE

###############

def mane(f, y):
    f = f.flatten()
    y = y.flatten()
    df = pd.DataFrame({'f_i':f, 'y_i': y})
    df['e'] = np.abs((df['y_i'] - df['f_i'])/df['f_i'])
    return np.mean(df['e'])


def u1(f,y):
    y = y.flatten()
    f = f.flatten()
    df = pd.DataFrame({'f_i':f, 'y_i': y})
    df['(f_i - y_i)^2'] = np.square(df['f_i'] - df['y_i'])
    df['y_i^2'] = np.square(df['y_i'])
    df['f_i^2'] = np.square(df['f_i'])
    return (np.sqrt(np.mean(df['(f_i - y_i)^2'])))/(np.sqrt(np.mean(df['y_i^2']))+np.sqrt(np.mean(df['f_i^2'])))


def u2(f,y):
    y = y.flatten()
    f = f.flatten()
    df = pd.DataFrame({'f_i+1':f, 'y_i+1': y})
    df['y_i'] = df['y_i+1'].shift(periods=1)
    df['numerator'] = np.square((df['f_i+1'] - df['y_i+1']) / df['y_i'])
    df['denominator'] = np.square((df['y_i+1'] - df['y_i']) / df['y_i'])
    df.dropna(inplace=True)
    return np.sqrt(np.sum(df['numerator'])/np.sum(df['denominator']))


def rrmse(f, y):
    f = f.flatten()
    y = y.flatten()
    df = pd.DataFrame({'f_i':f, 'y_i': y})
    df['e'] = np.square(df['y_i'] - df['f_i'])/np.square(df['y_i'])
    return np.sqrt(np.mean(df['e']))



###########

print("RMNSE step 0")
print(calculate_RMNSE("Synthetic_Data_No_Distinction_err","Calibration_Data_No_Distinction_Step_0_all_Veh_with_CAV"))
print("")
print("RMNSE best step")
print(calculate_RMNSE("Synthetic_Data_No_Distinction_err","Calibration_Data_No_Distinction_Best_Step_all_Veh_with_HDV"))
print("")
print("RMNSE validation step")
print(calculate_RMNSE("Validation_Synthetic_Data_No_Distinction_err","Validation_Data_No_Distinction"))
print("")





print(np.var(array_speed_step_0)/np.var(array_speed_ref))
print(np.var(array_speed_best_step)/np.var(array_speed_step_0))
print(np.var(array_speed_vali_sim)/np.var(array_speed_vali_ref))



print(np.mean(array_speed_ref))
print(np.mean(array_speed_step_0))
print(np.mean(array_speed_best_step))
print(np.mean(array_speed_vali_ref))
print(np.mean(array_speed_vali_sim))

print("")
print("count mean")
print(np.mean(array_count_ref))
print(np.mean(array_count_step_0))
print(np.mean(array_count_best_step))
print(np.mean(array_count_vali_ref))
print(np.mean(array_count_vali_sim))

arr_1 = np.array([5,5,7,3,6,4,8,5])
arr_2 = np.array([-100,99,55,-55,300,-300,10,2])

stat_res_ttest = stats.ttest_ind(arr_1, arr_2)
stat_res_KStest = stats.ks_2samp(arr_1, arr_2)

D_alpha = 1.36 * sqrt((1248*2)/1248**2)
print(D_alpha)
# Speed

stat_res_step_0 = stats.ks_2samp(array_speed_ref.flatten(), array_speed_step_0.flatten())

stat_res_best_step = stats.ks_2samp(array_speed_ref.flatten(), array_speed_best_step.flatten())

stat_res_vali = stats.ks_2samp(array_speed_vali_ref.flatten(),array_speed_vali_sim.flatten())


# Count
stat_count_step_0 = stats.ks_2samp(array_count_ref.flatten(), array_count_step_0.flatten())

stat_count_best_step = stats.ks_2samp(array_count_ref.flatten(), array_count_best_step.flatten())

stat_count_vali = stats.ks_2samp(array_count_vali_ref.flatten(), array_count_vali_sim.flatten())


# U1 speed
U1_step0 = u1(array_speed_step_0,array_speed_ref)
U1_best_step = u1(array_speed_best_step,array_speed_ref)
U1_vali = u1(array_speed_vali_sim,array_speed_vali_ref)

# U2 speed
U2_step0 = u2(array_speed_step_0,array_speed_ref)
U2_best_step = u2(array_speed_best_step,array_speed_ref)
U2_vali = u2(array_speed_vali_sim,array_speed_vali_ref)

# mane speed
MANE_step0 = mane(array_speed_step_0,array_speed_ref)
MANE_best_step = mane(array_speed_best_step,array_speed_ref)
MANE_vali = mane(array_speed_vali_sim,array_speed_vali_ref)

# rmse speed
RMSE_step0 = rrmse(array_speed_step_0,array_speed_ref)
RMSE_best_step = rrmse(array_speed_best_step,array_speed_ref)
RMSE_vali = rrmse(array_speed_vali_sim,array_speed_vali_ref)