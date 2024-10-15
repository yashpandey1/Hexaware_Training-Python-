class Customer:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._address = address
        self._total_orders = 0  

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def calculate_total_orders(self):
        return self._total_orders

    def get_customer_details(self):
        return {
            "CustomerID": self._customer_id,
            "FirstName": self._first_name,
            "LastName": self._last_name,
            "Email": self._email,
            "Phone": self._phone,
            "Address": self._address
        }

    def update_customer_info(self, email: str = None, phone: str = None, address: str = None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
