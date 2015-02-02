#version 1.0, 01/29/14
import csv
import random

def posLinear(init):
	init = init + random.randint(7,9)
	return init
def negLinear(init):
	init = init - random.randint(7,9)
	return init
def posExp(init):
	init = init * random.uniform(1.0,1.3)
	return init
def negExp(init):
	init = init * random.uniform(.7,1.0)
	return init

studentName = raw_input("Please enter the name of the student: \n") +'.csv'

with open(studentName, 'w') as csvfile:
    dataWriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    
    numRounds = int(raw_input("How many rounds would you like? \n"))
    numTrials = int(raw_input("How many trials would you like? \n"))
    init = int(raw_input("What is the intial value of your dependent variable? \n"))
    
    relation = int(raw_input("What is the relationship you want data to represent? (enter a number)\n 1. Positive linear \t 2. Negative linear \t3. Exponential Growth \t 4. Exponential Decay \n"))
    if relation == 1:
    	relationship = posLinear
    if relation == 2:
    	relationship = negLinear
    if relation == 3:
    	relationship = posExp
    if relation == 4:
    	relationship = negExp
    
    data = [[]]
    for i in range(numTrials):
    	data[0].append(init)
    
    for i in range(1,numRounds+1):
    	data.append([])
    	for j in range(numTrials):
    		data[i].append(relationship(data[i-1][j]))

    dataWriter.writerows(data)

    
    