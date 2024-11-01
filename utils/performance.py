import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd

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

stock_symbol = 'TCS.NS' #USe '.NS' for nifty and '.BO' for sensex

# Fetch real-time data
real_time_data = get_realtime_data(stock_symbol)
print("Real-Time Data:\n", real_time_data)

# Fetch 3-month historical data
historical_data = get_historical_data(stock_symbol).reset_index()
print("\nHistorical Data (3 Months):\n", historical_data)

historical_data['Date'] = pd.to_datetime(historical_data['Date'])
historical_data.set_index('Date', inplace=True)
historical_data['High_Low_STD'] = historical_data[['High', 'Low']].std(axis=1)
# Calculate the 20-day moving average of the Close price
historical_data['SMA_20'] = historical_data['Close'].rolling(window=20).mean()

# Calculate the standard deviation of the Close price over a 20-day window
historical_data['STD_20'] = historical_data['Close'].rolling(window=20).std()

# Calculate the Bollinger Bands
historical_data['Upper_Band'] = historical_data['SMA_20'] + (historical_data['STD_20'] * 2)
historical_data['Lower_Band'] = historical_data['SMA_20'] - (historical_data['STD_20'] * 2)

# Plot the Close price and Bollinger Bands
plt.figure(figsize=(12, 6))
plt.plot(historical_data.index, historical_data['Close'], label='Close', color='blue')
plt.plot(historical_data.index, historical_data['SMA_20'], label='20-Day SMA', color='orange')
plt.plot(historical_data.index, historical_data['Upper_Band'], label='Upper Bollinger Band', color='green', linestyle='--')
plt.plot(historical_data.index, historical_data['Lower_Band'], label='Lower Bollinger Band', color='red', linestyle='--')

plt.fill_between(historical_data.index, historical_data['Upper_Band'], historical_data['Lower_Band'], color='gray', alpha=0.3)
plt.title('Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()