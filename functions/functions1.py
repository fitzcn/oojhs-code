def solveHW(r1,r2,dist):
	totalMPH = r1 + r2 
	time = dist/float(totalMPH)
	return time
	
#print solveHW(550,650,2000)

#print (solveHW(260,300,140))

def distance(r,t):
	d = r*t
	return d

print (distance(5,10))

"""
create a function called distance
give it a rate and time
return the distance traveled
"""

