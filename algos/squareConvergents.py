import sys
from fractions import Fraction
sys.setrecursionlimit(10000)
a = 2
root = a**2
def convergent(num):
    base = 1 
    if num == 0:
        return False
    elif num > 1000 :
        return None
    num -= 1
    sumCon = base +1/(1/2 + convergent(num)) # this just calculates the convergence recursively, for full solution it would be better to find numerator and denominator seperatelty in a for/while loop
    return sumCon

print(convergent(1000))