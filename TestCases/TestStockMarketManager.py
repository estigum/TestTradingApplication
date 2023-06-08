import unittest
from Source.StockMarketManager import StockMarketManager


class TestStockMarketManager(unittest.TestCase):
    def setUp(self):
        self.stockmarketmanager = StockMarketManager()

    def test_adding_ticker(self):
        self.stockmarketmanager.add_ticker('get')
        self.assertEqual(len(self.stockmarketmanager.ticker_list), 1)

    def test_get_stock_price(self):
        self.stockmarketmanager.add_ticker('MSFT')
        self.stockmarketmanager.get_latest_stock_prices()
        val = self.stockmarketmanager.get_stock_price('MSFT')
        self.assertTrue(val > 0)

    def test_get_currency_pair_price(self):
        self.stockmarketmanager.add_currency_pair('USD/EUR')
        self.stockmarketmanager.get_latest_currency_prices()
        val = self.stockmarketmanager.get_currency_pair_price('USD/EUR')
        self.assertTrue(val > 0)
