import numpy as np
import os
import pandas as pd
# import nashpy as nash
import math, time
# easy way :-
from pokereval.card import Card
from pokereval.hand_evaluator import HandEvaluator

TwoPair = False
ThreePair = False
FourKind = False
RoyalFlush = False
cwd = os.getcwd()
pokertxt = open('/Users/shanmukhasurapuraju/containers/data/poker.txt')
hands = pokertxt.read().split(',')
take = 0
seq = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def highCard(hand):
    faces = [f for f,s in hand]
    if faces[0] == 'A' :
        print("Ace high")
    return "high_card", sorted(faces, key=lambda f: faces.index(f), reverse=True)[0]

def decideHand(hand):
    suit = [s for f,s in hand]
    flush = suit.count(suit[0]) == len(suit) 
    if(flush):
        print("Flush baby")
    return flush

def kinds(hand):
    num = [n for f,n in hand]
    if len(num) == len(set(num)):
        return "Two of a Kind"
    else :
        return "Unique Cards"
    # count = map(lambda x : n if(n in num) else print("values"))
    print ("test")

def swap(hand):
    firstWinningCard = hand[0]
    return firstWinningCard

def thePot(amount, startAmount):
    take += amount
    if take < startAmount :
        print("the logical limit of gambling has passed")
    return take

def flush(hand):
    suit = [s for f,s in hand]
    if(len(suit) == len(set(suit))):
        print("Flush!")

# easy way :-
""" hole = [Card(10, 1), Card(2, 2)]
score = HandEvaluator.evaluate_hand(hole, [])
print(score) """
# print(hands[0])
# inputFile = pd.read_csv (r'/Users/shanmukhasurapuraju/containers/data/poker.txt')
# outputFile.to_csv (r'/Users/shanmukhasurapuraju/containers/data/poker.csv', index=None)
print(swap(hands[0][1]))