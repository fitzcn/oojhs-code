class Wizard:
    def __init__(self, name, favSpell):
        self.name = name
        self.favSpell = favSpell
    def castFavSpell(self):
        print(self.name + " casts " + self.favSpell.name)

class Spell:
	def __init__(self, name):
		self.name = name

def practiceSpells(group):
	for wizard in group:
		wizard.castFavSpell()

expl = Spell("expelliarmus")
wL = Spell("wingardium leviosa")
pT = Spell("petrificus totalus")

harry = Wizard("Harry", expl)
hermione = Wizard("Hermione", wL)
ron = Wizard("Ron", pT)

group = [harry, hermione, ron]
practiceSpells(group)