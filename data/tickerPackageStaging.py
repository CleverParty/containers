from tickerScanner import yfinanceCreateContainer,altmanZScore
import matplotlib.pyplot as plt
import datetime
import hashlib
import random
import numpy as np
from yahoofinance import BalanceSheet 
# project imports

class merkleLeaf(): # extenuate this with a base class
    def __init__(self,cargo,left=None,right=None):
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def cargoHash(self):
        if(type(self.cargo) is str):
            tempHash = hashlib.sha256()
            print("String Cargo")
            print(str.encode(self.cargo))
            tempHash.update(str.encode(self.cargo))
        return (tempHash.hexdigest())
    
    def currHash(self):
        if(type(self.cargo) in range(0,len(self.cargo))):
            tempHash = hashlib.sha256()
            print("internal test structure")
        else:
            return self.cargo
        return self.left,self.right

    def __str__(self):
        print(f'the merkle node {self.cargo} has following representation')
        return(str(self.cargo))
    
    def interator(self):
        return iter(self.cargo)
    

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

def anomalyPriceDetection(data,period):
    print(data.iloc[0,0])
    index = 0
    for value in data["Close"]:
        print(f'{data.iloc[index,3]} for period {index}')
        index += 1
        rtrnVal = data.iloc[index,3]
        print(rtrnVal)
    return (index*10)

# def marketCapLive(data):
# Daily Margin Interest (Short Position) = The Daily Market Value of the Borrowed Stocks when Market Closes* Stock Loan Rate for That Stock/360.
# also the typivcal fee for Stock loan rate in the usa is 0.30% per annum, and might increase to 20-30% per annum
# when returning the stock, the loan fee and the divendends are to be paid to lender.
# 
def main():
    start = datetime.datetime(2020,7,1) # format :- year,month,day
    end = datetime.datetime(2020,9,16)
    tickerSymbol = yfinanceCreateContainer("AAPL")
    rtrnData = tickerSymbol.symbolDownloadHistoricalData(start,end)
    # rtrnAnomaly  = anomalyPriceDetection(rtrnData,3)
    node = merkle(root="teststr",prevTransactions="teststrtest",currentHash=hashlib.sha256())
    # print(f'the test string (hash) : = {rtrnHash.hexdigest()}')
    tran1 = merkleLeaf("23")
    # print(tran1.cargoHash()) # to test merkle tree implemenatation
    print(print(np.std(rtrnData["Close"])))
    hashTest = tran1.cargoHash()
    prntTest = node.doubleHash(hashTest)
    score = altmanZScore(symbol = "AAPL", sales = 265595000000, totalAssets = 338215000000, retainedEarnings = 53700000000 , rawEarnings = 1678000000, marketValueEquity = 19000000000, totalLiability = 248000000000)
    print(f"z-score :{score}")
    tran2 = merkleLeaf(str(score))
    print(tran2.cargoHash())
    tempCargo = []
    """for j in range(len(node)):
        print(j)
        tempCargo[j] = (2*cos(theta)*tempCargo[j-1]) - tempCargo[j-1]
        rtrnThetaConversion = 2*cos(theta) * tempCargo[j-1]"""
    createMerkleTreeLevel(tran1,leftCargo="21",rightCargo="3")
    # adding leaves
    valueInput = "ditto was a pidgeon"
    tran3 = merkleLeaf(valueInput)
    print(tran3.cargoHash())
    valueToBePrinted = str(tran1.cargoHash()) + str(tran2.cargoHash()) + str(tran3.cargoHash())
    print(valueToBePrinted)
    req = BalanceSheet('AAPL')
    print(req)

if __name__ == "__main__" :
    main()

