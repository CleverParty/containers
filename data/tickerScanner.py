# import keras
import numpy as np 
import requests
import datetime
import finnhub 
import pandas as pd
import websocket
import pandas_datareader.data as reader
import sklearn
import yahoofinancials
# from sklearn.svm import SVR
# from keras.layers import Dense
# from keras.layers import LSTM
# from keras.layers import Dropout
import matplotlib.pyplot as plt
from matplotlib import style
import yfinance as yf 
from yahoofinance import BalanceSheet 
import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

stripped = ""

MA_PERIOD = 50 # default moving average period is set to 20 "periods"

class yfinanceCreateContainer():
    def __init__(self,symbol):
        self.symbol = symbol 
    
    def symbolHist(self,start,end,interval):
        ticker = yf.Ticker(self.symbol)
        historicalData = ticker.history(start = start,end = end, interval = interval) # calls on yfinace pkg through a wrapper
        print(historicalData)
        return historicalData
    
    def downloadSymbolHist(self,symbol,start,end):
        tickerHist = yf.download(symbol, start=start, end=end, progress=False )
        return tickerHist
    
    def symbolDownloadHistoricalData(self,start,end):
        entireData = yf.download(self.symbol,start,end)
        return entireData

def create(symbol,start,end):
    style.use('ggplot')
    df = reader.DataReader(symbol, 'yahoo', start, end)
    # sort by date
    df = df.sort_values('Date') 
    # fix the date 
    df.reset_index(inplace=True)
    stockTicker = yf.Ticker(symbol)
    return(df,stockTicker.dividends)

def ticker():
    start = datetime.datetime(2020,8,7)
    # end = datetime.datetime(2020,8,1)
    end = datetime.date.today()
    df = reader.DataReader("CRWD", 'yahoo', start, end)
    # sort by date
    df = df.sort_values('Date')
    df = df.sort_values('Date')
    # fix the date 
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    return (df)

def generateData(x):    
    r = [a/10 for a in x]
    y = np.sin(x)+np.random.uniform(-.5, .2, len(x))
    Z = np.linspace(0,101)
    print(Z)
    # created entities
    return np.array(y+r)

def on_message(ws, message):
    print(message)  

def on_close(ws):
    print("service has ended")

def on_error(ws, error):
    print(error)

def symbolsFinnhub(ws):
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
                # line = access.readline()
                line += access.readline(())
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
    ws.symbolDefault = symbolsDefault
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

