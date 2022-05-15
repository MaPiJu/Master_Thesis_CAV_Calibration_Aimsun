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
	
	file = open(cwd+"\\"+ "Initial_parameters_"+str(name_veh)+"_calibration"+".txt","w")
	
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

def write_dico_txt_params_vehicles(Veh_ID):
	veh = model.getCatalog().find( Veh_ID )
	name_veh = veh.getName()
	gkRea=veh.getVariableReactionTimes()
	
	file = open(cwd+"\\"+ "WU_Dico_Best_parameters_"+str(name_veh)+"_calibration"+".txt","w")
	
	# maxSpeed Mean
	file.write("maxSpeed"+","+str(veh.getDataValueByID(GKVehicle.maxSpeedMean)[0]))
	file.write("\n")

	# maxAccel Mean
	file.write("maxAccel"+","+str(veh.getDataValueByID(GKVehicle.maxAccelMean)[0]))
	file.write("\n")

	# normalDecel Mean
	file.write("normalDecel"+","+str(veh.getDataValueByID(GKVehicle.normalDecelMean)[0]))
	file.write("\n")
	
	# maxDecel Mean
	file.write("maxDecel"+","+str(veh.getDataValueByID(GKVehicle.maxDecelMean)[0]))
	file.write("\n")
	
	# speedAcceptance Mean
	file.write("speedAcceptance"+","+str(veh.getDataValueByID(GKVehicle.speedAcceptanceMean)[0]))
	file.write("\n")

	# minDist Mean
	file.write("minDist"+","+str(veh.getDataValueByID(GKVehicle.minDistMean)[0]))
	file.write("\n")
	

	# Reaction time parameters 
	for elt in gkRea:
         file.write("reactionTime"+","+str(round(elt.reactionTime,1)))

	file.close()



#############
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

	f.close()

	return(arrayData)

def readAndSortData():

	arrayData = [[9999,9999,9999,9999,9999,9999]]

	with open("AllAggregatedData_Calibration.csv", "r") as f:
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

def dictionaries_to_array(dictCAV):

	data2 = np.array(list(dictCAV.values()))

	return data2

##############

def array_to_dictionaries(array_in,dictCAV):

	newDictC = {}
	
	
	dataC = array_in

	i=0
	
	for key in dictCAV.keys():

		newDictC[key] = dataC[i]
		i+=1

	return newDictC
	

	

#######################

def Normalize_dict_values(dict_of_ranges,dictVeh,Reverse):

	newDictV = {}

	if Reverse == False:

		for key in dict_of_ranges.keys():

			val_to_normalize_V = dictVeh[key]

			newDictV[key] = round((val_to_normalize_V - dict_of_ranges[key][0])/(dict_of_ranges[key][1] - dict_of_ranges[key][0]),2)

	else:

		for key in dict_of_ranges:

			val_to_Denormalize_V= dictVeh[key]

			newDictV[key] = float(round(val_to_Denormalize_V * (dict_of_ranges[key][1] - dict_of_ranges[key][0])+dict_of_ranges[key][0],2))

	return newDictV

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


def calculate_RMNSE(synthetic_Data, calibration_Data):
	file_name_SYN = str(synthetic_Data)+".csv"
	file_name_CAL = str(calibration_Data)+".csv"

	dat_syn = np.genfromtxt(file_name_SYN, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))
	dat_cal = np.genfromtxt(file_name_CAL, delimiter = ",",dtype=float, skip_header=1, usecols=(3,4))

	N = len(dat_syn)

	array_temp = np.square((dat_cal-dat_syn)/dat_syn)

	RMNSE = list(np.sqrt((1/N) * np.sum(array_temp,axis=0)))

	return RMNSE
 


