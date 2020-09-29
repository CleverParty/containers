prices = [3,3,5,0,0,3,1,4]
defaultStartAvg = sum(prices)/len(prices)
print(defaultStartAvg)

def avgUpdater(index,prices,period):
    return((prices[index] + prices[index] + prices[index - 1])/period)

def sma(prices,period):
    movingAvg = []
    for i in range(0,len(prices)-2):
        avg  = (prices[i] + prices[i+1] + prices[i+2])/period
        movingAvg.append(avg)
    print(movingAvg)
    return movingAvg

movingAverages = sma(prices=prices,period=3)
print(movingAverages)
def buySell(prices,period):
    signals = []
    j=0
    for i in range(0,len(prices)):
        if( i<=period and prices[i] < defaultStartAvg):
            signals.append("B")
            print(f'with price:{prices[i]}, we are to "B"')
        elif( i>period and prices[i] > movingAverages[j]):
            signals.append("S")
            j+=1
            print(f'with price:{prices[i]}, we are to "S"')
        else:
            signals.append("S")
        print(signals)
    return signals

# if len(prices) >> 1000 or 10000, we are to use EMA rather than SMA
# because of price fluctuations in the short term
# EMA = (K * ( C - P )) + P 
buySell(prices=prices,period=3)
