import keras
import numpy as np 
import requests
import datetime
import pandas as pd
import pandas_datareader.data as reader
from sklearn.svm import SVR
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2020,3,11)
# end = datetime.datetime(2020,8,1)
end = datetime.date.today()
df = reader.DataReader("AMZN", 'yahoo', start, end)
# sort by date
df = df.sort_values('Date')
df = df.sort_values('Date')

# fix the date 
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)

def accessGrant():
    stripped = ""
    # adding noise to the data process:
    # data[::5] += 3 * (0.5 - np.random.rand(5))
    # accessfile = open("access.txt","r")
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

def unixTimeStamp():
    timenow = datetime.datetime.now()
    epoch = datetime.datetime.utcfromtimestamp(0)
    value = (timenow - epoch).total_seconds() * 1000.0
    return(value,timenow)

def genWebHook():
    r = requests.post('https://finnhub.io/api/v1/webhook/add?token=', stripped , json={'event': 'earnings', 'symbol': 'TSLA'})
    res = r.json() # limit 30/sec base
    print(res)

def main():
    utc , _ = unixTimeStamp()
    print(utc)
    print(df)
    # genWebHook()
if __name__ == "__main__":
    main()

# quandl.ApiConfig.api_key = contents
# data = quandl.get('WIKI/TSLA', start_date='2019-12-26', end_date='2020-7-28')
# tsla = quandl.get("EOD/TSLA")
# print(tsla.head())