num = 10

# result = list(map(lambda x: a ** b, range(num)))
def sumOfDigits(cargo):
    digitsum = 0
    while cargo:
        digitsum += cargo/10
        cargo//10
    return digitsum

carry = []

for a in range(num):
    for b in range(num):
        power = pow(a,b)
        sum = sumOfDigits(power)
        # now store the highest sum available and check if greater
        carry.append(sum)


print(carry)