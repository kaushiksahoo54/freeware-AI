#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
from datetime import datetime, timedelta


# In[5]:


#real_time data for stock
def get_realtime_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    real_time_data = stock.history(period="1d", interval="1m") 
    return real_time_data.tail()  

#3month data for stock
def get_historical_data(stock_symbol, months=3):
    stock = yf.Ticker(stock_symbol)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=months * 30)  
    historical_data = stock.history(start=start_date, end=end_date)
    return historical_data


# In[6]:


if __name__ == "__main__":
    stock_symbol = 'TCS.NS' #USe '.NS' for nifty and '.BO' for sensex
    
    # Fetch real-time data
    real_time_data = get_realtime_data(stock_symbol)
    print("Real-Time Data:\n", real_time_data)
    
    # Fetch 3-month historical data
    historical_data = get_historical_data(stock_symbol)
    print("\nHistorical Data (3 Months):\n", historical_data)


# In[ ]:




