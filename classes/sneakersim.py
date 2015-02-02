"""
create a sneaker that has a strength value (100)

print shoe strength

continue to print and decrease shoe 
strength by random number until shoe 
is below 50 
"""

import random

sneaker = 100
print sneaker

while sneaker > 50:
	sneaker = sneaker - random.randint(1,20)
	print

if sneaker < 50:
	print "Get new shoes"
