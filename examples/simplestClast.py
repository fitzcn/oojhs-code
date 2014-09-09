class Barbarian:
  #  hitpoints,attack,speed = 150,60,4

    def __init__(self, name):
        self.level = 1    
        self.damage_per_second = 8     
        self.hitpoints = 45
        self.name = name

    def dies(self):
        print(self.name + " has died.")
        del self

class Archer:
#    hitpoints,attack,speed = 200,50,2

    def __init__(self, name):
        self.level = 1
        self.damage_per_second = 7     
        self.hitpoints = 20
        self.name = name

    def dies(self):
        print(self.name + " has died.")
        del self

def fight(attacker, defender):
    defender.hitpoints = defender.hitpoints - attacker.damage_per_second
    attacker.hitpoints = attacker.hitpoints - defender.damage_per_second



sara = Archer("Sara")
bruce = Barbarian("Bruce")

fightRound = 1

while sara.hitpoints > 0 and bruce.hitpoints > 0:
    print("Fight round: ", fightRound)
    fight(bruce,sara)
    fightRound += 1
    if sara.hitpoints <= 0:
        sara.dies()
    if bruce.hitpoints <= 0:
        bruce.dies()
