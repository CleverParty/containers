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
arrayOfInt = [1,2,3,4,5]


def consecutiveNumberSum(arrayOfInt,startIndex,endIndex,sumSet=0):
    if (startIndex > endIndex):
        print(f'{sumSet} and {startIndex} , {endIndex}')
    consecutiveNumberSum(arrayOfInt,startIndex+1,endIndex,sumSet + arrayOfInt[startIndex])
    return sumSet

rtrnSum = consecutiveNumberSum(arrayOfInt=arrayOfInt, endIndex=len(arrayOfInt), startIndex=0)
print(rtrnSum)


