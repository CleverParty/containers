import time

carry = []
sumCarry = []
maxDigits = 0
# result = list(map(lambda x: a ** b, range(num)))

def sumOfDigits(cargo):
    digitsum = 0
    while cargo:
        digitsum += cargo%10
        cargo //= 10
    return digitsum
    
for i in range(0,100):
    for j in range(0,100):
        value = sumOfDigits(i**j)
        if value > maxDigits:
            maxDigits = value

sumOfDigits(carry)
# store = max(sumCarry)
print(maxDigits)

