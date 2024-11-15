#!/usr/bin/env python
# coding: utf-8
import time
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()

stock_symbol = 'RVNL'
# Navigate to the webpage
driver.get(f"https://www.screener.in/company/{stock_symbol}/consolidated/#peers")

# Find the table element
table = driver.find_element(By.XPATH, '//*[@id="peers-table-placeholder"]/div[3]')

# Get the table rows
rows = table.find_elements(By.TAG_NAME, "tr")

# Get the table headers
headers = [th.text for th in rows[0].find_elements(By.TAG_NAME, "th")]

# Get the table data
data = []
for row in rows[1:]:
    cells = row.find_elements(By.TAG_NAME, "td")
    data.append([cell.text for cell in cells])

df = pd.DataFrame(data, columns=headers)

print(df)

# Close the browser
driver.quit()