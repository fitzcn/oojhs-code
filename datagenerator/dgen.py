#version 1.1, 02/02/15
import csv
import random

def posLinear(init):
	init = init + random.uniform(minDelta,maxDelta)
	return init
def negLinear(init):
	init = init - random.uniform(minDelta,maxDelta)
	return init
def posExp(init):
	init = init * random.uniform(minDelta,maxDelta)
	return init
def negExp(init):
	init = init * random.uniform(minDelta,maxDelta)
	return init

studentName = raw_input("Please enter a filename to save the data: \n") +'.csv'
relation = int(raw_input("Enter a number between 1-4 \n"))
if relation == 1:
    relationship = posLinear
if relation == 2:
    relationship = negLinear
if relation == 3:
    relationship = posExp
if relation == 4:
    relationship = negExp

numSteps = int(raw_input("How many time steps would you like? \n"))
numTrials = int(raw_input("How many trials would you like? \n"))
init = float(raw_input("What is the intial value of your dependent variable? \n"))

#relation = int(raw_input("What relationship do you want? (enter a number)\n1. Positive linear \n2. Negative linear \n3. Exponential Growth \n4. Exponential Decay \n"))


minDelta = float(raw_input("What's the minimum amount of change? \n"))
maxDelta = float(raw_input("What's the maximum amount of change? \n"))

data = [['time'],[0]]
for i in range(1,numTrials+1):
    data[0].append("trial " + str(i))
    data[1].append(init)
  
for i in range(2,numSteps+2):
    data.append([i-1])
    for j in range(1,numTrials+1):
        data[i].append(relationship(data[i-1][j]))

with open(studentName, 'w') as csvfile:
    dataWriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    dataWriter.writerows(data)    