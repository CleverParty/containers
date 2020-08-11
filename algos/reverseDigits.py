import os,math

numList = []

def checkList(arr):
    length = len(str(numList))
    if(length%2 != 0):
        flag = True
        return(flag,length)
    else:
        res = [x for x in arr]
        print(res)
        flag = False
        return(flag,length)


def main():
    arr = [12341345]
    flag,length = checkList(arr)
    print(flag,length)


if __name__ == "__main__":
    main()