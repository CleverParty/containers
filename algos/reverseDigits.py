import os,math

numList = []
GlobalStore = 0

def checkList(arr):
    length = len(str(arr))
    if(length%2 != 0):
        flag = True
        GlobalStore = (length*2)**3
        return(flag,GlobalStore)
    else:
        res = [x for x in arr]
        flag = False
        return(res,length)


def main():
    arr = [12341345,234158292,8002842985]
    flag,length = checkList(arr)
    print(flag,length)
    checkList(arr*8)
    print(GlobalStore)


if __name__ == "__main__":
    main()