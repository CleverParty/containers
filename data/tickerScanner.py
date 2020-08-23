import quandl
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

accessfile = open("access.txt","r")
with open("access.txt","r") as access:
    while access:
        line = access.readline()
        cnt = 1
        while line:
            if ("finnhub" in line):
                print("Line {}: {}".format(cnt, line.strip()))
            line = access.readline()
            cnt += 1
accessfile.close()
contents = accessfile.read()
# quandl.ApiConfig.api_key = contents
# data = quandl.get('WIKI/TSLA', start_date='2019-12-26', end_date='2020-7-28')
print(contents)




import requests
r = requests.get('https://finnhub.io/api/v1/covid19/us?token=bt0rj6748v6ptb8skvpg')
print(r.json())
# tsla = quandl.get("EOD/TSLA")
# print(tsla.head())