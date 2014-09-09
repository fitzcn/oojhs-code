class Barbarian:
    def __init__(self, name):
        self.level = 1    
        self.damage_per_second = 8     
        self.hitpoints = 45
        self.name = name
        self.dead = False

    def dies(self):
        print(self.name + " has died.")
        self.dead = True
        del self

class Archer:
    def __init__(self, name):
        self.level = 1
        self.damage_per_second = 7     
        self.hitpoints = 20
        self.name = name
        self.dead = False

    def dies(self):
        print(self.name + " has died.")
        self.dead = True
        del self

def fight(attacker, defender):
    defender.hitpoints = defender.hitpoints - attacker.damage_per_second
    attacker.hitpoints = attacker.hitpoints - defender.damage_per_second

def fightToDeath(attacker, defender):
    print("Fight to the death between " + attacker.name + " and " + defender.name)
    fightRound = 1
    while attacker.hitpoints > 0 and defender.hitpoints > 0:
        print("Fight round: ", fightRound)
        fight(attacker,defender)
        fightRound += 1
        if attacker.hitpoints <= 0:
            attacker.dies()
        if defender.hitpoints <= 0:
            defender.dies()

olympianArmy = [Barbarian("Sara"), Barbarian("Bruce")]
oracleArmy = [Archer("Sammy"), Archer("Bob")]

for i in range(0,len(oracleArmy)):
    fightToDeath(olympianArmy[i],oracleArmy[i])

for warrior in olympianArmy:
    print("Olypian Army status:")
    print(warrior.name + " dead? " + str(warrior.dead))

for warrior in oracleArmy:
    print("Oracle Army status:")
    print(warrior.name + " dead? " + str(warrior.dead))
