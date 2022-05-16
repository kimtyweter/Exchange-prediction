#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import twder
import pandas as pd


# In[ ]:


# 現有幣別
# twder.currencies() 


# In[ ]:


# 查詢指定貨幣昨日全部報價
# twder.past_day('USD')


# In[ ]:


# current = twder.past_day('USD')[-1][1]


# In[ ]:


# 查詢指定貨幣過去半年每天收盤價
us_6month = twder.past_six_month('USD')


# In[ ]:





# In[ ]:


# twder.past_six_month('USD') [0][1]


# In[ ]:


# 查詢指定貨幣於指定月份每天收盤價

# twder.specify_month('USD', 2019, 10) 


# # For loop

# In[ ]:


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
df1


# # Model

# In[ ]:


from statsmodels.formula.api import ols
import pandas.util.testing as tm


# In[ ]:


# train data
train = df1.iloc[1:,1:].astype(float)

# predict data
predict = df1.iloc[0:1,1:].astype(float)


# In[ ]:


train


# In[ ]:


model = ols('USD ~ HKD + GBP + AUD + CAD + SGD + CHF + JPY + SEK + NZD + THB + PHP + IDR + EUR + KRW + VND + MYR + CNY', data = train).fit() 
model.summary()


# In[ ]:


model1 = ols('EUR ~ HKD + GBP + AUD + CAD + SGD + CHF + JPY + SEK + NZD + THB + PHP + IDR + USD + KRW + VND + MYR + CNY', data = train).fit() 
model1.summary()


# In[ ]:


predictions_USA = model.predict(predict)


# In[ ]:


predictions_EUR = model1.predict(predict)


# In[ ]:


out = pd.DataFrame({'USA' : predictions_USA.round(2), 'EUR' : predictions_EUR.round(2)})
out = out.style.hide_index()
out


# In[ ]:


df1.to_excel('exchange.xlsx', index = 0)


# In[ ]:


out.to_excel('prediction.xlsx', index = 0)


# In[ ]:


# 查詢指定貨幣昨日全部報價


# In[ ]:




