# Fibonacci Retracement Stock Analysis

This Python script retrieves historical stock data, calculates **Fibonacci retracement levels**, and plots these levels along with the stock's closing price. Fibonacci retracement is a popular tool used in technical analysis to identify potential levels where the price might reverse or find support/resistance.

## Table of Contents
- [Overview](#overview)
- [Fibonacci Retracement Levels](#fibonacci-retracement-levels)
- [Installation](#installation)
- [Configuration](#configuration)
- [How to Use](#how-to-use)
- [Interpretation](#interpretation)
- [Customization](#customization)

## Overview
This script helps traders and analysts identify potential **support** and **resistance** levels for a stock, using **Fibonacci retracement** levels. The Fibonacci retracement tool is based on the idea that markets often retrace a predictable portion of a move, after which they may continue in the original direction.

The script does the following:
1. Retrieves the stock's **historical data** for a given time period.
2. Calculates the **Fibonacci retracement levels** based on the stock’s highest and lowest prices.
3. Plots the **Fibonacci levels** along with the **closing price** to help visualize potential price reversals.

## Fibonacci Retracement Levels
Fibonacci retracement levels are key horizontal lines drawn on a chart that indicate potential support or resistance levels. These levels are derived by taking the high and low points of a stock price and applying the key Fibonacci ratios:
- **0%**: Lowest point (start of the move).
- **23.6%**: The first retracement level.
- **38.2%**: The second retracement level.
- **50%**: Often used as a psychological level.
- **61.8%**: The most important Fibonacci retracement level.
- **100%**: Highest point (end of the move).

These levels are typically used to predict the possible points at which the stock price may reverse or find support during a pullback.

### **Common interpretations of Fibonacci levels**:
- **Price Near 0%**: If the price is close to the low point (0%), the trend is at its beginning.
- **Price Near 100%**: If the price reaches the high point (100%), the trend has potentially reached its peak.
- **Price Reaching 61.8%**: This level is considered one of the most significant. If the price retraces to this level and starts moving in the direction of the original trend, it might be a continuation signal.
- **Price Near 50%**: This level is not a true Fibonacci level but is often used in technical analysis as it represents a significant midpoint.

## Installation

To use this script, you need to install the following Python libraries:
- `yfinance` - To fetch real-time and historical stock data.
- `matplotlib` - To plot the stock data and Fibonacci levels.
- `pandas` - To handle and manipulate data.

Install the necessary libraries with:

```bash
pip install yfinance matplotlib pandas
