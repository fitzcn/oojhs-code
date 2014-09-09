import random

"""
1. define a class call Die
	a. remove None and initialize self.numSides to numSides
	b. remove None and initialize self.value to a random integer 
		between values 1 and numSides (from Codecademy, think back!)
	c. define a function within class Die called rollDie that rolls the dice
		i.e. rollDie updates self.value with a new random integer

remember: dies() was a function within a class last week, it was defined like this:
    def dies(self):
        print(self.name + " has died.")
        del self

"""
class Die:
	def __init__(self, numSides):
		self.numSides = None
		self.value = None
	def rollDie(self):
		None		

"""
2. define a function called rollCup
	a. rollCup takes a cup (a list of dice) and 
	uses a for loop to roll each one

remember: call functions of a class by using the objects' 
name  + . + nameOfFunction() 

from last week, sara the archer died by writing:
sara.dies()
"""	
def rollCup(cup):
	None

"""
2. Create a function called printCup
	a. printCup takes a cup (a list of dice) and 
	uses a for loop to print the values of each die 
	in the cup on the same line

hint: if you completed part 2 of printingThroughLoops,
you've already written this function once!

"""	

def printCup(cup):
	None

"""
declare 5 die variable objects, each to be six-sided
call them something that makes sense, like die1, die2, etc.

remember: Just like initializing a barbarian named Bruce last week
Bruce = Barbarian("Bruce")
you need a formula like
name + = + className(initial parameters)
"""

None
None
None
None
None
None

"""
initialize a list called "cup" (like fibSeq or chorusWords)
put the 5 die into the "cup"
"""
cup = None

"""
create a loop that runs 3 times. 
each time the loop runs, call the functions 
printCup and rollCup
"""

for i in range(0,10):
	None
	None
