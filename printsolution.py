# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:12:55 2020

@author: Jay Prakash
"""
# import DataParsing
import matplotlib.pyplot as plt
import numpy as np

# fileName = "Input_Data.txt"
# numVehicle, capacityLimit, demand, graph = DataParsing.parsedata(fileName)
# solution= ([[15, 17], [14, 16], [22, 21, 20], [13, 18, 19], [1, 2, 4, 3], [24, 25, 23], [12, 11, 8, 9], [5, 7, 6, 10]], 466.2594985481975, 8)

def printroutes(solution, graph):
    
    routes = solution[0]    
    
    xyd = list(graph.values())
    xyd = np.array(xyd)
    
    plt.scatter(xyd[:,0], xyd[:,1], marker='s', s=10)
    plt.scatter(xyd[0,0], xyd[0,1], marker='s', s=40)
    
    for x in routes:
        xcoord = [xyd[0,0]]
        ycoord = [xyd[0,1]]
        
        for i in x:             
            xcoord.append(xyd[i,0])
            ycoord.append(xyd[i,1])
        xcoord.append(xyd[0,0])
        ycoord.append(xyd[0,1])
                
        plt.plot(xcoord, ycoord)    
    plt.title("Route Map Traveled by Different Vehicles")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show() 