from Source.Customer import Customer
from Source.CustomerManager import CustomerManager
from Source.CustomerDatabase import CustomerDatabase
from Source.StockMarketManager import StockMarketManager

import yfinance as yf
from yahooquery import Ticker

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
    #price = StockManager.get_price("IBM");
    #print("Price of IBM " + str(price))
    msft = yf.Ticker("MSFT")
    latest_price = msft.history(period="1d")["Close"].iloc[-1]
    print("MSFT Last Price " + str(latest_price))
    aapl = Ticker('aapl ibm ge', asynchronous=True)

    #aapl.summary_detail
    data =aapl.asset_profile
    price = aapl.price
    real = price['aapl']
    the_price = real['regularMarketPrice']
    print("The Price for AAPL " + str(the_price))

    stock_market = StockMarketManager()
    val = stock_market.get_stock_price('ibm')
    print(f"The price of ibm is {val}" )
    stock_market.add_ticker('ge')
    stock_market.add_ticker('msft')
    stock_market.add_ticker('goog')
    stock_market.get_stock_prices()
    val = stock_market.get_stock_price('goog')
    print(f"The price of goog is {val}")


    symbols = aapl.symbols


    symbols = ['fb', 'aapl', 'amzn', 'nflx', 'goog']

    #faang = Ticker(symbols)
    #df = faang.option_chain
    #test = df.loc['aapl', '2023-04-14']
    #faang.summary_detail

    print("getting data")

