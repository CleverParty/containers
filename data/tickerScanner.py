import keras
import numpy as np 
import requests
import datetime
import finnhub 
import pandas as pd
import websocket
import pandas_datareader.data as reader
import sklearn
from sklearn.svm import SVR
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import matplotlib.pyplot as plt
from matplotlib import style

stripped = ""

def ticker():
    start = datetime.datetime(2020,3,11)
    # end = datetime.datetime(2020,8,1)
    end = datetime.date.today()
    df = reader.DataReader("EBAY", 'yahoo', start, end)
    # sort by date
    df = df.sort_values('Date')
    df = df.sort_values('Date')
    # fix the date 
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    print(df.head())

def genData(x):    
    r = [a/10 for a in x]
    y = np.sin(x)+np.random.uniform(-.5, .2, len(x))
    return np.array(y+r)

def on_message(ws, message):
    print(message)  

def on_close(ws):
    print("service has ended")

def on_error(ws, error):
    print(error)

def symbolsFinn(ws):
    ws.send('{"type":"subscribe","symbol":"OKTA"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

def accessGrant():
    # adding noise to the data process:
    # data[::5] += 3 * (0.5 - np.random.rand(5))
    # accessfile = open("access.txt","r")
    with open("access.txt","r") as access:
            line = access.readline()
            cnt = 1
            while line:
                # if ("finnhub" in line):
                #     print(f'Line {cnt}: {line.strip("finnhub=")}')
                stripped = line.strip("finnhub=")
                line = access.readline()
                cnt += 1
                if(cnt>2):
                    break
    return stripped

def getTickerNews(category):
    extracted = accessGrant()
    cargo = f'https://finnhub.io/api/v1/news?category={category}&token=b{extracted}'
    r = requests.get(cargo)
    print(f'General news from finnhub')
    print(r.json())

def unixTimeStamp():
    timenow = datetime.datetime.now()
    epoch = datetime.datetime.utcfromtimestamp(0)
    value = (timenow - epoch).total_seconds() * 1000.0
    return(value,timenow)

def genWebHook():
    # r = requests.post('https://finnhub.io/api/v1/webhook/add?token=', stripped , json={'event': event, 'symbol': symbol})
    # res = r.json() # limit 30/sec base
    websocket.enableTrace(True)
    searchStr = "wss://ws.finnhub.io?token=b" + extracted
    ws = websocket.WebSocketApp(searchStr,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.symbolsFinn = symbolsFinn
    # ws.run_forever()

def workaround_LSTM():
    # x_train , y_train, x_test , y_train = train_test_split(date,y)
    # y_pred = svrTickerRBF.predict()
    n = 100
    x = [i/100 for i in range(n)]
    y = genData(x)
    x = np.array(x).reshape(-1,1)
    plt.scatter(x, y, s=5, color="green")
    plt.show()

def main():
    client = finnhub.Client(api_key=stripped)
    print(client.company_profile(cusip='679295105'))

if __name__ == "__main__":
    main()



# quandl.ApiConfig.api_key = contents
# data = quandl.get('WIKI/TSLA', start_date='2019-12-26', end_date='2020-7-28')
# tsla = quandl.get("EOD/TSLA")
# print(tsla.head())