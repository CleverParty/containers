import math

list_1 = [25,2,3,57,38,41]
searchDict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
print(searchDict)

def digitTotal(arr):
    for i in range(0,len(arr)):
        if(str(arr[i]) in str(searchDict.keys())):
            print(f'the values are {arr[i]}')
            searchDict[i] = arr[i]
        if(len(str(arr[i])) >= 2):
            n = arr[i]
            while(n>0):
                n /= 10
                if(str(n) in str(searchDict.keys())):
                    print(f'values of the new dict are:{arr[i]}')
                    searchDict[i] = n
                
digitTotal(list_1)
print(searchDict)