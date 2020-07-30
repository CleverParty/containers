import sys
sys.setrecursionlimit(10000)
counter = 0

def palindrome(number):
    if(int(str(number)[::-1]) == number) :
        return True
    else:
        return False

def lychrel(cargo , iter = 0):
    sumVal = int(str(cargo)[::-1])  +  cargo
    if(iter > 996):
        print("probably lychrel number")
        return 3
    # print(sumVal)
    if(palindrome(sumVal)):
        print(f'this took {iter} iterations')
        return 1
    else:
        lychrel(sumVal, iter+1 )
        return 2


counter = 0
print(lychrel(196))
for n in range(0,10000):
    print(f'for n value:= {n}')
    if(lychrel(n) == 3):
        counter += 1
    else:
        print(f'plaindrome setting was found')

print(counter)