from Source.Customer import Customer
from Source.CustomerManager import CustomerManager
from Source.CustomerDatabase import CustomerDatabase
from Source.StockMarketManager import StockMarketManager

if __name__ == '__main__':
    print('This is  a test trading application')
    dbMgr = CustomerDatabase("customer.db")
    custMgr = CustomerManager()
    dbMgr.create_customer_table()
    customers = dbMgr.get_all_customers()
    for customer_id, customer in customers.items():
        custMgr.add_customer_object(customer)
    customer_id = dbMgr.get_customer_id_by_username("tstigum")
    if customer_id is None:
        cust = Customer(custMgr.get_next_customer_id(), "tstigum", "Tove", "Stigum","tstigum@gmail.com");
        dbMgr.save_customer(cust)
    else:
        cust = Customer(customer_id, "tstigum", "Tove", "Stigum","tstigum@gmail.com");
        dbMgr.update_customer(cust)
    custMgr.add_customer_object(cust)
    dbMgr.close()

    stock_market = StockMarketManager()
    stock_market.add_ticker('IBM')
    stock_market.add_ticker('GE')
    stock_market.add_ticker('MSFT')
    stock_market.add_ticker('GOOG')
    stock_market.add_ticker('AMZN')
    stock_market.add_currency_pair("EUR/USD")
    stock_market.add_currency_pair("USD/JPY")
    stock_market.add_currency_pair("USD/CAD")
    stock_market.add_currency_pair("GBP/USD")
    stock_market.add_currency_pair("USD/CNY")
    stock_market.get_latest_stock_prices()
    stock_market.get_latest_currency_prices()
    val = stock_market.get_stock_price('IBM')
    print(f"The price of IBM is {val}" )
    val = stock_market.get_stock_price('GOOG')
    print(f"The price of GOOG is {val}")
    val = stock_market.get_currency_pair_price('EUR/USD')
    print(f"The price of EUR/USD is {val}")
    val = stock_market.get_currency_pair_price('USD/JPY')
    print(f"The price of USD/JPY is {val}")
    val = stock_market.get_currency_pair_price('USD/CNY')
    print(f"The price of USD/CNY is {val}")
    val = stock_market.get_latest_btc_price("USD")
    print(f"The price of BTC/USD is {val}")