def runMultipleReplications(ListOfReplications,Dict_Veh_Cal,Dict_Veh_No_Cal,ID_Veh):

	if ID_Veh == 154:
		ID_Data = 0
		Name_Veh = "HDV"
		dico_CF_HDV = Dict_Veh_Cal
		dico_CF_CAV = Dict_Veh_No_Cal
	
	elif ID_Veh == 37968:
		ID_Data = 1
		Name_Veh = "CAV"
		dico_CF_CAV = Dict_Veh_Cal
		dico_CF_HDV = Dict_Veh_No_Cal
		

	removeFiles("AllAggregatedData_Calibration")
	removeFiles("AllAggregatedDataNoDistinction_Calibration")

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

	Veh_array_Data = readAndSortData()[ID_Data]
	array_Data_No_Distinction = readData()

	Calibration_Data_Veh = averageAggData(Veh_array_Data,nb_replication)
	synthetic_Data_No_Distinction = averageAggData(array_Data_No_Distinction,nb_replication)


	# We save the CF and LC parameters used during the simulation

	write_params_vehicles(ID_Veh)

	# We write the measurements of the detectors

	writeCSVfileAllData(Calibration_Data_Veh,"Calibration_Data_" + str(Name_Veh))
	writeCSVfileAllData(synthetic_Data_No_Distinction,"Calibration_Data_No_Distinction")


	# We calculate the RMNSE for the two sort of Vehicles
	#print("\n RMNSE for All Vehicles (First=Count, Second=Speed):")
	l_RMNSE = calculate_RMNSE("Synthetic_Data_"+str(Name_Veh)+"_err","Calibration_Data_"+ str(Name_Veh))
	l_RMNSE_No_distinc = calculate_RMNSE("Synthetic_Data_No_Distinction_err","Calibration_Data_No_Distinction")
	err_ct_all = l_RMNSE_No_distinc[0]
	err_sp_all = l_RMNSE_No_distinc[1]

	l_RMNSE.append(err_ct_all)
	l_RMNSE.append(err_sp_all)	

	return l_RMNSE


############


##############



