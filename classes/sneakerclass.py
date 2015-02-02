"""
refactor the code to use a Sneaker class
(i.e. write a Sneaker class and replace
instances of the Sneaker variable with a
sneaker object)

PSEUDOCODE:
1) create a sneaker that has a strength value (100)
2) print shoe strength
3) continue to print and decrease shoe 
strength by random number until shoe 
strength is below 50 



sneaker = 100
print sneaker

while sneaker > 50:
	sneaker = sneaker - random.randint(1,20)
	print

if sneaker < 50:
	print "Get new shoes"
"""

import random

class Sneaker:
	def __init__(self):
		self.strength = 100

nike = Sneaker()
sketchers = Sneaker()

print nike.strength
print nike
print sketchers

















