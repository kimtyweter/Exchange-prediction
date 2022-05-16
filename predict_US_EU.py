import twder
import pandas as pd

# Finding USD dollar value during last six months
us_6month = twder.past_six_month('USD')

# Coins
coin = twder.currencies() 
df1 = pd.DataFrame()
time = []
for i in twder.past_six_month(coin[0]):
    time.append(i[0])

df1['Time'] = time
for i in range(0,len(coin)):
    b = []
    a = twder.past_six_month(coin[i])
    for j in a:
        b.append(j[1])
    df1[coin[i]] = b


# import package for prediction: linear regression
from statsmodels.formula.api import ols
import pandas.util.testing as tm


# train data
train = df1.iloc[1:,1:].astype(float)

# predict data
predict = df1.iloc[0:1,1:].astype(float)

# Model: linear regression
model = ols('USD ~ HKD + GBP + AUD + CAD + SGD + CHF + JPY + SEK + NZD + THB + PHP + IDR + EUR + KRW + VND + MYR + CNY', data = train).fit() 
model.summary()


model1 = ols('EUR ~ HKD + GBP + AUD + CAD + SGD + CHF + JPY + SEK + NZD + THB + PHP + IDR + USD + KRW + VND + MYR + CNY', data = train).fit() 
model1.summary()

predictions_USA = model.predict(predict)
predictions_EUR = model1.predict(predict)

out = pd.DataFrame({'USA' : predictions_USA.round(2), 'EUR' : predictions_EUR.round(2)})
out = out.style.hide_index()

df1.to_excel('exchange.xlsx', index = 0)

out.to_excel('prediction.xlsx', index = 0)