from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader
from pandas_datareader import data
import yfinance as yf

print(pandas_datareader.__version__)

def SandP():
    url = urlopen("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(url.read(), 'lxml')
    tbody = soup.tbody
    tr = tbody.find_all('tr')
    data = []
    for t in tr:
        data.append(t.text.split('\n'))
    raw_df = pd.DataFrame(data)
    raw_df.columns = raw_df.iloc[0,:]
    raw_df = raw_df.iloc[1:,:]
    sectors = raw_df.groupby('GICS Sector').count().iloc[:,0].sort_values()
    sectors.plot(kind='pie')
    plt.ylabel('Number of Constituents')
    plt.xlabel('Markets', fontsize=2)
    plt.title('Sector Constituents in S&P 500 as of 2019')
    # plt.show()
    rtrn = raw_df.to_numpy()
    return (rtrn)

def HistAssetReturns():
    my_url = urlopen('https://www.portfoliovisualizer.com/historical-asset-class-returns')
    soup = BeautifulSoup(my_url.read(), 'lxml')
    col_names = soup.tr
    col_names = col_names.text.split('\n')
    col_names = list(filter(None,col_names))
    data = []
    for t in soup.find_all('td'):
        data.append(t.text)
    del data[-1] # this is essential to re-shape the array
    df_returns = pd.DataFrame(np.array(data).reshape(49,40), columns=col_names)
    df_returns.set_index('Year', inplace=True)
    # df_returns.to_csv('hist.csv') use this command when generating the csv file
    return (df_returns)

def liveDataYahooData():
    start_date = '1990-01-01'
    end_date = '2019-02-01'
    ticker = 'AMZN' # change ticker to test
    datastock = data.get_data_yahoo(ticker, start_date, end_date)
    # datastock.head()
    # data['Adj Close'].plot()
    # plt.show()
    return(datastock.head())

def liveDataYFinance():
    amzn = yf.Ticker("AMZN")
    pb = amzn.info['priceToBook']
    print(amzn.actions)
    print('Price to Book Ratio is: %.2f' % pb)
    return(pb)

datafromFunc = HistAssetReturns()
print(datafromFunc)
# SandP()
# HistAssetReturns()
# liveDataYahooData()
# liveDataYFinance()
# companyData = liveDataYFinance()
# print(companyData)