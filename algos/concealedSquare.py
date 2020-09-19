import os,math
import re

stringtocompare = "1_2_3_4_5_6_7_8_9_0"
xCount = 0
yCount = 0
zCount = 0
def squared(num):
    temp = 1
    for i in range(0,num):
        temp = i*i
        # sq = i**2
        xCount += 1
        yCount += 1
        zCount += 1
        x = re.findall(r"\b2", str(temp))
        y = re.findall(r"\b1", str(temp))
        z = re.findall(r"0\b", str(temp))
        if(x):
            print(f"the next few numbers start with 2 is {xCount}")
        if(y):
            print(f"the next few numbers start with 1 {yCount}")
        if(z):
            print(f"the next few numbers end with 0 {zCount}")
        val = re.findall(r'\d{1,5}',str(temp)) 
        spl = re.split(r'\d',str(temp))
        print(spl)
        # val = re.findall(r"[1]\d[2]\d[3]\d[4]\d[5]\d[6]\d[7]\d[8]\d[9]\d[0]",str(temp))
        print(val)
        if(val):
            print("found")
        if(i > 100000):
            exit() # for ci testing 
        # Note : '-' in regex denotes range

squared(100000)

        
