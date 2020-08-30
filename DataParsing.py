# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:34:37 2020

@author: Jay Prakash
"""
#Parsing the data and reading the parameters from file#

import re

filename= "Input_Data.txt"
file= open(filename, 'r')
content = file.read()

#searching pattern in contents in file
VehicleCapacity =re.search(r"^\s+(\d+)\s+ (\d+)$", content, re.MULTILINE)
NumVehicle = int(VehicleCapacity.group(1))
Capacity = int(VehicleCapacity.group(2))
                 
tuples = re.findall(r"^\s+(\d+)\s+ (\d+)\s+ (\d+)\s+ (\d+)\s+", content, re.MULTILINE)
graphtuples = re.findall(r"^\s+(\d+)\s+ (\d+)\s+ (\d+)\s+", content, re.MULTILINE)


demand=[]
for tuple in tuples:   
    d = tuple[0],tuple[3]
    d= list(d)
    demand.append(d)    

#Converting customer location (XCOORD, YCOORD) in to Graph Dict
graph = {int(a):(int(b),int(c)) for a,b,c in graphtuples}
#Converting customer demand  in to  Dict
demand = {int(a):int(b) for a,b in demand}

print('No. of Vehicle, Capacity')
print(NumVehicle, '\t\t', Capacity)
print('Customer Demand')
print(demand)
print('Customer Location Coord XY')
print(graph)
#Number_Vehicles= 
file.close()


