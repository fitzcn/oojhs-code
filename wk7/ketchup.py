
ourMachine = {"amount of yellow color",500: "base", 500: "Color options", ['red','green','yellow']}
 
dispenseKetchup(batch):
	ourMachine["base"] = ourMachine["base"] - 50

class Machine(self):
	self.base = 500
	self.colors = ['red','green','yellow']
	self.yellow_available = 500
	def dispenceBatch(self, batch):
		self.yellow_available -= 50


dispenseKetchup(batch):
	ourMachine.dispenseBatch(batch)