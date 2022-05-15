# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:26:59 2022

@author: Marc
"""
import os
import csv
from operator import itemgetter
import random
random.seed(1)

SITEPACKAGES = "c:\\users\\marc\\appdata\\local\\programs\\python\\python37\\lib\\site-packages"
sys.path.append(SITEPACKAGES)
import numpy as np

cwd = os.getcwd()

# Find a way to get Id of the Experiment automaticaly
CurrentExperiment = model.getActiveExperiment()


###################
def write_params_vehicles(Veh_ID):
	veh = model.getCatalog().find( Veh_ID )
	name_veh = veh.getName()
	gkRea=veh.getVariableReactionTimes()
	
	file = open(cwd+"\\"+ "Initial_parameters_"+str(name_veh)+".txt","w")
	
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

def readData():
	arrayData = [[9999,9999,9999,9999,9999,9999]]
	with open("AllAggregatedDataNoDistinction.csv", "r") as f:
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

def readAndSortData():
    
    arrayData = [[9999,9999,9999,9999,9999,9999]]
    
    with open("AllAggregatedData.csv", "r") as f:
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
    
    return array_Data_HDV,array_Data_CAV
#################
def rand_err_prod():
	rd = random.random()
	if rd > 0.5:
		err_count = random.uniform(0.001,0.035)
		err_speed = random.uniform(0.012,0.033)

	else:
		err_count = -random.uniform(0.001,0.035)
		err_speed = -random.uniform(0.012,0.033)

	return err_count,err_speed


#################

def averageAggData(array_Data_Vehicle,Number_of_Replications):

	array_result=[["ID_Detector","ID_Vehicle","Time","Average_Count","Average_Speed"]]
	array_result_err = [["ID_Detector","ID_Vehicle","Time","Average_Count","Average_Speed"]]

	for i in range(int(len(array_Data_Vehicle)/Number_of_Replications)):

		sub_array = array_Data_Vehicle[Number_of_Replications*i:(Number_of_Replications*i+Number_of_Replications)]
		first_row = list(sub_array[0])
		new_row = first_row[1:4]
		new_row_err = first_row[1:4]
		temp_speed_list = []
		temp_count_list = []


		for elt in sub_array:
			temp_speed_list.append(elt[-1])
			temp_count_list.append(elt[-2])

		# Generate random numbers for the error
		err_tuple = rand_err_prod()
    
		#Random percentage error for Counting
		err_multi_count = 1 + err_tuple[0]
    
		#Random percentage error for Speed
		err_multi_speed = 1 + err_tuple[1]


		avg_speed = sum(temp_speed_list)/len(temp_speed_list)
		avg_count = sum(temp_count_list)/len(temp_count_list)

		avg_speed_err = avg_speed * err_multi_speed
		avg_count_err = avg_count * err_multi_count

		temp_speed_list = []
		temp_count_list = []

		new_row.append(avg_count)
		new_row.append(avg_speed)

		new_row_err.append(avg_count_err)
		new_row_err.append(avg_speed_err)

		array_result = np.append(array_result, [new_row], axis = 0)
		array_result_err = np.append(array_result_err, [new_row_err], axis = 0)

	return array_result,array_result_err

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

# Function which finds the Replication Id. It is used to communicate later to the API
# About the ID of the Replication currently used
def findReplicationIds(Experiment):
        
    replicationsIdList = []
    
    repObjects = CurrentExperiment.getReplications()
    
    if repObjects != None:
    	for replicationObj in repObjects:
            replicationsIdList.append(replicationObj.getDBId())
    return(replicationsIdList)


def findReplications(Experiment):
    
    replicationsList = []
    
    repObjects = CurrentExperiment.getReplications()
    
    if repObjects != None:
    	for replicationObj in repObjects:
            replicationsList.append(replicationObj)
    return(replicationsList)

def removeFiles(Name):
    if os.path.exists(cwd+"\\"+str(Name)+".csv"):
        os.remove(cwd+"\\"+str(Name)+".csv")
    else:
        print("There is no temporary csv file to remove.")
        
    if os.path.exists(cwd+"\\Id.txt"):
        os.remove(cwd+"\\Id.txt")
    else:
        print("There is no temporary txt file to remove.")
        
    

def runMultipleReplications(ListOfReplications):

	for replication in ListOfReplications:

		idCurrentRep = replication.getDBId()

		temp_ID_file = open(cwd+"\\Id.txt","w")
		print(idCurrentRep)

		temp_ID_file.write(str(idCurrentRep))

		temp_ID_file.close()

		GKSystem.getSystem().executeAction( "execute", replication, [], "" )

		print("Replication number %d is done." % idCurrentRep)


	array_Data_HDV = readAndSortData()[0]
	array_Data_CAV = readAndSortData()[1]
	array_Data_No_Distinction = readData()

	avg_dat_HDV = averageAggData(array_Data_HDV,nb_replication)
	avg_dat_CAV = averageAggData(array_Data_CAV,nb_replication)
	avg_dat_No_Distinction = averageAggData(array_Data_No_Distinction,nb_replication)
	
	synthetic_Data_HDV = avg_dat_HDV[0]
	synthetic_Data_CAV = avg_dat_CAV[0]
	synthetic_Data_No_Distinction = avg_dat_No_Distinction[0]

	synthetic_Data_HDV_err = avg_dat_HDV[1]
	synthetic_Data_CAV_err = avg_dat_CAV[1]
	synthetic_Data_No_Distinction_err = avg_dat_No_Distinction[1]

	# We save the CF and LC parameters used during the simulation
	write_params_vehicles(154)
	write_params_vehicles(37968)

	# We write the measurements of the detectors
	writeCSVfileAllData(synthetic_Data_HDV,"Synthetic_Data_HDV")
	writeCSVfileAllData(synthetic_Data_CAV,"Synthetic_Data_CAV")
	writeCSVfileAllData(synthetic_Data_No_Distinction,"Synthetic_Data_No_Distinction")
	
	writeCSVfileAllData(synthetic_Data_HDV_err,"Synthetic_Data_HDV_err")
	writeCSVfileAllData(synthetic_Data_CAV_err,"Synthetic_Data_CAV_err")
	writeCSVfileAllData(synthetic_Data_No_Distinction_err,"Synthetic_Data_No_Distinction_err")


	# Signalling when the production of synthetic data is finished
	print("The production of synthetic data is done")



    

# Get the objects "replication"
replicationsList = findReplications(CurrentExperiment)

nb_replication = len(replicationsList)-1
print(nb_replication)


# Remove precedent files
removeFiles("AllAggregatedData")
removeFiles("AllAggregatedDataNoDistinction")

# Run the multiple replications
runMultipleReplications(replicationsList)