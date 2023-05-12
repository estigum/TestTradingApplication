import yfinance as yf
from yahooquery import Ticker

class StockMarketManager:
    def __init__(self):
        self.ticker_list = {}

    def add_ticker(self,ticker):
        if ticker not in self.ticker_list.keys():
            self.ticker_list[ticker] = 0.0

    def get_stock_price(self, ticker):
        if ticker in self.ticker_list:
            return self.ticker_list[ticker]
        else:
            data = yf.Ticker(ticker)
            latest_price = data.history(period="1d")["Close"].iloc[-1]
            return latest_price

    def get_stock_prices(self):
        tickers = ' '.join([str(key) for key in self.ticker_list.keys()])
        data = Ticker(tickers, asynchronous=True)
        data.asset_profile
        prices = data.price

        for ticker in self.ticker_list.keys():
            if ticker in prices.keys():
                real = prices[ticker]
                self.ticker_list[ticker] = real['regularMarketPrice']


