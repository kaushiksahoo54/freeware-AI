import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
from utils.performance import get_historical_data

# Load configuration
with open("./config.json") as f:
    config = json.load(f)
stock_symbol = config.get("stock_symbol", "AAPL")

def calculate_indicators(df):
    """
    Adds ATR, SMA, EMA, and RSI columns to the DataFrame.

    Args:
        df (DataFrame): DataFrame containing stock OHLC data.
    
    Returns:
        DataFrame: DataFrame with additional ATR, SMA, EMA, and RSI columns.
    """
    df['Previous_Close'] = df['Close'].shift(1)
    
    # True Range (TR) and Average True Range (ATR)
    df['TR'] = np.maximum(
        df['High'] - df['Low'],
        np.maximum(
            abs(df['High'] - df['Previous_Close']),
            abs(df['Low'] - df['Previous_Close'])
        )
    )
    df['ATR'] = df['TR'].rolling(window=14).mean()

    # Simple Moving Average (SMA) and Exponential Moving Average (EMA)
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()

    # RSI Calculation
    delta = df['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df

def prepare_candlestick_data(df):
    """
    Prepares data for candlestick chart plotting.

    Args:
        df (DataFrame): DataFrame with stock OHLC data.

    Returns:
        np.array: Data formatted for candlestick_ohlc plotting.
    """
    df['Date_num'] = mdates.date2num(df.index)
    ohlc_data = df[['Date_num', 'Open', 'High', 'Low', 'Close']].dropna().values
    return ohlc_data

def plot_stock_data(df):
    """
    Plots candlestick chart with ATR, SMA, EMA, and RSI.

    Args:
        df (DataFrame): DataFrame with calculated indicators.
    """
    ohlc_data = prepare_candlestick_data(df)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
    
    # Candlestick chart with SMA and EMA
    candlestick_ohlc(ax1, ohlc_data, width=0.6, colorup='green', colordown='red', alpha=0.8)
    ax1.plot(df.index, df['SMA_20'], label='20-Day SMA', color='orange', linewidth=1.5)
    ax1.plot(df.index, df['EMA_20'], label='20-Day EMA', color='blue', linestyle='--', linewidth=1.5)
    ax1.set_ylabel('Price')
    ax1.set_title('Stock Price with 20-Day SMA, EMA, and ATR')
    ax1.xaxis_date()
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.grid(True)
    ax1.legend(loc='upper left')
    
    # ATR line on a secondary y-axis in ax1
    ax3 = ax1.twinx()
    ax3.plot(df.index, df['ATR'], label='ATR (14-day)', color='purple', linewidth=1.5)
    ax3.set_ylabel('ATR', color='purple')
    ax3.legend(loc='upper right')
    
    # RSI plot in a separate subplot
    ax2.plot(df.index, df['RSI'], label='RSI (14-day)', color='brown', linewidth=1.5)
    ax2.axhline(70, color='red', linestyle='--', linewidth=0.7)  # Overbought line
    ax2.axhline(30, color='green', linestyle='--', linewidth=0.7)  # Oversold line
    ax2.set_ylabel('RSI')
    ax2.set_xlabel('Date')
    ax2.legend(loc='upper left')
    ax2.grid(True)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Fetch historical data and calculate indicators
    historical_data = get_historical_data(stock_symbol).reset_index()
    df = pd.DataFrame(historical_data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Calculate indicators
    df = calculate_indicators(df)
    
    # Plotting
    plot_stock_data(df)

# Run main function
if __name__ == "__main__":
    main()
