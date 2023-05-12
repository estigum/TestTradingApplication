import unittest
from Source.StockMarketManager import StockMarketManager


class TestStockMarketManager(unittest.TestCase):
    def setUp(self):
        self.stockmarketmanager = StockMarketManager()

    def test_adding_ticker(self):
        self.stockmarketmanager.add_ticker('get')
        self.assertEqual(len(self.stockmarketmanager.ticker_list), 1)

    def test_get_stock_price(self):
        val = self.stockmarketmanager.get_stock_price('msft')
        self.assertTrue(val > 0)
