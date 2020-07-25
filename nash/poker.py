import numpy as np
import nashpy as nashie

seq = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def high_card(hand):
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