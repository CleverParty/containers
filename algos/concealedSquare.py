import os,math
import re

stringtocompare = "1_2_3_4_5_6_7_8_9_0"

def squared(num):
    temp = 1
    for i in range(0,num):
        temp = i*i
        yCount = 0
        zCount = 0
        y = re.findall(r"\b1", str(temp))
        z = re.findall(r"0\b", str(temp))
        if(y):
            yCount += 1
        if(z):
            zCount += 1
        regexcompare = re.compile(r'\b1_\b2_\b3_\b4_\b5_\b6_\b7_\b8_\b9_\Z0')
        # print(x)
        # '-' in regex denotes range
        if(y and z and regexcompare):
            # continue
            print(f'the value starting with 1 and ending with 0 is {i} and the square is {temp} and {yCount} and {zCount}')
            # x = re.search("^The.*Spain$", txt)
    print (f'y = {yCount} and z = {zCount}')

squared(10000)

        
