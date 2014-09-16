class Barbarian:
  #  hitpoints,attack,speed = 150,60,4

    def __init__(self, name):
        self.level = 1    
        self.damage_per_second = 7     
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
        self.hitpoints = 45
        self.name = name

    def dies(self):
        print(self.name + " has died.")
        del self

def fight(attacker, defender):
    defender.hitpoints = defender.hitpoints - attacker.damage_per_second
    attacker.hitpoints = attacker.hitpoints - defender.damage_per_second



Sara = Archer("Sara")
Bruce = Barbarian("Bruce")

fightRound = 1

while Sara.hitpoints > 0 and Bruce.hitpoints > 0:
    print("Fight round: ", fightRound)
    print(Sara.hitpoints)
    print(Bruce.hitpoints)
    fight(Bruce,Sara)
    fightRound += 1
    if Sara.hitpoints <= 0:
        Sara.dies()
    if Bruce.hitpoints <= 0:
        Bruce.dies()





























