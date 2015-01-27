import random

class World:
    def __init__(self):
        self.population = []

class Bunny:
    def __init__(self):
        self.sex = sexes[random.randint(0,1)]

def encounter(peter, jessica):
    if peter.sex != jessica.sex:
        oojhs.population.append(Bunny())


sexes = ['male','female']



oojhs = World()

for i in range(0,5):
    oojhs.population.append(Bunny())

for i in range(0,10):
    encounter(oojhs.population[random.randint(0,len(oojhs.population)-1)],
        oojhs.population[random.randint(0,len(oojhs.population)-1)])

for bunny in oojhs.population:
    print bunny.sex

