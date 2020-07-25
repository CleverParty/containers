import numpy as np
import nashpy as nashie

seq = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def high_card(hand):
    allfaces = [f for f,s in hand]
    if allfaces[0] == 'A' :
        print("Ace high")
    return "high_card", sorted(allfaces, key=lambda f: allfaces.index(f), reverse=True)[0]