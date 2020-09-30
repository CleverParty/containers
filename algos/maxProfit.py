prices = [3,4,2,0,1,4,3,2,5]
defaultStartAvg = sum(prices)/len(prices)
print(defaultStartAvg)

def avgUpdater(prices,period):
    tempSum = 0
    for i in range(0,period):
        tempSum += prices[i]
    return int(tempSum/period)

def sma(prices,period):
    movingAvg = []
    for i in range(0,len(prices)-period):
        avg  = sum(prices[i:i+period])/period
        movingAvg.append(avg)
    print(movingAvg)
    return movingAvg

def ema(prices,period):
    initEma = avgUpdater(prices=prices,period=period)
    exponentialMovingAvg = [initEma]
    multiplier = 2 / ( period + 1 ) # smoothing constant
    j = 1
    for i in range(period,len(prices)):
        exponentialMovingAvg.append(((prices[i] - exponentialMovingAvg[j-1]) * multiplier) + exponentialMovingAvg[j-1])
        j += 1
    return exponentialMovingAvg

movingAverages = sma(prices=prices,period=3)
print(movingAverages)
def buySell(prices,period):
    signals = []
    j=0
    for i in range(0,len(prices)):
        if( i<=period ):
            if( prices[i] < defaultStartAvg ):
                signals.append("B")
                print(f'with price:{prices[i]}, with current average : {defaultStartAvg}  we are to "B"')
            else:
                signals.append("S")
        elif( i > len(prices)-period ):
            if(prices[i] > movingAverages[j]):
                signals.append("S")
                print(f'with price:{prices[i]}, with moving average : {movingAverages[j]} we are to "S"')
                j+=1
            else:
                signals.append("S")
                j+=1
        else:
            signals.append("S")
        print(signals)
    return signals

def profiCalc(prices,period):
    tempDiff = []
    diff = 0
    for i in range(0,len(prices)):
        for j in range(i,len(prices)):
            print(i,j)
            diff = abs(prices[j]-prices[i])
            print(f"for prices = {prices[i]} and {prices[j]} , the profit would be : {diff}")
            tempDiff.append(diff)
    print(max(tempDiff))
    return tempDiff
# if len(prices) >> 1000 or 10000, we are to use EMA rather than SMA
# because of price fluctuations in the short term
# EMA = (K * ( C - P )) + P 
# MA-crossover with 10/20/30/40/50 periods 
buySell(prices=prices,period=3)
print(f"the moving averages are {movingAverages}")
ema(prices=prices,period=3)
profiCalc(prices=prices,period=3)
