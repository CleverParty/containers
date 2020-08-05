import os,math
import re

stringtocompare = "1_2_3_4_5_6_7_8_9_0"

def squared(num):
    temp = 1
    for i in range(0,num):
        temp = i*i
        y = re.findall(r"\b1", str(temp))
        z = re.findall(r"0\b", str(temp))
        # print(x)
        if(y and z):
            print(f'the value starting with 1 and ending with 0 is {i}')
            # x = re.search("^The.*Spain$", txt)

squared(100000000)

        