def SPSA(SPSA_para,ListOfReplications,Dict_Veh_Cal,Dict_Veh_No_Cal,ID_Veh):

	if ID_Veh == 154:
		ID_Data = 0
		Name_Veh = "HDV"

	elif ID_Veh == 37968:
		ID_Data = 1
		Name_Veh = "CAV"


	removeFiles("List_of_Errors")
	removeFiles("Calibration_Data_No_Distinction_Step_0_" + str(Name_Veh))
	removeFiles("Calibration_Data_No_Distinction_Best_Step_" + str(Name_Veh))

	N = SPSA_para["N"] # Number of iterations we do in total for the optimization
	c = SPSA_para["c"]
	A = 2.5
	alpha = SPSA_para["alpha"]
	gamma = SPSA_para["gamma"]
	G = SPSA_para["G"] # Number of time we do the iteration to calculate g
	t = SPSA_para["t"] # Parameter to calculate ak at k = 0

	print("Dict to calibrate")
	print(Dict_Veh_Cal)
	print("Dict not to calibrate")
	print(Dict_Veh_No_Cal)


	replicationsList = findReplications(CurrentExperiment)

	# Defining the two dictionaries of CF paramaters
	dict_Veh_Para_Plus = Dict_Veh_Cal

	dict_Veh_Para_Minus = Dict_Veh_Cal

	l_ak = []
	l_ck = []
	l_SA_HDV = []
	l_SA_CAV = []
	l_errors_speed_Veh = []
	l_errors_speed_All = []
	l_errors_counting_Veh = []
	l_errors_counting_All = []

	# Create the dictionnay of ranges
	dict_of_ranges = from_txt_to_dict("Parameters_ranges")

	# Run the multiple replications

	print("Start of simulation 0:")
	y = runMultipleReplications(replicationsList,Dict_Veh_Cal,Dict_Veh_No_Cal,ID_Veh)
	print("Starting RMNSE count and speed errors= ",y)

	# Save the data at step 0 for evaluating the evolution
	array_Data_No_Distinction = readAndSortData()[ID_Data]
	synthetic_Data_No_Distinction = averageAggData(array_Data_No_Distinction,nb_replication)
	writeCSVfileAllData(synthetic_Data_No_Distinction,"Calibration_Data_No_Distinction_Step_0_only_"+ str(Name_Veh))

	# Save the data at step 0 for evaluating the evolution
	array_Data_No_Distinction = readData()
	synthetic_Data_No_Distinction = averageAggData(array_Data_No_Distinction,nb_replication)
	writeCSVfileAllData(synthetic_Data_No_Distinction,"Calibration_Data_No_Distinction_Step_0_all_Veh_with_"+ str(Name_Veh))

	l_errors_speed_Veh.append(y[1])
	l_errors_counting_Veh.append(y[0])
	l_errors_speed_All.append(y[3])
	l_errors_counting_All.append(y[2])
	print("###########################")

	Best_RMNSE = 100

	best_dict_Veh_Para = {}



	
	iteration = 0


	while iteration < N:

		print("Current iteration number: ",iteration)

		# Normalization of the initial CF parameters
		dictionaries = Normalize_dict_values(dict_of_ranges,Dict_Veh_Cal,False)
		Dict_Veh_Cal = dictionaries

		ck = c / ((iteration+1) ** gamma)

		l_ck.append(ck)


		# Create the vector of CF parameters or the Delta_k
		CF_param_normalized = dictionaries_to_array(Dict_Veh_Cal)

		g_prime_it = pd.DataFrame()
		g_it = 1

		# Start of the calculation of several g'
		while g_it <= G:

			# Generation of a new random vector
			delta = 2*np.random.binomial(n=1,p=0.5,size=7)-1
			
			# Plus perturbation of CF parameters
			CF_param_plus = CF_param_normalized + ck * delta
			print("CF_param_plus")
			print(CF_param_plus)
				
			# Minus perturbation of CF parameters
			CF_param_minus = CF_param_normalized - ck * delta
			print("CF_param_minus")
			print(CF_param_minus)
			
			# Checking if new values are between the bounds
			CF_param_plus_checked = Checking_bounds(CF_param_plus)
			CF_param_minus_checked = Checking_bounds(CF_param_minus)
			print("CF_param_plus_checked")
			print(CF_param_plus_checked)

			print("CF_param_minus_checked")
			print(CF_param_minus_checked)
				
			# Creating dictionaries of the CF parameters
			dictionaries_para_plus = array_to_dictionaries(CF_param_plus_checked,dict_Veh_Para_Plus)
			dictionaries_para_minus = array_to_dictionaries(CF_param_minus_checked,dict_Veh_Para_Minus)



			dict_Veh_Para_Plus = dictionaries_para_plus
			print("dict_"+ str(Name_Veh)+"_Para_Plus")
			print(dict_Veh_Para_Plus)

			dict_Veh_Para_Minus = dictionaries_para_minus
			print("dict_"+ str(Name_Veh)+"_Para_Minus")
			print(dict_Veh_Para_Minus)
	

			# De-Normalization of the CF parameters
			dictionaries_DeNorm_plus = Normalize_dict_values(dict_of_ranges,dict_Veh_Para_Plus,True)
			dictionaries_DeNorm_minus = Normalize_dict_values(dict_of_ranges,dict_Veh_Para_Minus,True)


			dict_Veh_Para_Plus = dictionaries_DeNorm_plus

			dict_Veh_Para_Minus = dictionaries_DeNorm_minus

			print("dict_"+ str(Name_Veh)+"_Para_Plus")
			print(dict_Veh_Para_Plus)

			print("dict_"+ str(Name_Veh)+"_Para_Minus")
			print(dict_Veh_Para_Minus)

			# Calculation of y+ and y-
			print("Simulation of y_plus of g_it = %d / %d. For iteration k = %d / %d" %(g_it,G, iteration,N))

			y_plus = runMultipleReplications(replicationsList,dict_Veh_Para_Plus,Dict_Veh_No_Cal,ID_Veh)[1]
			print("y_plus")
			print(y_plus)



			print("Simulation of y_minus of g_it = %d / %d. For iteration k = %d / %d" %(g_it,G, iteration,N))

			y_minus = runMultipleReplications(replicationsList,dict_Veh_Para_Minus,Dict_Veh_No_Cal,ID_Veh)[1]
			print("y_minus")
			print(y_minus)


			print("y_plus - y_minus =")
			print(y_plus - y_minus)

			print("ck")
			print(ck)
			

			# Calculation of g_prime for this sub-iteration
			print("Calcul de g_prime temp:")
			
			g_prime_temp = pd.DataFrame( ( (y_plus - y_minus)/(2 * ck) )  *  delta   )
			print(g_prime_temp)

			# Concatenation of g_prime_it
			print("Liste des g prime calculés:")
		
			g_prime_it = pd.concat([g_prime_it, g_prime_temp], axis=1)
			print(g_prime_it)

			#Incrementation of g_it
			g_it += 1

		# Averaging of g_prime over the Gth iteration
		print("print de g moyenné:")

		g_prime_avg = g_prime_it.mean(axis = 1)
		print(g_prime_avg)

		if iteration == 0:
	
			# We keep the absolute values of g_prime_avg
			g_prime_avg_abs = g_prime_avg.abs()
			print("g_prime_avg")
			print(g_prime_avg)

			# We can obtain the average value of "g" that will pertub the Normalized CF parameters
			g_ak0 = float(g_prime_avg_abs.mean(axis = 0))
			print("g_ak0")
			print(g_ak0)

			a = float( round( ((t * (A+1)**alpha)/g_ak0),2 ) )
			print("a")
			print(a)
			

		# We update Delta_k or the vector of CF parameters of HDV and CAV
		ak = a/((iteration+1+A) ** alpha)
		print("ak")
		print(ak)
		l_ak.append(ak)
		
		# Minimization
		CF_param_normalized = CF_param_normalized - ak * g_prime_avg


		# We check if the new CF parameters respects the bounds
		print("CF_param_normalized")
		print(CF_param_normalized)

		CF_param_normalized_checked_and_updated = Checking_bounds(CF_param_normalized)

		print("CF_param_normalized_checked_and_updated")
		print(CF_param_normalized_checked_and_updated)

		# We update the CF parameters for the two kind of vehicles

		updated_dictonnaries = array_to_dictionaries(CF_param_normalized_checked_and_updated,Dict_Veh_Cal)

		Dict_Veh_Cal_updated = updated_dictonnaries

		#De-Normalization
		dictionaries_DeNorm_final = Normalize_dict_values(dict_of_ranges,Dict_Veh_Cal_updated,True)

		Dict_Veh_Cal = dictionaries_DeNorm_final

		print("dict_"+str(Name_Veh))
		print(Dict_Veh_Cal)
	
		#add the SA of the two vehicles
		#l_SA_HDV.append(dict_HDV.get("speedAcceptance"))
		#l_SA_CAV.append(dict_CAV.get("speedAcceptance"))

		# Calculation of the error for the current iteration
		y = runMultipleReplications(replicationsList,Dict_Veh_Cal,Dict_Veh_No_Cal,ID_Veh)
		l_errors_speed_Veh.append(y[1])
		l_errors_counting_Veh.append(y[0])
		l_errors_speed_All.append(y[3])
		l_errors_counting_All.append(y[2])
		print("Error for iteration= ",iteration)
		print("errrors counting and speed")
		print(y)

		print("List of speed errors of the current vehicles")
		print(l_errors_speed_Veh)
		print("List of speed errors of all vehicles")
		print(l_errors_speed_All)

		if y[1] < Best_RMNSE:
				Best_RMNSE = y[1]
				best_dict_Veh_Para = Dict_Veh_Cal
				write_dico_txt_params_vehicles(ID_Veh)
				array_Data_No_Distinction = readAndSortData()[ID_Data]
				synthetic_Data_No_Distinction = averageAggData(array_Data_No_Distinction,nb_replication)
				writeCSVfileAllData(synthetic_Data_No_Distinction,"Calibration_Data_No_Distinction_Best_Step_only_"+str(Name_Veh))
				
				# Save the data at step 0 for evaluating the evolution
				array_Data_No_Distinction = readData()
				synthetic_Data_No_Distinction = averageAggData(array_Data_No_Distinction,nb_replication)
				writeCSVfileAllData(synthetic_Data_No_Distinction,"Calibration_Data_No_Distinction_Best_Step_all_veh_with_"+ str(Name_Veh))

		# Incrementation updating

		iteration +=1
	
	iteration_final = iteration-1
	print("Iteration Number: %d / %d done"% (iteration_final,N))
	
	print("Best RMNSE =", Best_RMNSE)

	#title_ak = "WU_CAV_List_of_ak_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)
	#title_ck = "WU_CAV_List_of_ck_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)
	#title_SA_HDV = "WU_CAV_List_of_SA_HDV_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)
	#title_SA_CAV = "WU_CAV_List_of_SA_CAV_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)
	

	#writeCSV_1D_list(l_ak,title_ak)
	#writeCSV_1D_list(l_ck,title_ck)
	#writeCSV_1D_list(l_SA_HDV,title_SA_HDV)
	#writeCSV_1D_list(l_SA_CAV,title_SA_CAV)


	print("List of speed errors"+ str(Name_Veh)+":")
	print(l_errors_speed_Veh)

	print("List of speed errors all vehicles:")
	print(l_errors_speed_All)

	print("Dictionnary of HDV:")
	print(Dict_Veh_No_Cal)

	print("Dictionnary of CAV:")
	print(best_dict_Veh_Para)

	print("List of counting errors"+ str(Name_Veh)+":")
	print(l_errors_counting_Veh)

	print("List of counting errors all vehicles:")
	print(l_errors_counting_All)

	title_speed_veh = "WU_"+ str(Name_Veh)+"_List_of_Speed_Errors_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)
	title_counting_veh = "WU_"+ str(Name_Veh)+"_List_of_Counting_Errors_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)

	title_speed_all = "WU_All_Veh_"+ str(Name_Veh)+"_List_of_Speed_Errors_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)
	title_counting_all = "WU_All_Veh_"+ str(Name_Veh)+"_List_of_Counting_Errors_c_equals_" + str(c) + "_Number_iters_equals_"+str(N)

	writeCSV_1D_list(l_errors_speed_Veh,title_speed_veh)
	writeCSV_1D_list(l_errors_counting_Veh,title_counting_veh)
	writeCSV_1D_list(l_errors_speed_All,title_speed_all)
	writeCSV_1D_list(l_errors_counting_All,title_counting_all)


	return Best_RMNSE, l_errors_speed_Veh, Dict_Veh_No_Cal, best_dict_Veh_Para,l_errors_counting_Veh

	

