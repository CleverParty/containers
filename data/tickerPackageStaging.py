from tickerScanner import yfinanceCreateContainer,altmanZScore
import matplotlib.pyplot as plt
import datetime
import hashlib
import random

# project imports

class merkleLeaf():
    def __init__(self,cargo,left=None,right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def cargoHash(self):
        if(type(self.cargo) is str):
            tempHash = hashlib.sha256()
            print("String Cargo")
            tempHash.update(str.encode(self.cargo))
        return (tempHash.hexdigest())

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
        self.cargo = ""
    
    def create(self):
        self.completeTransactions = self.prevTransactions
        self.currentHash = hashlib.sha256(currentTransaction)
    
    def doubleHash(self,cargo): # Double hashing within the inner node itself for easier access to cargo
        self.status = hashlib.sha256(str.encode(self.cargo))
        print(self.status.hexdigest())
        self.currentHash = hashlib.sha256()
        return (self.currentHash)

def createMerkleTreeLevel(root,leftCargo,rightCargo):
    merkleCargo = root.cargo
    leftElement = merkleLeaf(cargo = leftCargo)         
    rightElement = merkleLeaf(cargo = rightCargo)
    tempLeftHash = leftElement.cargoHash()
    tempRightHash = rightElement.cargoHash()

    print(f"left hashed cargo : {tempLeftHash} and right hashed cargo : {tempRightHash}")
    return True

    
def main():
    start = datetime.datetime(2020,9,12) # format :- year,month,day
    end = datetime.datetime(2020,9,16)
    tickerSymbol = yfinanceCreateContainer("AAPL")
    tickerSymbol.symbolDownloadHistoricalData(start,end)
    node = merkle(root="teststr",prevTransactions="teststrtest",currentHash=hashlib.sha256())
    # print(f'the test string (hash) : = {rtrnHash.hexdigest()}')
    tran1 = merkleLeaf("23")
    print(tran1.cargoHash())
    hashTest = tran1.cargoHash()
    prntTest = node.doubleHash(hashTest)
    score = altmanZScore(symbol = "AAPL", sales = 265595000000, totalAssets = 338215000000, retainedEarnings = 53700000000 , rawEarnings = 1678000000, marketValueEquity = 19000000000, totalLiability = 248000000000)
    print(f"z-score :{score}")
    tran2 = merkleLeaf(str(score))
    print(tran2.cargoHash())
    createMerkleTreeLevel(tran1,leftCargo="2",rightCargo="3")

if __name__ == "__main__" :
    main()

