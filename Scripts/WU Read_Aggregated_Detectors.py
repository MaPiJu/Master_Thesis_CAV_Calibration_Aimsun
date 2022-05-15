# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 17:18:44 2022

@author: Marc
"""

from AAPI import *
import os



# Current Location of files
cwd = os.getcwd()

# Cycle time of aggregation of Data (here every 10min)
cycleTimes = [1800,2400,3000,3600,4200,4800,5400,6000,6600,7200,7800,8400]

# Header of the list of the aggregation of the data
initListAgg = [["ID_Replication","ID_Detector","ID_Vehicle","Time","Count","Speed"]]

# Header for list of the aggregated data without distinguish vehicle type
initListAgg_II = [["ID_Replication","ID_Detector","ID_Vehicle","Time","Count","Speed"]]

def findAllDetectors():
    NbDetectors = AKIDetGetNumberDetectors()
    DETECTOR_ID = []
    for i in range(NbDetectors):
        DETECTOR_ID.append(AKIDetGetIdDetector(i))
    return DETECTOR_ID



def AAPILoad():

    #AKIPrintString( "AAPILoad" )

    return 0



def AAPIInit():

    #AKIPrintString( "AAPIInit" )

    return 0

def AAPISimulationReady():

    #AKIPrintString( "AAPISimulationReady" )
    
    return 0



def AAPIManage(time, timeSta, timeTrans, acycle):

    #AKIPrintString( "AAPIManage" )

    return 0


# This function returns the current Id number
def readTempIdFile():
    
    return(int(open(cwd+"\\Id.txt","r").read()))
    

def addRowList(initList,newRow):
    for row in range(len(initList)):
        inner_list = []
        for col in range(len(newRow)):
            inner_list.append(newRow[col])
    initList.append(inner_list)



def aggregatedArrayMeasurements(time,replicationId, detectorId,aggList,IdVehicle):
    
    counterAggregated = AKIDetGetCounterAggregatedbyId( detectorId, IdVehicle)

    speedAggregated = AKIDetGetSpeedAggregatedbyId( detectorId, IdVehicle)
    
    aggHumanMeasurement= [replicationId,detectorId,IdVehicle, time, counterAggregated, speedAggregated]
    
    aggList = addRowList(aggList,aggHumanMeasurement)
    
    return aggList



def writeCSVfileAllData(arrayAggData,Name):

	if os.path.exists(cwd+"\\"+str(Name)+".csv"):

		file = open(cwd+"\\"+str(Name)+".csv","a")
	
		for line in arrayAggData[1:]:    
			for data in line:
				file.write(str(data)+",")
			file.write("\n")
		file.close()

	else:
		file = open(cwd+"\\"+str(Name)+".csv","w")

		for line in arrayAggData:    
			for data in line:
				file.write(str(data)+",")
			file.write("\n")
		file.close()



def AAPIPostManage(time, timeSta, timeTrans, acycle):
    
    DETECTOR_IDS = findAllDetectors()

    currentReplicID = readTempIdFile()
    
    IDHuman = 1
    IDAutonomous = 2    
        
    for t in cycleTimes:
        
        if time == t:
            
            for detectorId in DETECTOR_IDS:
                
                aggList = initListAgg
                aggListNoDist = initListAgg_II
                
                # Add aggregated data for Human Driven Vehicles           
                aggregatedArrayMeasurements(time,currentReplicID ,detectorId ,aggList, IDHuman)
                
                # Add aggregated data for Autonomous Vehicles                
                aggregatedArrayMeasurements(time,currentReplicID ,detectorId ,aggList, IDAutonomous)

                # Add aggregated data for not distinguished vehicle
                aggregatedArrayMeasurements(time,currentReplicID ,detectorId ,aggListNoDist, 0)
                
    if time == 8400:
        
        writeCSVfileAllData(aggList,"AllAggregatedData")
        writeCSVfileAllData(aggListNoDist,"AllAggregatedDataNoDistinction")
                

    return 0



def AAPIFinish():

    #AKIPrintString( "AAPIFinish" )

    return 0



def AAPIUnLoad():

    #AKIPrintString( "AAPIUnLoad" )

    return 0



def AAPIPreRouteChoiceCalculation(time, timeSta):

    #AKIPrintString( "AAPIPreRouteChoiceCalculation" )

    return 0



def AAPIEnterVehicle(idveh, idsection):

    return 0



def AAPIExitVehicle(idveh, idsection):

    return 0



def AAPIEnterPedestrian(idPedestrian, originCentroid):

    return 0



def AAPIExitPedestrian(idPedestrian, destinationCentroid):

    return 0



def AAPIEnterVehicleSection(idveh, idsection, atime):

    return 0



def AAPIExitVehicleSection(idveh, idsection, atime):

    return 0



def AAPIVehicleStartParking (idveh, idsection, time):
    return 0