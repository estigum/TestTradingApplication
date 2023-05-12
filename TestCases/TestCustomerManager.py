import unittest
from Source.CustomerManager import CustomerManager, Customer


class TestCustomerManager(unittest.TestCase):
    def setUp(self):
        self.customer_manager = CustomerManager()
        self.customer1 = Customer(self.customer_manager.get_next_customer_id(), "user1", "John", "Doe", "john.doe@example.com")
        self.customer2 = Customer(self.customer_manager.get_next_customer_id(), "user2", "Jane", "Doe", "jane.doe@example.com", "123-456-7890")

    def test_add_customer(self):
        self.customer_manager.add_customer("user1", "John", "Doe", "john.doe@example.com")
        self.assertEqual(len(self.customer_manager.get_all_customers()), 1)


    def test_add_customer_object(self):
        self.customer_manager.add_customer_object(self.customer1)
        self.assertEqual(len(self.customer_manager.get_all_customers()), 1)

    def test_get_customer_by_id(self):
        self.customer_manager.add_customer_object(self.customer1)
        self.customer_manager.add_customer_object(self.customer2)
        customer = self.customer_manager.get_customer_by_id(1)
        self.assertEqual(customer.get_first_name(), "John")

    def test_get_all_customers(self):
        self.customer_manager.add_customer_object(self.customer1)
        self.customer_manager.add_customer_object(self.customer2)
        all_customers = self.customer_manager.get_all_customers()
        self.assertEqual(len(all_customers), 2)
        self.assertEqual(all_customers[0].get_username(), "user1")
        self.assertEqual(all_customers[1].get_username(), "user2")

    def test_get_customer_by_id_nonexistent(self):
        with self.assertRaises(ValueError):
            self.customer_manager.get_customer_by_id(1)


if __name__ == '__main__':
    unittest.main()
