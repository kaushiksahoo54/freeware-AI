import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from performance import get_historical_data
import json
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

with open("./config.json") as f:
    config = json.load(f)
stock_symbol = config["stock_symbol"]
historical_data = get_historical_data(stock_symbol).reset_index()

df = pd.DataFrame(historical_data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Calculate True Range (TR)
df['Previous_Close'] = df['Close'].shift(1)
df['TR'] = np.maximum(
    df['High'] - df['Low'],
    np.maximum(
        abs(df['High'] - df['Previous_Close']),
        abs(df['Low'] - df['Previous_Close'])
    )
)

# Calculate Average True Range (ATR) with a 14-day window
df['ATR'] = df['TR'].rolling(window=14).mean()

# candlestick chart
df['Date_num'] = mdates.date2num(df.index)
ohlc = df[['Date_num', 'Open', 'High', 'Low', 'Close']].dropna().values

fig, ax1 = plt.subplots(figsize=(12, 6))

# Candlestick chart
candlestick_ohlc(ax1, ohlc, width=0.6, colorup='green', colordown='red', alpha=0.8)
ax1.set_ylabel('Price')
ax1.set_title('Stock Price with ATR')
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.grid(True)


ax2 = ax1.twinx()
ax2.plot(df.index, df['ATR'], label='Volatility', color='blue', linewidth=1)
ax2.set_ylabel('ATR', color='purple')
ax2.legend(loc='upper right')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()