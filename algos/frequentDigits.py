import math

list_1 = [25,2,3,57,38,4,678,897,5878,1]
searchDict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}
print(list_1)

def digitTotal(arr):
    for i in range(0,len(arr)):
        if(str(arr[i]) in str(searchDict.keys())):
            print(f'the values are {arr[i]}')
            searchDict[i] += 1
        elif(len(str(arr[i])) >= 2):
            n = arr[i]
            res = [int(x) for x in str(n)] 
            print("digit is",res,n)
            for index in res:
                if(str(index) in str(searchDict.keys())):
                    searchDict[index] += 1
                    print(searchDict)

                
digitTotal(list_1)
print(list_1)
print(searchDict)