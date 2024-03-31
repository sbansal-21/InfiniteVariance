import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
import random
import sys
import yfinance as yf

os.getcwd()

today = datetime.datetime.now().today()
numbers_of_years = 5
start_date = today - datetime.timedelta(numbers_of_years*365)

start_date = start_date.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
tickers = ["AAPL"]

stock_data = yf.Ticker(tickers[0])
historical_data = stock_data.history(start=start_date, end=end_date)
historical_data.head()


