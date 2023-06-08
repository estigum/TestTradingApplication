import yfinance as yf
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

class StockMarketManager:
    """
    This class is used to manage stock market information
    usage: stock_market = StockMarketManager()
    """
    def __init__(self):
        self.ticker_list = {}
        self.currency_pair_list = {}

    """
    comment: This will add a ticker to the list
    :param ticker: the ticker to add
    """
    def add_ticker(self, ticker):
        if ticker not in self.ticker_list.keys():
            self.ticker_list[ticker] = 0.0

    def add_currency_pair(self, currency_pair):
        if currency_pair not in self.currency_pair_list.keys():
            self.currency_pair_list[currency_pair] = 0.0

    """
    comment: This will get the stock price for a ticker. If not in ticker list will return None
    :param ticker: the ticker to get the price for
    :return: the price of the ticker, None if it does not have ticker list
    """
    def get_stock_price(self, ticker):
        if ticker in self.ticker_list:
            return self.ticker_list[ticker]
        else:
            print("Ticker has not been added to the list")
            return None

    def get_currency_pair_price(self, currency_pair):
        if currency_pair in self.currency_pair_list:
            return self.currency_pair_list[currency_pair]
        else:
            print("Currency pair has not been added to the list")
            return None

    """
    comment: This will get the latest stock prices for all tickers in the list
    """
    def get_latest_stock_prices(self):
        try:
            tickers = [yf.Ticker(ticker) for ticker in self.ticker_list.keys()]
            for ticker in tickers:
                latest_price = ticker.history(period="1d")["Close"].iloc[-1]
                self.ticker_list[ticker.ticker] = latest_price
        except Exception as e:
            print("Error getting stock data: " + str(e))

    def get_latest_currency_prices(self):
        try:
            c = CurrencyRates()
            for currency_pair in self.currency_pair_list.keys():
                currencies = currency_pair.split('/')
                if len(currencies) == 2:
                    rate = c.get_rate(currencies[0], currencies[1])
                    self.currency_pair_list[currency_pair] = rate
        except Exception as e:
            print("Error getting currency data: " + str(e))

    def get_latest_btc_price(self, currency):
        try:
            b = BtcConverter()
            rate = b.get_latest_price(currency)
            return rate
        except Exception as e:
            print("Error getting crypto data: " + str(e))
