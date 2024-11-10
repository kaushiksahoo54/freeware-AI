import pytest
import pandas as pd
import numpy as np
from datetime import datetime
from unittest.mock import patch, mock_open
import json
import sys
sys.path.append(".")  # or ".." based on your folder structure
import utils.ATR as ATR

# Sample configuration
sample_config = {
    "stock_symbol": "TEST"
}

# Sample historical data for testing
@pytest.fixture
def sample_data():
    dates = pd.date_range(start="2023-01-01", periods=20, freq="D")
    data = {
        "Date": dates,
        "Open": np.random.uniform(100, 200, size=20),
        "High": np.random.uniform(200, 300, size=20),
        "Low": np.random.uniform(50, 100, size=20),
        "Close": np.random.uniform(150, 250, size=20)
    }
    return pd.DataFrame(data).set_index("Date")

# Test calculate_indicators function
def test_calculate_indicators(sample_data):
    from utils.ATR import calculate_indicators  # Replace with actual script name

    df = calculate_indicators(sample_data.copy())
    
    # Check if the necessary columns are created
    assert 'ATR' in df.columns, "ATR column missing"
    assert 'SMA_20' in df.columns, "SMA_20 column missing"
    assert 'EMA_20' in df.columns, "EMA_20 column missing"
    assert 'RSI' in df.columns, "RSI column missing"
    
    # Check values (ATR, SMA, EMA, RSI should not be null after rolling period)
    assert not df['ATR'].isnull().all(), "ATR calculation failed"
    assert not df['SMA_20'].isnull().all(), "SMA calculation failed"
    assert not df['EMA_20'].isnull().all(), "EMA calculation failed"
    assert not df['RSI'].isnull().all(), "RSI calculation failed"

# Test get_historical_data function with mock
@patch('utils.ATR.get_historical_data')
def test_get_historical_data(mock_get_historical_data, sample_data):
    mock_get_historical_data.return_value = sample_data
    
    # Call the function with the mock
    from utils.ATR import get_historical_data
    result = get_historical_data(stock_symbol="TEST")

    # Verify the mock was called and result is as expected
    mock_get_historical_data.assert_called_once_with("TEST")
    pd.testing.assert_frame_equal(result, sample_data)

# Test plot_stock_data function with mock (no assertion on plot itself here)
@patch('utils.ATR.calculate_indicators')
@patch('utils.ATR.prepare_candlestick_data')
def test_plot_stock_data(mock_prepare_candlestick_data, mock_calculate_indicators, sample_data):
    from utils.ATR import plot_stock_data
    
    # Mock outputs for dependencies
    mock_prepare_candlestick_data.return_value = np.array([[1, 2, 3, 4, 5]])  # Dummy data for candlestick
    mock_calculate_indicators.return_value = sample_data
    
    # Run the plot function (visual check)
    plot_stock_data(sample_data)  # Here we assume visual inspection; use pytest-mpl for automated visual testing
    
    # Verify mocks were called
    mock_prepare_candlestick_data.assert_called_once_with(sample_data)
    mock_calculate_indicators.assert_called_once_with(sample_data)

# Test main function with mocked configuration and data retrieval
@patch('utils.ATR.get_historical_data')
@patch('builtins.open', new_callable=mock_open, read_data=json.dumps(sample_config))
@patch('utils.ATR.plot_stock_data')
def test_main(mock_plot_stock_data, mock_open, mock_get_historical_data, sample_data):
    from utils.ATR import main  # Replace with actual script name

    # Set up mock return values
    mock_get_historical_data.return_value = sample_data

    # Run main function
    main()

    # Verify mocks
    mock_open.assert_called_once_with('./config.json')
    mock_get_historical_data.assert_called_once_with("TEST")
    mock_plot_stock_data.assert_called_once()
if __name__ == "__main__":
    pytest.main()