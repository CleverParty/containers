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
    denominator = 2
    count = 0
    for _ in range(0,1000):
        # print(f'{numerator} and {denomenator}')
        """ if(i==0):
            n = numerator + nextnumerator """
        denominator = numerator + denominator
        numerator = denominator + 2*denominator
        # print(numerator)
        if(len(str(numerator)) > len(str(denominator))):
            count += 1
    return count

print(convergent(10))
print(f'the number of fractions with more digits in numerator than denomenator are: {numeratorDenomenatorForm()}')