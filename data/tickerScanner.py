import quandl
import numpy as np 
import requests
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

stripped = ""

accessfile = open("access.txt","r")
with open("access.txt","r") as access:
        line = access.readline()
        cnt = 1
        while line:
            if ("finnhub" in line):
                print(f'Line {cnt}: {line.strip("finnhub=~")}')
            stripped = line.strip("finnhub=~")
            line = access.readline()
            cnt += 1
            if(cnt>2):
                break

r = requests.get('https://finnhub.io/api/v1/company-news?symbol=TSLA&from=2020-04-30&to=2020-05-01&token=',stripped)
print(r.json())
print(stripped)
accessfile.close()
# quandl.ApiConfig.api_key = contents
# data = quandl.get('WIKI/TSLA', start_date='2019-12-26', end_date='2020-7-28')

# tsla = quandl.get("EOD/TSLA")
# print(tsla.head())