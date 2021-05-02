import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import  adfuller
import statsmodels as sm
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as smi
from statsmodels.graphics.tsaplots import plot_pacf
df=pd.read_csv('/Users/yashjain/Downloads/Project/champagne.csv')
df.columns=['Month','Sales']
df['Month']=pd.to_datetime(df['Month'])
df.set_index("Month",inplace=True)
plt.subplot(231)
df.plot()
def adfuller_test(sales):
    result=adfuller(sales)
    labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
    for value,label in zip(result,labels):
        print(label+' : '+str(value) )
    if result[1] <= 0.05:
        print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
    else:
        print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")
adfuller_test(df['Sales'])
df["Sales First Difference"]=(df["Sales"] )-(df["Sales"].shift(1))
df["Sales Seasonal Difference"]=(df["Sales"] )-(df["Sales"].shift(12))
adfuller_test(df["Sales First Difference"].dropna())
fig=plt.figure(figsize=(12,8))
plt.subplot(232)
fig=sm.graphics.tsaplots.acf(df["Sales Seasonal Difference"].dropna(),nlags=40)
plt.plot(fig)
plt.subplot(233)
fig=sm.graphics.tsaplots.pacf(df["Sales Seasonal Difference"].dropna(),nlags=40)
plt.plot(fig)
model=ARIMA(df['Sales'],order=(1,1,1))
model_fit=model.fit()
print (model_fit.summary)
df['forecast']=model_fit.predict(start=90,end=103,dynamic=True)
plt.subplot(234)
plt.plot(df[["Sales",'forecast']])
model=smi.tsa.statespace.SARIMAX(df["Sales"],orde=(1,1,1),seasonal_order=(1,1,1,12))
results =model.fit()
print (results.summary)
df['forecast']=results.predict(start=90,end=103,dynamic=True)
plt.subplot(235)
plt.plot(df[['Sales','forecast']])
plt.show()

#/Users/yashjain/Library/Preferences/PyCharmCE2019.2/scratches/Data Science/ARIMA.py
