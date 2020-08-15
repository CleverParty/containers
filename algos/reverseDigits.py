import os,math

numList = []
GlobalStore = 0

def checkList(arr):
    length = len(str(arr))
    if(length%2 != 0):
        flag = True
        GlobalStore = length**2
        return(flag,length)
    else:
        res = [x for x in arr]
        flag = False
        return(flag,length)


def main():
    arr = [12341345,234158292,8002842985]
    flag,length = checkList(arr)
    print(flag,length)
    print(GlobalStore)


if __name__ == "__main__":
    main()