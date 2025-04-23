import pandas as pd

data = pd.read_csv('Screener\excel\Companies List for Screener Watchlist(Sheet1).csv',header=None)

d = data.iloc[1:,0].to_list()
data_50 = []
for i in range(0,len(d),50):
    data_50.append(d[i:i+50])
