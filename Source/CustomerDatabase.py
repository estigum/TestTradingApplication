import sqlite3
from Source.Customer import Customer


class CustomerDatabase:
    """
    This is my constructor
    """
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_customer_table()

    def create_customer_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT
        )''')
        self.conn.commit()

    def save_customer(self, customer):
        self.cursor.execute('''INSERT INTO customers (
            customer_id,
            username,
            first_name,
            last_name,
            email,
            phone_number
        ) VALUES (?, ?, ?, ?, ?, ?)''', (
            customer.customer_id,
            customer.username,
            customer.first_name,
            customer.last_name,
            customer.email,
            customer.phone_number
        ))
        self.conn.commit()

    def update_customer(self, customer):
        self.cursor.execute('''UPDATE customers SET
            username = ?,
            first_name = ?,
            last_name = ?,
            email = ?,
            phone_number = ?
        WHERE customer_id = ?''', (
            customer.username,
            customer.first_name,
            customer.last_name,
            customer.email,
            customer.phone_number,
            customer.customer_id
        ))
        self.conn.commit()

    def get_all_customers(self):
        self.cursor.execute('''SELECT * FROM customers''')
        customers = self.cursor.fetchall()
        return {row[0]: Customer(*row) for row in customers}

    def customer_exists(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM customers WHERE customer_id = ?', (customer_id,))
        return cursor.fetchone()[0] > 0

    def get_customer_id_by_username(self, username):
        self.cursor.execute('SELECT customer_id FROM customers WHERE username=?', (username,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def close(self):
        self.cursor.close()
        self.conn.close()
