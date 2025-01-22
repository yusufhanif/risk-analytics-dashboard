import pandas as pd
import yfinance as yf
import numpy
import matplotlib
from datetime import datetime

LITgStocks = 'corporate_positions.csv'

df = pd.read_csv(LITgStocks, usecols=["Symbol", "Qty", "Cost Basis"]) #need to confirm that CB is titled that way

#print(df)

ticker_list = []

for x in range(len(df)):

    ticker = df.iloc[x, 0]

    print(ticker)

    #adding tickers to single string and list

    all_stock_tickers_string = ticker + " "

    ticker_list.append(ticker)

    #getting sector of ticker

    stock_info = yf.Ticker(ticker)

    print(stock_info.info['sector'])




    # sharpe ratio

    for x in range(len(ticker_list)):

        ticker_object = yf.Ticker(ticker_list[x])
        historical_data = ticker_object.history(period='max')

        # Calculate daily percentage returns

        historical_data['Daily Return'] = historical_data['Close'].pct_change()

        # Calculate total return
        total_return = (historical_data['Close'].iloc[-1] / historical_data['Close'].iloc[0]) - 1 #dividing most recent price by first
        print(f"Total Return: {total_return:.4f}")

        # you need to write out what the problem requires first and think from there.

        calculated_average_return = -1
        riskfreerate = 4.79
        stdstockreturn = -1

        #individual_sharpe_ratio = ((calculated_average_return - riskfreerate)/stdstockreturn)

        # sharpe ratio of particular stock

        # (average return - risk free return) / standard deviation of stock

        # sharpe ratio of sector

        # sharpe ratio of entire portfolio

    # VaR parametric
    # VaR historical
    # basic beta
    # plotly visualizations
    #









