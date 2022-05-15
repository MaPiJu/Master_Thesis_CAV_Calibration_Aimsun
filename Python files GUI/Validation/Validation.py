# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:26:59 2022

@author: Marc
"""

import os
import csv
import random
from operator import itemgetter

SITEPACKAGES = "c:\\users\\marc\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"
sys.path.append(SITEPACKAGES)
import numpy as np
import pandas as pd

cwd = os.getcwd()


# Find a way to get Id of the Experiment automaticaly
CurrentExperiment = model.getActiveExperiment()

def from_txt_to_dict(Name):
	file = open(cwd+"\\"+ str(Name)+".txt","r") 
	lines = file.readlines()
	dict_params_ranges = {}

	for line in lines:
		currentline = line.split(",")

		if len(currentline)==3:
			dict_params_ranges[currentline[0]] = [float(currentline[1]),float(currentline[2])]

		elif len(currentline)==2:
			dict_params_ranges[currentline[0]] = float(currentline[1])

	file.close()

	return dict_params_ranges

def select_random_value_param(bound):
	param_value = round(random.uniform(bound[0], bound[1]),1)

	return param_value

def change_params_HDV(Veh_ID,dico):
	veh = model.getCatalog().find( Veh_ID )
	
	for key in dico.keys():
		new_value = dico[key]
		if key == "maxAccel":
		
			veh.setDataValueByID( GKVehicle.maxAccelMean, QVariant( new_value ))
			
	
		elif key == "maxDecel":
		
			veh.setDataValueByID( GKVehicle.maxDecelMean, QVariant( new_value ))
			
	
		elif key == "maxSpeed":

			veh.setDataValueByID( GKVehicle.maxSpeedMean, QVariant(new_value ))
			

		elif key == "minDist":

			veh.setDataValueByID( GKVehicle.minDistMean, QVariant( new_value))
			

		elif key == "normalDecel":

			veh.setDataValueByID( GKVehicle.normalDecelMean, QVariant(new_value ))
			

		elif key == "speedAcceptance":

			veh.setDataValueByID( GKVehicle.speedAcceptanceMean, QVariant(new_value))
			

		elif key == "reactionTime":

			car_react = GKVehicleReactionTimes(new_value, new_value, new_value, 1)

			veh.setVariableReactionTimes([car_react])



# We make another function for CAV


def change_params_CAV(Veh_ID,dico):
	veh = model.getCatalog().find( Veh_ID )
	
	for key in dico.keys():
		new_val = dico[key]
		
		if key == "maxAccel":

		
			veh.setDataValueByID( GKVehicle.maxAccelMean, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.maxAccelMin, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.maxAccelMax, QVariant( new_val ))
	
		elif key == "maxDecel":
		
			veh.setDataValueByID( GKVehicle.maxDecelMean, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.maxDecelMin, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.maxDecelMax, QVariant( new_val ))
	
		elif key == "maxSpeed":

			veh.setDataValueByID( GKVehicle.maxSpeedMean, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.maxSpeedMin, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.maxSpeedMax, QVariant( new_val ))


		elif key == "minDist":

			veh.setDataValueByID( GKVehicle.minDistMean, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.minDistMin, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.minDistMax, QVariant( new_val ))

		elif key == "normalDecel":

			veh.setDataValueByID( GKVehicle.normalDecelMean, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.normalDecelMin, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.normalDecelMax, QVariant( new_val ))


		elif key == "speedAcceptance":

			veh.setDataValueByID( GKVehicle.speedAcceptanceMean, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.speedAcceptanceMin, QVariant( new_val ))
			veh.setDataValueByID( GKVehicle.speedAcceptanceMax, QVariant( new_val ))

		elif key == "reactionTime":

			car_react = GKVehicleReactionTimes(new_val, new_val, new_val, 1)

			veh.setVariableReactionTimes([car_react])



def write_params_vehicles(Veh_ID):
	veh = model.getCatalog().find( Veh_ID )
	name_veh = veh.getName()
	gkRea=veh.getVariableReactionTimes()
	
	file = open(cwd+"\\"+ "WU_Best_parameters_"+str(name_veh)+"_validation"+".txt","w")
	
	# maxSpeed Mean Dev Min Max
	file.write("maxSpeed"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.maxSpeedMean)[0])+","+str(veh.getDataValueByID(GKVehicle.maxSpeedDev)[0])+","+str(veh.getDataValueByID(GKVehicle.maxSpeedMin)[0])+","+str(veh.getDataValueByID(GKVehicle.maxSpeedMax)[0]))
	file.write("\n")

	# maxAccel Mean Dev Min Max
	file.write("maxAccel"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.maxAccelMean)[0])+","+str(veh.getDataValueByID(GKVehicle.maxAccelDev)[0])+","+str(veh.getDataValueByID(GKVehicle.maxAccelMin)[0])+","+str(veh.getDataValueByID(GKVehicle.maxAccelMax)[0]))
	file.write("\n")

	# normalDecel Mean Dev Min Max
	file.write("normalDecel"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.normalDecelMean)[0])+","+str(veh.getDataValueByID(GKVehicle.normalDecelDev)[0])+","+str(veh.getDataValueByID(GKVehicle.normalDecelMin)[0])+","+str(veh.getDataValueByID(GKVehicle.normalDecelMax)[0]))
	file.write("\n")
	
	# maxDecel Mean Dev Min Max
	file.write("maxDecel"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.maxDecelMean)[0])+","+str(veh.getDataValueByID(GKVehicle.maxDecelDev)[0])+","+str(veh.getDataValueByID(GKVehicle.maxDecelMin)[0])+","+str(veh.getDataValueByID(GKVehicle.maxDecelMax)[0]))
	file.write("\n")
	
	# speedAcceptance Mean Dev Min Max
	file.write("speedAcceptance"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.speedAcceptanceMean)[0])+","+str(veh.getDataValueByID(GKVehicle.speedAcceptanceDev)[0])+","+str(veh.getDataValueByID(GKVehicle.speedAcceptanceMin)[0])+","+str(veh.getDataValueByID(GKVehicle.speedAcceptanceMax)[0]))
	file.write("\n")

	# minDist Mean Dev Min Max
	file.write("minDist"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.minDistMean)[0])+","+str(veh.getDataValueByID(GKVehicle.minDistDev)[0])+","+str(veh.getDataValueByID(GKVehicle.minDistMin)[0])+","+str(veh.getDataValueByID(GKVehicle.minDistMax)[0]))
	file.write("\n")
	
	# overtakeSpeedAtt Overtake Speed Threshold Percentage
	file.write("overtakeSpeedAtt"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.overtakeSpeedAtt)[0]))
	file.write("\n")

	# laneRecoverySpeedAtt Lane Recovery Speed Threshold Percentage
	file.write("laneRecoverySpeedAtt"+"_"+name_veh+","+str(veh.getDataValueByID(GKVehicle.laneRecoverySpeedAtt)[0]))
	file.write("\n")

	# Reaction time parameters 
	for elt in gkRea:
         file.write("reactionTime"+"_"+name_veh+","+str(round(elt.reactionTime,1)))
         file.write("\n")
         file.write("reactionTimeAtStop"+"_"+name_veh+","+str(round(elt.reactionTimeAtStop,1)))
         file.write("\n")
         file.write("reactionTimeAtTrafficLight"+"_"+name_veh+","+str(round(elt.reactionTimeAtTrafficLight,1)))
         file.write("\n")
         file.write("probability"+"_"+name_veh+","+str(round(elt.probability,1)))
         file.write("\n")
	file.close()


#############

def readData():
	arrayData = [[9999,9999,9999,9999,9999,9999]]
	with open("AllAggregatedDataNoDistinction_Validation.csv", "r") as f:
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

	f.close()

	return(arrayData)

def readAndSortData():

	arrayData = [[9999,9999,9999,9999,9999,9999]]

	with open("AllAggregatedData_Validation.csv", "r") as f:
		reader = csv.reader(f, delimiter="\t")

		print(reader)

		for row in list(reader)[1:]:

			l = ', '.join(row)

			newRow = [x.strip() for x in l.split(',')]

			integer_map = map(float, newRow[:-1])

			newRow = list(integer_map)

			arrayData = np.append(arrayData, [newRow], axis = 0)

	arrayData = arrayData[1:]

    # We sort the data

	array_sorted = sorted(arrayData,key=itemgetter(2,1,3))
    
    # We calculate the average of aggregated data for the 5 replications
    
    # First we split the data into two lists, the first half is for human vehicles
    # The second half is for CAVs


	array_Data_HDV = array_sorted[:int(len(array_sorted)/2)]
	array_Data_CAV = array_sorted[int(len(array_sorted)/2):]

	f.close()

	return array_Data_HDV,array_Data_CAV


def averageAggData(array_Data_Vehicle,Number_of_Replications):
    
    array_result=[["ID_Detector","ID_Vehicle","Time","Average_Count","Average_Speed"]]

    for i in range(int(len(array_Data_Vehicle)/Number_of_Replications)):
        
        
        sub_array = array_Data_Vehicle[Number_of_Replications*i:(Number_of_Replications*i+Number_of_Replications)]
        first_row = list(sub_array[0])
        new_row = first_row[1:4]
        temp_speed_list = []
        temp_count_list = []
        
        for elt in sub_array:
            temp_speed_list.append(elt[-1])
            temp_count_list.append(elt[-2])
        
        avg_speed = sum(temp_speed_list)/len(temp_speed_list)
        avg_count = sum(temp_count_list)/len(temp_count_list)
        
        temp_speed_list = []
        temp_count_list = []
        
        new_row.append(avg_count)
        new_row.append(avg_speed)

        array_result = np.append(array_result, [new_row], axis = 0)
        
    return(array_result)

def writeCSVfileAllData(arrayAggData,Name):
    
    if os.path.exists(cwd+"\\"+ str(Name)+".csv"):
        
        os.remove(cwd+"\\"+ str(Name)+".csv")
        
        file = open(cwd+"\\"+ str(Name)+".csv","w")

        for line in arrayAggData:    
            for data in line:
                file.write(str(data)+",")
            file.write("\n")
        file.close()
    
    else:
        
        file = open(cwd+"\\"+ str(Name)+".csv","w")

        for line in arrayAggData:    
            for data in line:
                file.write(str(data)+",")
            file.write("\n")
        file.close()

#################

def writeCSV_1D_list(arr,Name):
    
    if os.path.exists(cwd+"\\"+ str(Name)+".csv"):
        
        os.remove(cwd+"\\"+ str(Name)+".csv")
        
        file = open(cwd+"\\"+ str(Name)+".csv","w")

        for elt in arr:    
            file.write(str(elt)+",")
        file.write("\n")
        file.close()
    
    else:
        
        file = open(cwd+"\\"+ str(Name)+".csv","w")
   
        for elt in arr:
            file.write(str(elt)+",")
        file.write("\n")
        file.close()


# Function which finds the Replication Id. It is used to communicate later to the API
# About the ID of the Replication currently used
def findReplicationIds(Experiment):
        
    replicationsIdList = []
    
    repObjects = CurrentExperiment.getReplications()
    
    if repObjects != None:
    	for replicationObj in repObjects:
            replicationsIdList.append(replicationObj.getDBId())
    return replicationsIdList 


def findReplications(Experiment):
    
    replicationsList = []
    
    repObjects = Experiment.getReplications()
    
    if repObjects != None:
    	for replicationObj in repObjects:
            replicationsList.append(replicationObj)
    return replicationsList 
        
##############

def removeFiles(Name):
    if os.path.exists(cwd+"\\"+str(Name)+".csv"):
        os.remove(cwd+"\\"+str(Name)+".csv")
    else:
        print("There is no temporary csv file to remove.")
        
    if os.path.exists(cwd+"\\Id.txt"):
        os.remove(cwd+"\\Id.txt")
    else:
        print("There is no temporary txt file to remove.")
        
###########

def dictionaries_to_array(dictHDV,dictCAV):

	data1 = np.array(list(dictHDV.values()))
	data2 = np.array(list(dictCAV.values()))
	data = np.concatenate((data1,data2))

	return data

##############

def array_to_dictionaries(array,dictHDV,dictCAV):

	newDictH = {}
	newDictC = {}
	
	dataH = array[:len(array)//2]
	
	dataC = array[len(array)//2:]

	i=0

	for key in dictHDV.keys():

		newDictH[key] = dataH[i]
		i+=1

	i=0
	
	for key in dictCAV.keys():

		newDictC[key] = dataC[i]
		i+=1

	return newDictH,newDictC
	

	

#######################

def Normalize_dict_values(dict_of_ranges,dictHDV,dictCAV,Reverse):

	newDictH = {}
	newDictC = {}

	if Reverse == False:

		for key in dict_of_ranges.keys():

			val_to_normalize_H = dictHDV[key]
			val_to_normalize_C = dictCAV[key]

			newDictH[key] = round((val_to_normalize_H - dict_of_ranges[key][0])/(dict_of_ranges[key][1] - dict_of_ranges[key][0]),2)
			newDictC[key] = round((val_to_normalize_C - dict_of_ranges[key][0])/(dict_of_ranges[key][1] - dict_of_ranges[key][0]),2)

	else:

		for key in dict_of_ranges:

			val_to_Denormalize_H = dictHDV[key]
			val_to_Denormalize_C = dictCAV[key]

			newDictH[key] = float(round(val_to_Denormalize_H *(dict_of_ranges[key][1] - dict_of_ranges[key][0])+dict_of_ranges[key][0],2))
			newDictC[key] = float(round(val_to_Denormalize_C * (dict_of_ranges[key][1] - dict_of_ranges[key][0])+dict_of_ranges[key][0],2))

	return newDictH,newDictC

###############

def Checking_bounds(CF_param_array):

	i = 0

	CF_bounded = np.zeros( len(CF_param_array) )

	for value in CF_param_array:

		if value > 1:
			CF_bounded[i] = 1

		elif value < 0:
			CF_bounded[i] = 0

		else:
			CF_bounded[i] = value

		i += 1

	return CF_bounded


##################


def calculate_RMNSE(synthetic_Data, validation_Data):
	file_name_SYN = str(synthetic_Data)+".csv"
	file_name_CAL = str(validation_Data)+".csv"

	dat_syn = np.genfromtxt(file_name_SYN, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
	dat_cal = np.genfromtxt(file_name_CAL, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))

	N = len(dat_syn)

	array_temp = np.square((dat_cal-dat_syn)/dat_syn)

	RMNSE = np.sqrt((1/N) * np.sum(array_temp,axis=0))

	return RMNSE

############
def calculate_RMSE(synthetic_Data, validation_Data):
	file_name_SYN = str(synthetic_Data)+".csv"
	file_name_CAL = str(validation_Data)+".csv"

	dat_syn = np.genfromtxt(file_name_SYN, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
	dat_cal = np.genfromtxt(file_name_CAL, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))

	N = len(dat_syn)

	array_temp = np.square((dat_cal-dat_syn)/np.square(dat_syn))

	RMSE =100* np.sqrt((1/N) * np.sum(array_temp,axis=0))

	return RMSE

def calculate_GEH(synthetic_Data, validation_Data):
	file_name_SYN = str(synthetic_Data)+".csv"
	file_name_CAL = str(validation_Data)+".csv"

	dat_syn = np.genfromtxt(file_name_SYN, delimiter = ",",dtype=float, skip_header=1, usecols=(3))
	dat_cal = np.genfromtxt(file_name_CAL, delimiter = ",",dtype=float, skip_header=1, usecols=(3))

	N = len(dat_syn)

	array_temp_1 = 2*np.square(dat_cal-dat_syn)

	array_temp_2 = dat_cal + dat_syn

	GEH = np.sqrt(array_temp_1/array_temp_2)
 
	return GEH
 

def calculate_Theils(synthetic_Data, validation_Data):
	file_name_SYN = str(synthetic_Data)+".csv"
	file_name_CAL = str(validation_Data)+".csv"

	dat_syn = np.genfromtxt(file_name_SYN, delimiter = ",",dtype=float, skip_header=1, usecols=(3))
	dat_cal = np.genfromtxt(file_name_CAL, delimiter = ",",dtype=float, skip_header=1, usecols=(3))

	N = len(dat_syn)

	array_temp_1 = np.square(dat_syn-dat_cal)

	array_temp_2 = np.square(dat_syn)

	array_temp_3 = np.square(dat_cal)

	numerator_one = np.sqrt( (1/N) * np.sum(array_temp_1,axis=0) )

	denominator_one =  np.sqrt( (1/N) * np.sum(array_temp_2,axis=0) ) +  np.sqrt( (1/N) * np.sum(array_temp_3,axis=0) )

	U_one = numerator_one / denominator_one
 
	return U_one



def runMultipleReplications(ListOfReplications,dico_CF_HDV,dico_CF_CAV):

	removeFiles("AllAggregatedData_Validation")
	removeFiles("AllAggregatedDataNoDistinction_Validation")

	nb_replication = len(ListOfReplications)-1
	

     # Change the parameters of HDV
	change_params_HDV(154,dico_CF_HDV)

	# Change the parameters of CAV
	change_params_CAV(37968,dico_CF_CAV)

	for replication in ListOfReplications:

		idCurrentRep = replication.getDBId()

		temp_ID_file = open(cwd+"\\Id.txt","w")
		print(idCurrentRep)

		temp_ID_file.write(str(idCurrentRep))

		temp_ID_file.close()

		GKSystem.getSystem().executeAction( "execute", replication, [], "" )


		print("Replication number %d is done." % idCurrentRep)

	array_Data_No_Distinction = readData()

	synthetic_Data_No_Distinction = averageAggData(array_Data_No_Distinction,nb_replication)


	# We save the CF and LC parameters used during the simulation
	#write_params_vehicles(154)
	#write_params_vehicles(37968)

	# We write the measurements of the detectors

	writeCSVfileAllData(synthetic_Data_No_Distinction,"Validation_Data_No_Distinction")


	# We calculate the RMNSE for the two sort of Vehicles
	#print("\n RMNSE for All Vehicles (First=Count, Second=Speed):")
	l_RMNSE = calculate_RMNSE("Validation_Synthetic_Data_No_Distinction","Validation_Data_No_Distinction")

	return l_RMNSE


############


##############



# Get the objects "replication"
replicationsList = findReplications(CurrentExperiment)
nb_replication = len(replicationsList)-1
print(nb_replication)


# Change the parameters
dico_paras_validation_HDV = from_txt_to_dict("WU_Dico_Best_parameters_HDV_calibration")
dico_paras_validation_CAV = from_txt_to_dict("WU_Dico_Best_parameters_CAV Cautious_calibration")


#Run to find the error with the validation data set

y_val = runMultipleReplications(replicationsList,dico_paras_validation_HDV,dico_paras_validation_CAV)

err_flow = y_val[0]

err_speed = y_val[1]


print("err_flow =")
print(err_flow)

print("err_speed =")
print(err_speed)