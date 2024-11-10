import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
sys.path.append(".")  # or ".." based on your folder structure
from utils.performance import get_realtime_data, get_historical_data, plotter

# Mock data for testing
mock_realtime_data = pd.DataFrame({
    'Open': [100.0, 101.0],
    'High': [105.0, 106.0],
    'Low': [99.0, 100.0],
    'Close': [104.0, 103.5],
    'Volume': [300, 500]
})

mock_historical_data = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Open': [100 + i for i in range(10)],
    'High': [105 + i for i in range(10)],
    'Low': [95 + i for i in range(10)],
    'Close': [102 + i for i in range(10)],
    'Volume': [1000 * i for i in range(10)]
}).set_index('Date')

@pytest.fixture
def sample_stock_symbol():
    return "TCS.NS"

@patch("utils.performance.yf.Ticker")
def test_get_realtime_data(mock_ticker, sample_stock_symbol):
    mock_ticker.return_value.history.return_value = mock_realtime_data
    result = get_realtime_data(sample_stock_symbol)
    assert not result.empty, "Returned data should not be empty"
    assert result.equals(mock_realtime_data.tail()), "Data returned does not match expected real-time data"

@patch("utils.performance.yf.Ticker")
def test_get_historical_data(mock_ticker, sample_stock_symbol):
    mock_ticker.return_value.history.return_value = mock_historical_data
    result = get_historical_data(sample_stock_symbol, months=3)
    assert not result.empty, "Returned data should not be empty"
    assert result.equals(mock_historical_data), "Data returned does not match expected historical data"

@patch("utils.performance.plt.show")
def test_plotter(mock_show):
    plotter(mock_historical_data)
    mock_show.assert_called_once()

if __name__ == "__main__":
    pytest.main()
