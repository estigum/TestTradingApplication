from Source.Customer import Customer


class CustomerManager:
    """
    This is the CustomerManger.  It is responsible for manging customers in the system.  It add and update custmers.
    :usage: custMgr= CustomerManager()
    """
    def __init__(self):
        self.customers = {}
        self.max_customer_Id = 0

    def add_customer(self, username, first_name, last_name, email, phone_number=None):
        """
        :comment: This will increment max_customer_id and assign that as thec customer_id being added
        :param username: the username of customer
        :type username: str
        :param first_name: the first name of the customer
        :type first_name: str
        :param last_name:  the last name of the customer
        :type last_name: str
        :param email:  the email address of the customer
        :type email: str
        :param phone_number:  the phone number of the customer if they provide one
        :type phone_number: str
        :return:
        """
        self.max_customer_Id += 1
        customer = Customer(self.max_customer_Id, username, first_name, last_name, email, phone_number)
        self.customers[self.max_customer_Id] = customer

    def add_customer_object(self, customer):
        """
        :comment: This takes an existing customer and adds it to list.  If the customer_id is greater than max_custome_id, then that becomes the max_customer_id
        :param customer: This is the customer
        :type customer:
        Customer :return:
        """
        if customer.get_customer_id() > self.max_customer_Id:
            self.max_customer_Id = customer.get_customer_id()
        self.customers[customer.get_customer_id()] = customer

    def get_customer_by_id(self, customer_id):
        """
        :comment: This will get a customer by customer_id
        :param customer_id: This is the customer that we want back.
        :type customer_id: int
        :return: customer: The customer based customer_id
        :rtype: Customer, None
        """
        customer = self.customers.get(customer_id)
        if customer is None:
            raise ValueError(f"No customer found with ID {customer_id}")
        return customer

    def get_next_customer_id(self):
        """
        :comment: This will increment max_customer_id and return it.
        :return: max_customer_id
        :rtype: int
        """
        self.max_customer_Id += 1
        return self.max_customer_Id

    def get_all_customers(self):
        """
        :comment: This will return a list of all customers
        :return:
        :rtype: list<str>
        """
        return list(self.customers.values())
