class Barbarian:
  #  hitpoints,attack,speed = 150,60,4

    def __init__(self, name):
        self.preferred_target = "any"
        self.attack_air = False
        self.attack_ground = True
        self.attack_type = "melee"
        self.housing_space = 1
        self.training_time = 1
        self.movement_speed = 16
        self.attack_speed = 1
        self.barracks_level = 1
        self.range = .4 
        self.level = 1    
        self.damage_per_second = 8     
        self.hitpoints = 45
        self.training_cost = 25
        self.research_cost = None
        self.laboratory_level = None
        self.research_time = None
        self.name = name

    def dies(self):
        print('dying')
        print(self.name + " has died.")
        del self


class Archer:
#    hitpoints,attack,speed = 200,50,2

    def __init__(self, name):
        self.preferred_target = "any"
        self.attack_air = False
        self.attack_ground = True
        self.attack_type = "melee"
        self.housing_space = 1
        self.training_time = 25
        self.movement_speed = 24
        self.attack_speed = 1
        self.barracks_level = 2
        self.range = 3.5             
        self.level = 1
        self.damage_per_second = 7     
        self.hitpoints = 20
        self.training_cost = 50
        self.research_cost = None
        self.laboratory_level = None
        self.research_time = None
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
