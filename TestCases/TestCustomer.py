import unittest
from Source.Customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer(1, "user1", "John", "Doe", "john.doe@example.com")
        self.customer2 = Customer(2, "user2", "Jane", "Doe", "jane.doe@example.com", "123-456-7890")

    def test_customer_properties(self):
        self.assertEqual(self.customer1.get_customer_id(), 1)
        self.assertEqual(self.customer1.get_username(), "user1")
        self.assertEqual(self.customer1.get_first_name(), "John")
        self.assertEqual(self.customer1.get_last_name(), "Doe")
        self.assertEqual(self.customer1.get_email(), "john.doe@example.com")
        self.assertIsNone(self.customer1.get_phone_number())

        self.assertEqual(self.customer2.get_customer_id(), 2)
        self.assertEqual(self.customer2.get_username(), "user2")
        self.assertEqual(self.customer2.get_first_name(), "Jane")
        self.assertEqual(self.customer2.get_last_name(), "Doe")
        self.assertEqual(self.customer2.get_email(), "jane.doe@example.com")
        self.assertEqual(self.customer2.get_phone_number(), "123-456-7890")

    def test_customer_setters(self):
        self.customer1.set_customer_id(10)
        self.assertEqual(self.customer1.get_customer_id(), 10)

        self.customer1.set_username("user10")
        self.assertEqual(self.customer1.get_username(), "user10")

        self.customer1.set_first_name("Tom")
        self.assertEqual(self.customer1.get_first_name(), "Tom")

        self.customer1.set_last_name("Smith")
        self.assertEqual(self.customer1.get_last_name(), "Smith")

        self.customer1.set_email("tom.smith@example.com")
        self.assertEqual(self.customer1.get_email(), "tom.smith@example.com")

        self.customer1.set_phone_number("123-456-7890")
        self.assertEqual(self.customer1.get_phone_number(), "123-456-7890")


if __name__ == '__main__':
    unittest.main()
