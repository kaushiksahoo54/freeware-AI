### Steps to Utilize
1. python -m venv venv
2. source venv/bun/activate
3. pip install requirements.txtß

### Fundamental Details

#### 1. Bollinger Bands
- **Purpose**: Identifies overbought or oversold conditions based on price deviation from a moving average.
- **Calculation**: Plots two standard deviations above and below a moving average line, creating bands.
- **Benefits**: Bollinger Bands are excellent for tracking trends and identifying reversals, offering a visual boundary for normal price movement.

#### Key Components of Bollinger Bands
- **Middle Band (SMA)**: Represents the 20-day simple moving average.
- **Upper Band**: SMA + 2 standard deviations; represents a potential resistance level.
- **Lower Band**: SMA - 2 standard deviations; represents a potential support level.

### General Interpretation
#### Price Touching or Moving Above the Upper Band:
- Indicates the stock might be overbought.
- A touch of the upper band alone is not necessarily a sell signal; it's a cautionary signal suggesting a high price level.
- **Sell Signal**: If the price touches the upper band and then begins to move back down toward the middle band, it could indicate a short-term peak.

#### Price Touching or Dropping Below the Lower Band:
- Indicates the stock might be oversold.
- A touch of the lower band alone isn’t necessarily a buy signal; it simply suggests a low price level.
- **Buy Signal**: If the price touches the lower band and then begins to rise back up toward the middle band, it could indicate a potential entry point as the price might rebound.

### Buy and Sell Signals Using Bollinger Bands
#### Buy Signal:
- Occurs when the price hits the lower band and starts to rise.
- This signal is stronger if accompanied by an increase in volume, suggesting buying interest.
- Another indicator of a buy signal could be the W-bottom pattern: the price touches the lower band, rebounds slightly, retests a similar level, and then moves upward.

#### Sell Signal:
- Occurs when the price hits the upper band and starts to fall.
- This signal is stronger if accompanied by increased selling volume, indicating potential profit-taking.
- An M-top pattern is also a bearish sign: the price touches the upper band, falls back, tests a similar high again, and then declines.

### Squeeze (Low Volatility, Trend Reversal):
- When the bands contract (come closer together), it indicates low volatility and often precedes a breakout. The price may move sharply in either direction following a squeeze.
- A breakout to the upside suggests a potential buy, while a breakout to the downside suggests a potential sell.

### Trend Continuation:
- If the price repeatedly rides along the upper band in an upward trend, this indicates strong bullish momentum. In this case, a price touching the upper band is not a sell signal but a sign that the trend may continue.
- Conversely, if the price rides along the lower band in a downtrend, it suggests bearish momentum.

### Caution
- **Confirmation with Other Indicators**: Bollinger Bands should not be used in isolation. It’s wise to confirm signals with other technical indicators, such as the Relative Strength Index (RSI) or Moving Average Convergence Divergence (MACD).
- **Avoid Overtrading**: Not every touch of the bands signals a buy or sell. Look for patterns, volume confirmation, and momentum to confirm signals.
