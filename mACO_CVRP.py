# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:34:46 2020

@author: Jay Prakash
"""

import DataParsing
import printsolution
import numpy
import csv
from functools import reduce


alfa = 2
beta = 5
sigm = 3
ro = 0.8
th = 80
fileName = "Input_Data.txt"
iterations = 10
ants = 25

def generateGraph():
    numVehicle, capacityLimit, demand, graph = DataParsing.parsedata(fileName)
    vertices = list(graph.keys())
    vertices.remove(0)

    edges = { (min(a,b),max(a,b)) : numpy.sqrt((graph[a][0]-graph[b][0])**2 + (graph[a][1]-graph[b][1])**2) for a in graph.keys() for b in graph.keys()}
    feromones = { (min(a,b),max(a,b)) : 1 for a in graph.keys() for b in graph.keys() if a!=b }
    
    return vertices, edges, capacityLimit, demand, feromones, graph

def solutionOfOneAnt(vertices, edges, capacityLimit, demand, feromones):
    solution = list()
    numRoutes = 0

    while(len(vertices)!=0):
        path = list()
        city = numpy.random.choice(vertices)
        capacity = capacityLimit - demand[city]
        path.append(city)
        vertices.remove(city)
        while(len(vertices)!=0):
            probabilities = list(map(lambda x: ((feromones[(min(x,city), max(x,city))])**alfa)*((1/edges[(min(x,city), max(x,city))])**beta), vertices))
            probabilities = probabilities/numpy.sum(probabilities)
            
            city = numpy.random.choice(vertices, p=probabilities)
            capacity = capacity - demand[city]

            if(capacity>0):
                path.append(city)
                vertices.remove(city)
            else:
                break
        solution.append(path)
        numRoutes += 1
    return solution, numRoutes

def rateSolution(solution, edges):
    s = 0
    for i in solution:
        a = 0
        for j in i:
            b = j
            s = s + edges[(min(a,b), max(a,b))]
            a = b
        b = 0
        s = s + edges[(min(a,b), max(a,b))]
    return s

def updateFeromone(feromones, solutions, bestSolution):
    Lavg = reduce(lambda x,y: x+y, (i[1] for i in solutions))/len(solutions)
    feromones = { k : (ro + th/Lavg)*v for (k,v) in feromones.items() }
    solutions.sort(key = lambda x: x[1])
    solutions.sort(key = lambda x: x[2])
    if(bestSolution!=None):
        if(solutions[0][1] < bestSolution[1]):
            bestSolution = solutions[0]
        for path in bestSolution[0]:
            for i in range(len(path)-1):
                feromones[(min(path[i],path[i+1]), max(path[i],path[i+1]))] = sigm/bestSolution[1] + feromones[(min(path[i],path[i+1]), max(path[i],path[i+1]))]
    else:
        bestSolution = solutions[0]
        
    for l in range(sigm):
        paths = solutions[l][0]
        L = solutions[l][1]
        for path in paths:
            for i in range(len(path)-1):
                feromones[(min(path[i],path[i+1]), max(path[i],path[i+1]))] = (sigm-(l+1)/L**(l+1)) + feromones[(min(path[i],path[i+1]), max(path[i],path[i+1]))]
    return bestSolution

def main():
    bestSolution = None
    vertices, edges, capacityLimit, demand, feromones, graph = generateGraph()
    
    for i in range(iterations):
        solutions = list()
        for _ in range(ants):
            solution, numOfVehicles = solutionOfOneAnt(vertices.copy(), edges, capacityLimit, demand, feromones)
            solutions.append((solution, rateSolution(solution, edges), numOfVehicles))
        bestSolution = updateFeromone(feromones, solutions, bestSolution)
        print(str(i)+":\t"+str(int(bestSolution[1]))+":\t"+str(int(bestSolution[2])))
        #saving in excel sheet
        with open('solutions.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(solutions)
    printsolution.printroutes(bestSolution, graph)    
    return bestSolution

    solution = main()
if __name__ == "__main__":
    
    print("file name:\t"+str(fileName)+
"\nalpha:\t"+str(alfa)+
"\nbeta:\t"+str(beta)+
"\nsigma:\t"+str(sigm)+
"\nrho:\t"+str(ro)+
"\ntheta:\t"+str(th)+
"\niterations:\t"+str(iterations)+
"\nnumber of ants:\t"+str(ants))

    solution = main()

    print("Solution: "+str(solution))   