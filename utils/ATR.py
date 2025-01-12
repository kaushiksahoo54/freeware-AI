import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
from Bollinger import get_historical_data, p_main

# Load the configuration file
with open("./config.json") as f:
    config = json.load(f)

stock_symbol = config["stock_symbol"]

# Fetch historical data
historical_data = get_historical_data(stock_symbol).reset_index()
def atr_metric(historical_data):
    # Convert 'Date' to datetime and set it as index
    df = pd.DataFrame(historical_data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Calculate True Range (TR) and Average True Range (ATR)
    df['Previous_Close'] = df['Close'].shift(1)
    df['TR'] = np.maximum(
        df['High'] - df['Low'],
        np.maximum(
            abs(df['High'] - df['Previous_Close']),
            abs(df['Low'] - df['Previous_Close'])
        )
    )

    # Calculate ATR with a 14-day rolling window
    df['ATR'] = df['TR'].rolling(window=14).mean()

    # Prepare data for candlestick plotting
    df['Date_num'] = mdates.date2num(df.index)
    ohlc = df[['Date_num', 'Open', 'High', 'Low', 'Close']].dropna().values
    return df, ohlc

# Function to create the figure and axis
def fig_creator():
    fig, ax1 = plt.subplots(figsize=(12, 6))
    return fig, ax1

# Function to display the plot
def fig_show():
    plt.show()

# Function to plot the ATR chart with candlesticks
def atr_plotter(df , ohlc, ax1):
    try:
        # Plot the candlestick chart
        candlestick_ohlc(ax1, ohlc, width=0.6, colorup='green', colordown='red', alpha=0.8)
        ax1.set_ylabel('Price')
        ax1.set_title(f'{stock_symbol} Price and ATR')
        ax1.xaxis_date()
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.grid(True)

        # Create a secondary axis for ATR (twinx)
        ax2 = ax1.twinx()
        ax2.plot(df.index, df['ATR'], label='ATR (Volatility)', color='blue', linewidth=1)
        ax2.set_ylabel('ATR', color='purple')
        ax2.legend(loc='upper right')

        # Format and display the plot
        plt.xticks(rotation=45)
        plt.tight_layout()

    except Exception as e:
        print(f"Error in plotting ATR chart: {e}")

# Main function to tie everything together
def atr_main():
    df , ohlc = atr_metric(historical_data)
    fig, ax1 = fig_creator()
    p_main()
    atr_plotter(df ,ohlc, ax1)
    fig_show()

# Run the script
if __name__ == "__main__":
    atr_main()
