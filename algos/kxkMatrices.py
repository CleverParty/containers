import math,os
import subprocess
GlobalConst = 0
GlobalList = [[2, 4, 6], [3, 6, 9], [4, 8, 12]]

def matrix(arr,k):
    res = [c for c in arr]
    print(res[0][2])
    for i in range(0,len(arr[0])):
        for j in range(i, k+1):
            if((i+j) == (i+1) and j == (i+1)):
                print((i*j)/2)
            if(j == (i+1)/2):
                print(res[i][j])
    # sub = [c,x for x in arr]


def main():
    matrix(GlobalList,2)

if __name__ == "__main__":
    main()
    