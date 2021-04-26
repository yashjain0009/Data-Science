import matplotlib.pyplot as plt
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
DAX = web.DataReader(name='ITC.NS', data_source='yahoo', start='2010-1-1')
#print DAX.info()
#DAX['Close'].plot(figsize=(8, 5))
df=pd.DataFrame(DAX)
#df["Date"]=pd.date_range('2010-1-1',periods=len(df.index),freq='B')

#plt.plot(df["Date"],df["Adj Close"])
DAX['Close'].plot()
DAX['Return'] = np.log(DAX['Close'] / DAX['Close'].shift(1))
df['42d']=df['Close'].rolling(window=42).mean()
df['252d']=df['Close'].rolling(window=252).mean()
df['Mov_Vol']=df['Return'].rolling(window=252).std()*math.sqrt(252)
print(df.columns)
#print (df['42d'])
#print DAX[['Close', '42d','252d']]
#DAX[['Close', '42d','252d']].plot(figsize=(8, 5))
#DAX[['Close','Mov_Vol','Return']].plot(subplots=True)
plt.grid(True)
#reg=np.polyfit(DAX["Date"],DAX["close"],deg=7)
#ry=np.polyval(reg,DAX["Date"])
#plt.plot(DAX["Date"],DAX["close"],'b')
#plt.plot(DAX["Date"],ry,'r')

#DAX[['Close', 'Return']].plot(subplots=True, style='b', figsize=(8, 5))
plt.show()
#/Users/yashjain/Downloads/Data/es.txt
#shift operation figure out
