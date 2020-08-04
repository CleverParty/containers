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
    for i in range(100):
        h = r.uniform(0, 0.5)
        t = 1 - h
    return h,t


stepfunc = np.heaviside(x, 0.5)
print(stepfunc)
generateOutcomes()
