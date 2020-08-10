import math, os
from datetime import datetime as time
inA = [0, 4, 8, 16]
inB = [0, 2, 6, 12, 14, 20] 
apList = []
rtnlist = []
def arith(arr,a,n,d):
    base = a 
    temp = 0
    if(d==None):
        d = 0
    sumn = (n/2) * (2*base + (n-1)*d)
    for i in range(0,len(arr)):
        base = arr[i]
        print("arr:",arr[i])
        for j in range(0,len(arr)):
            print("i value is :",j)
            sn = base + (j-1)*temp
            snp1 = base + (j)*temp
            if(snp1 not in arr and sn in apList):
                print("new ele added")
                apList.append(sn)
        sn = base + (i-1)*temp
        snp1 = base + (i)*temp
        temp = d
        print("snp1 is ",snp1)
        if(snp1 not in arr):
            temp+=1
            continue
        else:
            print("outter cond")
    print(apList)
    return(apList,sumn)


""" def process(arr): # should be sorted before passing it here
    for i in range(0,100): # put range max element size from a and b arrays
"""

def main():
    begin = time.now()
    merged = inA + inB
    merged.sort()
    maxi = max(merged)
    rtnList,sumn = arith(merged,merged[0],maxi,None)
    # merged[-1:] ==> last index (len-1)
    d = 0

    for i in range(0,len(merged)-1):
        s = merged[i] + (i-1)*d 
        if(s not in merged):
            d += 1
            print(s)
    print(f'rtnlist is :{rtnlist} and sum of n terms :{sumn}')
    # rtnList, sumn = arith(merged,merged[0],merged[-1],None)
    # print(f'merged = {merged} , max = {maximum}')
    # print(f'the list is {rtnList}, sum = {sumn}')
    # print(arith(10290,989899989899595354548798000000000000000000000000000000000000006547655555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555000000000000006876878766666666667987657435675899567908976858789897679876890876890898768756565374754756466745896079875676574675865745765867465876857686797807967856746576780987654536789765456789765435678976546778674697856475768767567687086958687086758676870656476567964345674334766354365476586745500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000023423423423413515167834523526534535000000,12312423445))
    end = time.now()
    print(f"elapsed = {end - begin}")


if __name__ == "__main__":
    main()



