import random
# lst[0:4]

def ship(nameA, nameB):
	lenA = len(nameA)
	lenB = len(nameB)
	port = nameA[0:random.randint(1,lenA)]
	bow = nameB[0:random.randint(1,lenB)]
	ship = port + bow 
	return ship


nameA = input("Please enter the first name: \n") 
nameB = input("Please enter the second name: \n") 

aBship = ship(nameA, nameB)
print(aBship + " setting its sails")