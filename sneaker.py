import random

class Sneaker():
   def __init__(self, materialStrength):
       self.materialStrength = materialStrength
       self.strength = 100
   def wear(self):
       self.strength = self.strength*random.uniform(0.5,1.0)

airJ = Sneaker(1)

while airJ.strength > 50:
    print airJ.strength
    airJ.wear()