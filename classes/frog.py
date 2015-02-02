"""
PSEUDOCODE:
Frog and a Bug. 
1) The frog has tongue length; the bug has distance from frog 
and whether or not it has been eaten. 
2) While the bug is still uneaten, update
the distance of the bug (randomly); if the 
bug position is equal or less than then 
length of the frog's tongue, 
the bug is eaten and the program ends.

"""

import random

class Frog:
	def __init__(self, tongueLength):
		self.tongueLength = tongueLength

class Bug:
	def __init__(self):
		self.dist = random.randint(0,10)
		self.eaten = False

frog = Frog(2)
bug = Bug()


while bug.eaten == False:
	if bug.dist <= frog.tongueLength:
		bug.eaten = True
		print "bug was eaten"
	else:
		bug.dist = random.randint(0,10)
		print "bug is at " + str(bug.dist)


















