num = 2
carry = []
sumCarry = []
print(23)
# result = list(map(lambda x: a ** b, range(num)))
def sumOfDigits(cargo):
 
    for arr in carry:
        digitsum = 0
        while arr:
            dig = arr/10
            digitsum = digitsum + dig
            arr = arr//10
        sumCarry.append(digitsum)




for i in range(100):
    for j in range(100):
        carry.append(pow(j,i))
    

"""for i in range(0,1):
    for j in range(0,1):
        power = pow(i,j)
        sum = sumOfDigits(power)
        # now store the highest sum available and check if greater
        carry.append(sum)"""

sumOfDigits(carry)
store = max(sumCarry)
print('%f' % (store))
