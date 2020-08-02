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


def numeratorDenomenatorForm():
    numerator = 3
    denomenator = 2
    count = 0
    for i in range(0,1000):
        numerator = numerator + 2*denomenator
        denomenator = numerator + denomenator
        if(len(str(numerator)) > len(str(denomenator))):
            count += 1
    return count

print(convergent(1000))
print(f'the number of fractions with more digits in numerator than denomenator are: {numeratorDenomenatorForm()}')