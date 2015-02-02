import random

class Agent():
	def __init__(self, *args):
		self.attrList = []
		for arg in args:
			self.attrList.append(arg)


def posLinear(agent,attrIndex):
	agent.attrList[attrIndex] = agent.attrList[attrIndex] + random.randint(7,9)
	return agent.attrList[attrIndex]
def negLinear(agent,attrIndex):
	agent.attrList[attrIndex] = agent.attrList[attrIndex] - random.randint(7,9)
	return agent.attrList[attrIndex]
def posExp(agent,attrIndex):
	agent.attrList[attrIndex] = agent.attrList[attrIndex] * random.uniform(1.0,1.3)
	return agent.attrList[attrIndex]
def negExp(agent,attrIndex):
	agent.attrList[attrIndex] = agent.attrList[attrIndex] * random.uniform(.7,1.0)
	return agent.attrList[attrIndex]


numRounds = int(raw_input("How many rounds would you like? \n"))
numAgents = int(raw_input("How many agents would you like? \n"))
agents = []
for i in range(numAgents):
	agents.append(Agent(100,200,300,700))

for i in range(numRounds):
	print posLinear(agents[0],1), negLinear(agents[1],1), posExp(agents[2],1), negExp(agents[3],1)


print agents[0]



"""
while self.strength > 50:
    self.strength = self.strength*random.uniform(0.5,1.0)
    print airJ.strength
    airJ.wear()
"""