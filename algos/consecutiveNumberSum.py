import math

"""lastNumb = number
        if( number == 0 ):
            return 1
        sumOfFew = i + consecutiveNumberSum(number-1)
        print( sumOfFew )
        if( sumOfFew <= i):
            print(f'sum is : {sumOfFew} and i : {number}')
        elif( i > lastNumb ):
            return 0
        return sumOfFew """


def consecutiveNumberSum(number):
    sumOfFew = 0
    for i in range(1,number):
        for j in range(1,i):
            print(j)
            sumOfFew += j
            print(sumOfFew)
            if ( sumOfFew == 5 ):
                print(i)

consecutiveNumberSum(5)

