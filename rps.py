"""
Initialize two players, each with a hand attribute and a play function that randomly selects
and sets a players' hand attrinbute value from rock, paper, or scissors.
Compare the hand values of the two players:
	if they values are the same, play again
	if not, declare a winner based on the rules of the game
"""

import random

class Player:
	def __init__(self):
		self.hand = ""

	def play(self):
		hands = ['rock', 'paper', 'scissors']
		self.hand = hands[random.randint(0,2)]

jack = Player()
jill = Player()

while jack.hand == jill.hand:
	jack.play()
	jill.play()

if jack.hand == 'rock':
	if jill.hand == 'paper':
		print "Jill wins! paper beats rock"
	else:
		print "Jack wins! rock beats scissors"

if jack.hand == 'paper':
	if jill.hand == 'scissors':
		print "Jill wins! scissors beats paper"
	else:
		print "Jack wins! paper beats rock"

if jack.hand == 'scissors':
	if jill.hand == 'rock':
		print "Jill wins! rock beats scissors"
	else:
		print "Jack wins! scissors beats paper"


