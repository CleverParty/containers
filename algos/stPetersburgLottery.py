import os,math
import numpy as np
x = np.array([0.23,0.5,0.8])

def Step(item):
    return 1 * (item >= 0.5)

for i in x:
    rtrnval = Step(i)
    print(rtrnval)

stepfunc = np.heaviside(x, 0.5)
print(stepfunc)
