import unittest
import tempfile
import os
from Source.Customer import Customer
from Source.CustomerDatabase import CustomerDatabase


class TestCustomerDatabase(unittest.TestCase):
    def setUp(self):
        self.db_file = "C:\\temp\\test.db"
        self.customer_db = CustomerDatabase(self.db_file)
        self.customer = Customer(1, "johndoe", "John", "Doe",  "johndoe@example.com", "123-456-7890")

    def tearDown(self):
        self.customer_db.close()
        os.remove(self.db_file)
        x = 45

    def test_save_customer(self):
        self.customer_db.save_customer(self.customer)
        result = self.customer_db.get_all_customers()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[1].username, "johndoe")

    def test_update_customer(self):
        self.customer_db.save_customer(self.customer)
        self.customer.email = "newemail@example.com"
        self.customer_db.update_customer(self.customer)
        result = self.customer_db.get_all_customers()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[1].email, "newemail@example.com")

    def test_customer_exists(self):
        self.customer_db.save_customer(self.customer)
        result = self.customer_db.customer_exists(1)
        self.assertTrue(result)

    def test_get_customer_id_by_username(self):
        self.customer_db.save_customer(self.customer)
        result = self.customer_db.get_customer_id_by_username("johndoe")
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
