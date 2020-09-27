from tickerScanner import yfinanceCreateContainer
import matplotlib.pyplot as plt
import datetime
# project imports

def createPinkfishSymbol(symbol):
    tsData = pf.fetch_timeseries(symbol)
    print(tsData.tail())

def main():
    start = datetime.datetime(2020,9,12) # format :- year,month,day
    end = datetime.datetime(2020,9,16)
    tickerSymbol = yfinanceCreateContainer("AAPL")
    tickerSymbol.symbolDownloadHistoricalData(start,end)

if __name__ == "__main__" :
    main()

