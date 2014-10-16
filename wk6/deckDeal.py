# coding: utf-8
import random
"""
INSTRUCTIONS:
write a function that prints seven cards from the deck. 
Feel free to use printRandomItem if you need/want.
"""

def printRandomItem(lst):
	print(lst[random.randint(0,51)])
def nameYourFunction(nameYourParameter):
	None


deck = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
"A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
"A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
"A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"]

nameYourFunction(deck)