def visualizeYfinanceHistoricalData(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(start="2010-01-01",  end="2020-07-21")
    fig = plotit.Figure(data=[plotit.Candlestick(x=data['Date'],high=data['High'],low=data['Low'],close=data['Close'])])  
    fig.show() 

def createPinkfishSymbol(symbol):
    tsData = pf.fetch_timeseries(symbol)
    print(tsData.tail())

def finnhubCreate(symbol): # current prices
    extracted = accessGrant()
    cargo = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token=b{extracted}'
    cargoPriceTarget = f'https://finnhub.io/api/v1/stock/price-target?symbol={symbol}&token=b{extracted}'
    cargoIPO = f'https://finnhub.io/api/v1/calendar/ipo?from=2020-01-01&to=2020-12-30&token=b{extracted}'
    r = requests.get(cargo)
    rPC = requests.get(cargoPriceTarget)
    rIPO = requests.get(cargoIPO)
    return r.json(),rPC.json(),rIPO.json()

def iexCreate(symbol):
    return (cargoDataFrame, cargoIexPricetarget)

def laggingVWAP(symbol, start, end, interval):
    ticker = yfinanceCreateContainer(symbol)
    entireDataframe = ticker.symbolHist(start=start,end=end,interval=interval)
    for i in range(0,500):
        high = entireDataframe.iloc[i,1]
        low = entireDataframe.iloc[i,2]
        close = entireDataframe.iloc[i,3]
        volume = entireDataframe.iloc[i,4]
        print(f'high = {high} , low = {low} , close = {close}, volume = {volume}')
        cumTypicalPrice = volume * ((high+low+close)/3)
        rtrnValue = cumTypicalPrice / volume # the first return value or the weighted period of VWAP, will always be equivalent to the first period's volume
        print (f'vwap value : {rtrnValue}')

    return rtrnValue

def sma(data, period):
    sumCloseThree = data["Close"][0] + data["Close"][1] + data["Close"][2] 
    avgCloseThree = sumCloseThree / period 
    return avgCloseThree

def macd(symbol, interval):
    # if sma(10/20) < sma(50/100) ... release
    # elif sma(50/100) > sma(10/20) ... aquire
    signal = False
    return signal

def maConvergenceDivergenceExponentialMovingAverage(symbol,interval):
    ema = exponentialMovingAverageScratch(symbol)
    return rtrnMacd,rtrnEma

def exponentialMovingAverageNumpy(data, window):
    multiplier = 2 / float(1+window)
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(data, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a

def exponentialMovingAverageScratch(data, window):
    ticker = yfinanceCreateContainer(symbol)
    entireDataframe = ticker.symbolHist(start=start,end=end,interval=interval)
    print(entireDataframe["High"])
    return entireDataframe["Low"]

def sentimentAnalysisScratch(symbol,start,end):
    bearOrBull = False
    return bearOrBull

def altmanZScore(symbol, totalAssets, retainedEarnings, rawEarnings, marketValueEquity, totalLiability, sales):
    # working capital 
    extracted  = accessGrant()
    r = urlopen(f'https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token=b{extracted}')
    data = r.read().decode("utf-8")
    jsonData = json.loads(data)
    workingCap = jsonData["marketCapitalization"] * 1000000 # per units
    revenueCurrent = retainedEarnings
    A = workingCap / totalAssets
    B = retainedEarnings / totalAssets # retained earnings in this step
    C = rawEarnings / totalAssets
    D = marketValueEquity / totalLiability
    E = sales / totalAssets
    zscoreFormula = ( 1.2 * A ) + ( 1.4 * B ) + ( 3.3 * C ) + ( 0.6 * D ) + ( E )
    # testing score efficacy 
    return zscoreFormula 

def bollingerBands(data,period):
    # upperBollingerBand = SMA(Typical price(trend price),number of smoothing periods) + number of standard deviations * standard deviations of last 'n' periods
    # lowerBollingerBand = SMA(Typical price(trend price),number of smoothing periods) - number of standard deviations * standard deviations of last 'n' periods
    # where, typical price = high + low + close / 3
    # band is to be a tuple of current bollinger band range
    # upperBollingerBand = sma(data,period) 
    std = sqrt(mean(abs(data.mean())))**2 # standard deviation calculation
    return std

def main():
    req = BalanceSheet('AGCO')
    start = datetime.datetime(2018,9,12) # format :- year,month,day
    end = datetime.datetime(2020,9,16)
    symbolDefault = "AGCO"
    # stripped = "b" + accessGrant()
    # client = finnhub.Client(api_key=stripped)
    # print(finnhubCreate("F"))
    print(laggingVWAP("AGCO", start=start, end=end, interval = '1mo'))
    ticker = yfinanceCreateContainer("AGCO")
    entireDataframe = ticker.symbolHist(start=start,end=end,interval="1m")
    # csv = entireDataframe.to_csv("/Users/shanmukhasurapuraju/containers/data/currentEvaluation.csv")
    print(f'entire data frame contents')
    print(entireDataframe)
    print(sma(entireDataframe,3))
    print(f'Period : {3} simple moving average gives : {sma(entireDataframe,3)}')
    score = altmanZScore(symbol = "AGCO", sales = 265595000000, totalAssets = 338215000000, retainedEarnings = 53700000000 , rawEarnings = 1678000000, marketValueEquity = 19000000000, totalLiability = 248000000000)
    print(f'Altman Z-score : {score}')
    # rtrnEmaValue = exponentialMovingAverageNumpy(entireDataframe,10)
    # visualizeYfinanceHistoricalData("F")
    # laggingVWAP("F",start,end,interval="5m")
    # entire,dividends= create("AAPL",start,end)
    # print(laggingVWAP("F",start,end))
    # print(client.company_profile(cusip='679295105'))

if __name__ == "__main__" :
    main()

# quandl.ApiConfig.api_key = contents
# data = quandl.get('WIKI/TSLA', start_date='2019-12-26', end_date='2020-7-28')
# tsla = quandl.get("EOD/TSLA")
# print(tsla.head())