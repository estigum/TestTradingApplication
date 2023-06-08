class Customer:
    """
    Represents a customer in the stock trading game.

    :param customer_id: The unique ID of the customer.
    :type customer_id: int
    :param username: The username of the customer.
    :type username: str
    :param first_name: The first name of the customer.
    :type first_name: str
    :param last_name: The last name of the customer.
    :type last_name: str
    :param phone_number: The phone number of the customer (optional).
    :type phone_number: str or None
    :param email: The email address of the customer.
    :type email: str

    :raises ValueError: If the customer ID is not a positive integer.
    :raises ValueError: If any of the required parameters (username, first_name, last_name, email) are empty strings.

    :usage: customer = Customer(customer_id=1, username='jdoe', first_name='John',
                                    last_name='Doe', phone_number='123-456-7890',
                                    email='jdoe@example.com')
    """

    def __init__(self, customer_id, username, first_name, last_name, email, phone_number=None):
        self.customer_id = customer_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Username: {self.username}, First Name: {self.first_name}, " \
               f"Last Name: {self.last_name}, Phone Number: {self.phone_number}, Email: {self.email}"

    def __repr__(self):
        return f"Customer(customer_id={self.customer_id}, username={self.username}, first_name={self.first_name}, " \
               f"last_name={self.last_name}, phone_number={self.phone_number}, email={self.email})"

    # Getters
    def get_customer_id(self):
        """
        :return: customer_id: This returns the customer_id for a given customer
        :rtype: int
        """

        return self.customer_id

    def get_username(self):
        """
        :return: username: username for this customer
        :rtype: str
        """
        return self.username

    def get_first_name(self):
        """
        :return: first_name: first name for this customer
        :rtype: str
        """
        return self.first_name

    def get_last_name(self):
        """
        :return: last_name: last name of this customer
        :rtype: str
        """
        return self.last_name

    def get_email(self):
        """
        :return: email: The email address for this customer
        :rtype: str
        """
        return self.email

    def get_phone_number(self):
        """
        :return: phone_number: The phone number for this customer
        :rtype: str
        """
        return self.phone_number

    # Setters
    def set_customer_id(self, customer_id):
        """
        :param customer_id: This is a unique id for customer
        :type customer_id: int
        """
        self.customer_id = customer_id

    def set_username(self, username):
        """
        :param username:  The username. Example would be estigum
        :type username: str
        """
        self.username = username

    def set_first_name(self, first_name):
        """
        :param first_name: The first name of the customer
        :type first_name: str
        """
        self.first_name = first_name

    def set_last_name(self, last_name):
        """
        :param last_name: The last name of the user
        :type last_name: str
        """
        self.last_name = last_name

    def set_email(self, email):
        """
        :param email:  This is the email address of customer
        :type email: str
        """
        self.email = email

    def set_phone_number(self, phone_number):
        """
        :param phone_number: This is the phone number for customer
        :type phone_number: str
        """
        self.phone_number = phone_number
