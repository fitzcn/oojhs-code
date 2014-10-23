# coding: utf-8
import random
"""
INSTRUCTIONS:
write a function that removes one card from the deck permanently.
"""

def printOneRandomCard(deck):
	print(deck[random.randint(0,51)])

def printSevenRandomCards(deck):
	for i in range(1,8):
		printOneRandomCard(deck)

#put your function here!
def dealSevenCardHard(deck):
	return None


deck = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
"A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
"A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
"A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"]


#print(deck[50])
print("number of cards before call")
print(len(deck))
#dealSevenCardHand(deck)
print("number of cards after call")
print(len(deck))
for card in deck:
	print(card)
#print(deck[50])


#call your function here!








