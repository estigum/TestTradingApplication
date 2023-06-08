class Transaction:
    def __init__(self, ticker, price, quantity, customer_id, transaction_type, transaction_id)
        self.ticker = ticker
        self.price = price
        self.quantity = quantity
        self.customer_id = customer_id
        self.transaction_type = transaction_type
        self.transaction_id = transaction_id

    def get_ticker(self):
        return self.ticker

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_customer_id(self):
        return self.customer_id

    def get_transaction_type(self):
        return self.transaction_type

    def get_transaction_id(self):
        return self.transaction_id