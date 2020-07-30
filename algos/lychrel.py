
GlobalCounter = 0

def palindrome(number):
    if(int(str(number)[::-1]) == number) :
        return True
    else:
        return False

def lychrel(cargo):
    sumVal = int(str(cargo)[::-1])  +  cargo
    if(palindrome(sumVal)):
        print(f'this took {GlobalCounter+1} iterations')
    else :
        lychrel(sumVal)
        print(f'this took {GlobalCounter+1} iterations')

lychrel(123)



print(palindrome(125372))