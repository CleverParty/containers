prices = [3,3,5,0,0,3,1,4]

def avgUpdater(index,prices):
    avg = prices[index] + prices[index] + prices[index - 1]

def sma(prices,period):
    defaultStartAvg = sum(prices)/len(prices)
    print(defaultStartAvg)
    movingAvg = []
    for i in range(0,len(prices)-2):
        avg  = (prices[i] + prices[i+1] + prices[i+2])/period
        movingAvg.append(avg)
    print(movingAvg)
    return movingAvg
        

# EMA = (K * ( C - P )) + P 
sma(prices=prices,period=3)
print((prices[0]+prices[1]+prices[2])/3)

