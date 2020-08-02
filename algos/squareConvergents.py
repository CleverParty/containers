import sys
from fractions import Fraction
sys.setrecursionlimit(10000)
a = 2
root = 2**2
def convergent(num):
    base = 1 
    if num == 0:
        return True
    sumCon = base +1/(1/2 + convergent(num-1)) # this just calculates the convergence recursively, for full solution it would be better to find numerator and denominator seperatelty in a for/while loop
    return sumCon

print(convergent(1000))