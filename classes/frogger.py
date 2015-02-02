import random

class Frog:
    def __init__(self, tongueLength):
        self.tongueLength = tongueLength

class Bug:
    def __init__(self):
        self.dist = random.randint(0,10)
        self.eaten = False

keropi = Frog(2)
fly = Bug()

i = 0
while fly.eaten == False:
    i+=1
    if fly.dist <= keropi.tongueLength:
        fly.eaten = True
        print "Fly was eaten"
    else:
        fly.dist = random.randint(0,10)
        print i


"""

import random

class Frog:
    def __init__(self, tongueLength):
        self.tongueLength = tongueLength

class Bug:
    def __init__(self):
        self.position = random.randint(0,20)
        self.eaten = False

kermit = Frog(8)
irma = Bug()

while irma.eaten == False:
    if kermit.tongueLength >= irma.position:
        irma.eaten = True
        print "irma was eaten"
    else:
        irma.dist = random.randint(0,20)
"""