from tickerScanner import yfinanceCreateContainer
import matplotlib.pyplot as plt
import datetime
import hashlib
import random

# project imports

class merkle:
    def __init__(self,root,prevTransactions):
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
    rtrnHash = hashlib.sha256()
    rtrnHash.update(b'hash initialised')
    print(rtrnHash.digest())
    print(rtrnHash.digest_size)

if __name__ == "__main__" :
    main()

