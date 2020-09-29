prices = [3,3,5,0,0,3,1,4]
defaultStartAvg = sum(prices)/len(prices)
print(defaultStartAvg)

def avgUpdater(prices,period):
    tempSum = 0
    for i in range(0,period):
        tempSum += prices[i]
    return (tempSum/period)

def sma(prices,period):
    movingAvg = []
    for i in range(0,len(prices)-period):
        avg  = sum(prices[i:i+period])/period
        movingAvg.append(avg)
    print(movingAvg)
    return movingAvg

def ema(prices,period):
    initEma = avgUpdater(prices=prices[:period],period=period)
    exponentialMovingAvg = [initEma]
    multiplier = ( 2 / period + 1 ) # smoothing constant
    for i in range(period,len(prices)):
        exponentialMovingAvg += (prices[i] - ema(prices=prices[i:period],period=period)) * multiplier + exponentialMovingAvg[i-1]
    return initEma

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
        elif( i> len(prices)-period ):
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

# if len(prices) >> 1000 or 10000, we are to use EMA rather than SMA
# because of price fluctuations in the short term
# EMA = (K * ( C - P )) + P 
# MA-crossover with 10/20/30/40/50 periods 
buySell(prices=prices,period=3)
print(f"the moving averages are {movingAverages}")
ema(prices=prices,period=3)
