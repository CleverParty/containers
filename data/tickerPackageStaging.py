from tickerScanner import yfinanceCreateContainer
import matplotlib.pyplot as plt
import datetime
import hashlib
import random

# project imports

class merkleLeaf():
    def __init__(self,cargo,left=None,right=None):
        tempHash = hashlib.sha256()
        if(type(cargo) is str):
            print("String")
        tempHash.update(str.encode(cargo))
        print(tempHash.hexdigest())
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        print(f'the merkle node {self.cargo} has following representation')
        return(str(self.cargo))
    

class merkle():
    def __init__(self,root,prevTransactions,currentHash,status=None):
        self.root = root
        self.completeTransactions = 0
        self.prevTransactions = prevTransactions
        self.currentHash = hashlib.sha256()
        self.status = None
    
    def create(self):
        self.completeTransactions = self.prevTransactions
        self.currentHash = hashlib.sha256(currentTransaction)
    
    def doubleHash(self):
        self.status = hashlib.sha256(b"two-level hash")
        self.status.update(b"node has been hashed")
        print(self.status.hexdigest())
        self.currentHash = hashlib.sha256()
        return (self.currentHash)
    
def main():
    start = datetime.datetime(2020,9,12) # format :- year,month,day
    end = datetime.datetime(2020,9,16)
    tickerSymbol = yfinanceCreateContainer("AAPL")
    tickerSymbol.symbolDownloadHistoricalData(start,end)
    node = merkle(root="teststr",prevTransactions="teststrtest",currentHash=hashlib.sha256())
    node.doubleHash()
    rtrnHash = hashlib.sha256()
    rtrnHash.update(b"the test string")
    print(f'the test string (hash) : = {rtrnHash.hexdigest()}')
    tran1 = merkleLeaf("23")
    print(tran1)


if __name__ == "__main__" :
    main()

