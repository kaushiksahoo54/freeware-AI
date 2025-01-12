import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import json

# Load configuration
with open("./config.json") as f:
    config = json.load(f)
num_months = config["num_months"]
stock_symbol = config["stock_symbol"]

# Function to get real-time data
def get_realtime_data(stock_symbol: str):
    stock = yf.Ticker(stock_symbol)
    real_time_data = stock.history(period="1d", interval="1m")
    return real_time_data.tail()

# Function to get historical data
def get_historical_data(stock_symbol: str, months=num_months):
    stock = yf.Ticker(stock_symbol)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=months * 30)
    historical_data = stock.history(start=start_date, end=end_date)
    return historical_data

# Function to calculate Fibonacci retracement levels
def fibonacci_retracement(data: pd.DataFrame):
    high_price = data['High'].max()
    low_price = data['Low'].min()

    # Calculate Fibonacci retracement levels
    diff = high_price - low_price
    levels = {
        "100%": high_price,
        "61.8%": high_price - 0.618 * diff,
        "50%": high_price - 0.5 * diff,
        "38.2%": high_price - 0.382 * diff,
        "23.6%": high_price - 0.236 * diff,
        "0%": low_price
    }
    
    return levels

# Plotter function to plot Fibonacci levels
def plotter(diary: pd.DataFrame, fib_levels: dict):
    plt.plot(diary.index, diary['Close'], label='Close Price', color='blue')

    # Plot the Fibonacci retracement levels
    for level, price in fib_levels.items():
        plt.axhline(price, linestyle='--', label=f'Fibonacci {level} Level: {price:.2f}')
    
    plt.title('Fibonacci Retracement Levels')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

# Main function
def f_main():
    real_time_data = get_realtime_data(stock_symbol)
    print("Real-Time Data:\n", real_time_data)

    historical_data = get_historical_data(stock_symbol).reset_index()
    print("\nHistorical Data:\n", historical_data)

    historical_data['Date'] = pd.to_datetime(historical_data['Date'])
    historical_data.set_index('Date', inplace=True)

    # Calculate Fibonacci levels
    fib_levels = fibonacci_retracement(historical_data)

    # Plot the data with Fibonacci levels
    if str.lower(config["plotter"]) == 'active':
        plotter(historical_data, fib_levels)

# Run the main function
if __name__ == "__main__":
    f_main()
    plt.show()
