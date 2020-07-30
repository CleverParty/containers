
GlobalCounter = 0

def palindrome(number):
    if(int(str(number)[::-1]) == number) :
        return True
    else:
        return False

def lychrel(cargo , iter = 0):
    sumVal = int(str(cargo)[::-1])  +  cargo
    print(sumVal)
    GlobalCounter + 1
    if(palindrome(sumVal)):
        print(f'this took {iter} iterations')
    else :
        lychrel(sumVal, iter+1 ) 

lychrel(89)
# for n in range(0,100):
#     print(lychrel(n))