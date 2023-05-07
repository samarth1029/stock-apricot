"""
class to fetch stock data for ticker symbols from Yahoo Finance API
"""

import time
import pandas as pd


class YahooAPI(object):

    def __init__(self, interval="1d"):
        self.base_url = "https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_time}&period2={" \
                        "end_time}&interval={interval}&events=history "
        self.interval = interval

    def __build_url(self, ticker, start_date, end_date):
        return self.base_url.format(ticker=ticker, start_time=start_date, end_time=end_date, interval=self.interval)

    def get_ticker_data(self, ticker, start_date, end_date):
        epoch_start = int(time.mktime(start_date.timetuple()))
        epoch_end = int(time.mktime(end_date.timetuple()))
        return pd.read_csv(self.__build_url(ticker, epoch_start, epoch_end))



