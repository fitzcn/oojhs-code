# coding: utf-8
import random

"""
write a function that prints a random card in the deck.
"""
def selectRandom(lst):
	index = random.randint(0,51)
	print lst[index]

"""
write a function that will print each card in a deck.
hint: use a "for/in" loop.
"""
def nameYourFunction(nameYourVariable):
	None

"""
write a function that prints each card in a deck in reverse
you can use:
1-as a "for/in" loop
2-as a "while" loop
3-as a "in range" loop
"""
def yourReverseFunction(yourVariable):
	None

deck = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
"A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
"A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦",
"A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"]

selectRandom(deck)
printEach(deck)
printEachInReverse(deck)
printEach(deck)