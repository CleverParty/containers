from tickerScanner import yfinanceCreateContainer
import matplotlib.pyplot as plt
import datetime
import hashlib

# project imports

def createPinkfishSymbol(symbol):
    tsData = pf.fetch_timeseries(symbol)
    print(tsData.tail())

class merkle(self):
    def __init__(self,root,originalChain):
        self.root = root
        self.completeTransactions = completeTransactions
        self.prevTransactions = prevTransactions
        self.currentHash = currentHash
    
    def create(self):
        self.completeTransactions = self.prevTransactions
        self.currentHash = hashlib.sha256(currentTransaction)
        self.doubleHash = hashlib.sha256(self.currentHash)
    
def main():
    start = datetime.datetime(2020,9,12) # format :- year,month,day
    end = datetime.datetime(2020,9,16)
    tickerSymbol = yfinanceCreateContainer("AAPL")
    tickerSymbol.symbolDownloadHistoricalData(start,end)

if __name__ == "__main__" :
    main()

