from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
my_url = urlopen('https://www.portfoliovisualizer.com/historical-asset-class-returns')
# Read the url into BeautifulSoup
soup = BeautifulSoup(my_url.read(), 'lxml')
# Select just the column names
col_names = soup.tr
# Split Column names
col_names = col_names.text.split('\n')
col_names = list(filter(None,col_names))
data = []
for t in soup.find_all('td'):
    data.append(t.text)
    
del data[-1] # this is essential to re-shape the array
df_returns = pd.DataFrame(np.array(data).reshape(49,40), columns=col_names)
df_returns.set_index('Year', inplace=True)
# df_returns.to_csv('hist.csv') use this command when generating the csv file
print(df_returns)