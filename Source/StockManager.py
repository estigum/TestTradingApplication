import requests

class StockManager:
    @classmethod
    def get_price(cls, symbol):
        url = f"https://finance.yahoo.com/quote/{symbol}"
        r = requests.get(url)
        start = r.text.find(f'"{symbol}":{"regularMarketPrice":{"raw":}}') + len(f'"{symbol}":{"regularMarketPrice":{"raw":}}')
        end = r.text.find(',"fmt"', start)
        price = float(r.text[start:end])
        return price