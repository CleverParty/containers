import math,os
import subprocess
GlobalConst = 0
GlobalList = [[2, 4, 6], [3, 6, 9], [4, 8, 12]] 

def matrix(arr):
    res = [c for c in arr]
    print(res[0][2])
    for i in range(0,3):
        for j in range(0,3):
            print(res[i][j])
    # sub = [c,x for x in arr]


def main():
    matrix(GlobalList)

if __name__ == "__main__":
    main()
    