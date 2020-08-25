import keras
import numpy as np 
import pandas as pd
import requests
import datetime
from sklearn.svm import SVR
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import pandas_datareader.data as reader
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
start = datetime.datetime(2020,3,11)
end = datetime.datetime(2020,8,1)
# end = datetime.date.today()
df = reader.DataReader("TSLA", 'yahoo', start, end)
print(df)

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
    # genWebHook()
    # reading dataset:
    dataset = pd.read_csv('Position_Salaries.csv')
    X = dataset.iloc[:, 1:2].values
    Y = dataset.iloc[:, 2].values

if __name__ == "__main__":
    main()

# quandl.ApiConfig.api_key = contents
# data = quandl.get('WIKI/TSLA', start_date='2019-12-26', end_date='2020-7-28')
# tsla = quandl.get("EOD/TSLA")
# print(tsla.head())