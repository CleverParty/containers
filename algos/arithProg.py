import math, os
from datetime import datetime as time
inA = [0, 4, 8, 16]
inB = [0, 2, 6, 12, 14, 20] 
apList = []
def arith(arr,a,n,d):
    base = a
    if(d==None):
        d = 0
    sumn = (n/2) * (2*base + (n-1)*d)
    for i in range(0,len(arr)):
        base = arr[i]
        print(base)
        sn = base + (i-1)*d
        snp1 = base + (i)*d
        if(snp1 not in arr):
            d=d+1
        print(f'{base} and + 1 = {snp1}')
        apList.append(sn)
    print(apList)
    return(apList,sumn)


""" def process(arr): # should be sorted before passing it here
    for i in range(0,100): # put range max element size from a and b arrays
"""

def main():
    begin = time.now()
    # rtnList,sumn = arith(merged,1,10,3)
    merged = inA + inB
    merged.sort()
    rtnList, sumn = arith(merged,merged[0],merged[-1],None)
    # print(f'merged = {merged} , max = {maximum}')
    print(f'the list is {rtnList}, sum = {sumn}')
    # print(arith(10290,989899989899595354548798000000000000000000000000000000000000006547655555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555000000000000006876878766666666667987657435675899567908976858789897679876890876890898768756565374754756466745896079875676574675865745765867465876857686797807967856746576780987654536789765456789765435678976546778674697856475768767567687086958687086758676870656476567964345674334766354365476586745500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000023423423423413515167834523526534535000000,12312423445))
    end = time.now()
    print(f"elapsed = {end - begin}")


if __name__ == "__main__":
    main()



