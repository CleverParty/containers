import numpy as np 
import requests
import datetime
# import SVR from Sklearn

stripped = ""

# accessfile = open("access.txt","r")
with open("access.txt","r") as access:
        line = access.readline()
        cnt = 1
        while line:
            if ("finnhub" in line):
                print(f'Line {cnt}: {line.strip("finnhub=~")}')
            stripped = line.strip("finnhub=~")
            line = access.readline()
            cnt += 1
            if(cnt>2):
                break



def unixTimeStamp():
    timenow = datetime.datetime.now()
    epoch = datetime.datetime.utcfromtimestamp(0)
    value = (timenow - epoch).total_seconds() * 1000.0
    return(value,timenow)

def genWebHook():
    r = requests.post('https://finnhub.io/api/v1/webhook/add?token=', stripped , json={'event': 'earnings', 'symbol': 'TSLA'})
    res = r.json() # limit 30/sec base
    print(res)
    webhook_id = res['id']
    # List webhook
    r = requests.get('https://finnhub.io/api/v1/webhook/list?token=bt0rj6748v6ptb8skvpg')
    res = r.json()
    print(res)

def main():
    utc , _ = unixTimeStamp()
    print(utc)
    # genWebHook()


if __name__ == "__main__":
    main()

# quandl.ApiConfig.api_key = contents
# data = quandl.get('WIKI/TSLA', start_date='2019-12-26', end_date='2020-7-28')
# tsla = quandl.get("EOD/TSLA")
# print(tsla.head())