# Initialization of the parameters for the SPSA algorithm
SPSA_para = dict(G = 1, Min_error = 0.05, c = 0.1, alpha = 0.602, gamma = 0.101, h = 0.7, N =10,t=0.1)

# Get the objects "replication"
replicationsList = findReplications(CurrentExperiment)
nb_replication = len(replicationsList)-1


# Change the parameters
dico_paras_initialization_HDV = from_txt_to_dict("Parameters_Initialization_Calibration_HDV")
dico_paras_initialization_CAV = from_txt_to_dict("Parameters_Initialization_Calibration_CAV")

 # Initialization of dictionaries for HDV and CAV parameters
dict_init_HDV = dico_paras_initialization_HDV
dict_init_CAV = dico_paras_initialization_CAV


# Run the SPSA algorithm
ID_CAV =37968
ID_HDV = 154

# We start with calibrating CAV (Important the first dict is the one to be calibrated !!)
Cal_1 = SPSA(SPSA_para,replicationsList,dict_init_CAV,dict_init_HDV,ID_CAV)


dico_paras_calibrated_CAV =  from_txt_to_dict("WU_Dico_Best_parameters_CAV Cautious_calibration")

Cal_2 = SPSA(SPSA_para,replicationsList,dict_init_HDV,dico_paras_calibrated_CAV,ID_HDV)
