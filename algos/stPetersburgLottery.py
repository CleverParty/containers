import os,math
import numpy as np
import random as r 
from random import shuffle

x = np.array([0.23,0.5,0.8])

def Step(item):
    return 1 * (item >= 0.5)

for i in x:
    rtrnval = Step(i)
    print(rtrnval)

# shuffle the possible H/T

def generateOutcomes():
    h = r.uniform(0, 0.5)
    t = 1 - h
    return h,t

def gamblerOutcome(m,s,heads,tails):
    base = m # initial pot which either compounds or gets evaporated
    cost = s # cost per game
    pot = 0 # base cases are as below
    if(cost < base):
        # probability reduces to 0
        return 0+m
    if(tails > heads):
        # game ends if tails is an out come
        return pot
    elif(heads > tails):
        pot = pot + m
        return pot
        


stepfunc = np.heaviside(x, 0.5)
print(stepfunc)
heads , tails = generateOutcomes()
print(heads)
print(tails)