import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import json

# Load configuration
with open("./config.json") as f:
    config = json.load(f)
num_months = config.get("num_months", 3)
stock_symbol = config.get("stock_symbol", "AAPL")
plot_active = config.get("plotter", "inactive").lower() == 'active'

def get_realtime_data(stock_symbol: str):
    """
    Fetches real-time stock data for the specified stock symbol.
    
    Args:
        stock_symbol (str): Ticker symbol of the stock.
    
    Returns:
        DataFrame: Real-time data for the current day with 1-minute intervals.
    """
    stock = yf.Ticker(stock_symbol)
    try:
        real_time_data = stock.history(period="1d", interval="1m")
        return real_time_data.tail()  # Last few rows for quick reference
    except Exception as e:
        print(f"Failed to fetch real-time data: {e}")
        return pd.DataFrame()

def get_historical_data(stock_symbol: str, months=num_months):
    """
    Fetches historical stock data over a specified duration.
    
    Args:
        stock_symbol (str): Ticker symbol of the stock.
        months (int): Number of months to look back for historical data.
    
    Returns:
        DataFrame: Historical OHLCV data over the specified period.
    """
    stock = yf.Ticker(stock_symbol)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=months * 30)
    try:
        historical_data = stock.history(start=start_date, end=end_date)
        return historical_data
    except Exception as e:
        print(f"Failed to fetch historical data: {e}")
        return pd.DataFrame()

def plotter(diary: pd.DataFrame):
    """
    Plots the stock's close price along with Bollinger Bands.
    
    Args:
        diary (pd.DataFrame): DataFrame containing stock prices to be plotted.
    """
    if diary.empty:
        print("No data to plot.")
        return
    
    plt.figure(figsize=(12, 6))
    plt.plot(diary.index, diary['Close'], label='Close', color='blue')

    # Calculate Bollinger Bands components
    diary['STD_20'] = diary['Close'].rolling(window=20).std()
    diary['SMA_20'] = diary['Close'].rolling(window=20).mean()
    diary['Upper_Band'] = diary['SMA_20'] + (diary['STD_20'] * 2)
    diary['Lower_Band'] = diary['SMA_20'] - (diary['STD_20'] * 2)

    # Plot SMA and Bollinger Bands
    plt.plot(diary.index, diary['SMA_20'], label='20-Day SMA', color='orange')
    plt.plot(diary.index, diary['Upper_Band'], label='Upper Bollinger Band', color='green', linestyle='--')
    plt.plot(diary.index, diary['Lower_Band'], label='Lower Bollinger Band', color='red', linestyle='--')
    plt.fill_between(diary.index, diary['Upper_Band'], diary['Lower_Band'], color='gray', alpha=0.3)
    
    plt.title('Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Fetch real-time data
    real_time_data = get_realtime_data(stock_symbol)
    print("Real-Time Data:\n", real_time_data)

    # Fetch and process historical data
    historical_data = get_historical_data(stock_symbol)
    if not historical_data.empty:
        historical_data = historical_data.reset_index()
        historical_data['Date'] = pd.to_datetime(historical_data['Date'])
        historical_data.set_index('Date', inplace=True)

        # High-Low standard deviation as additional metric
        historical_data['High_Low_STD'] = historical_data[['High', 'Low']].std(axis=1)

        # Plot if activated
        if plot_active:
            plotter(historical_data)
    else:
        print("Historical data could not be fetched.")

# Run main function
if __name__ == "__main__":
    main()
