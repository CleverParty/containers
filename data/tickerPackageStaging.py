from tickerScanner import yfinanceCreateContainer
import matplotlib.pyplot as plt
import datetime
import hashlib
import random

# project imports

class merkle:
    def __init__(self,root,prevTransactions,currentHash):
        self.root = root
        self.completeTransactions = 0
        self.prevTransactions = prevTransactions
        self.currentHash = hashlib.sha256()
    
    def create(self):
        self.completeTransactions = self.prevTransactions
        self.currentHash = hashlib.sha256(currentTransaction)
        self.doubleHash = hashlib.sha256(self.currentHash)
    
    def testNodeCreation(self):
        self.currentHash = hashlib.sha256()
        self.currentHash.update(b"node has been hashed")
        print(self.currentHash.hexdigest())
        return self.currentHash
    
def main():
    start = datetime.datetime(2020,9,12) # format :- year,month,day
    end = datetime.datetime(2020,9,16)
    tickerSymbol = yfinanceCreateContainer("AAPL")
    tickerSymbol.symbolDownloadHistoricalData(start,end)
    node = merkle(root="teststr",prevTransactions="teststrtest",currentHash=hashlib.sha256())
    node.testNodeCreation()
    rtrnHash = hashlib.sha256()
    rtrnHash.update(b"astoadsasasd")
    print(rtrnHash.hexdigest())

if __name__ == "__main__" :
    main()

