class Loan:
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status

    def get_loan_id(self):
        return self._loan_id

    def get_customer_id(self):
        return self._customer_id

    def get_principal_amount(self):
        return self._principal_amount

    def get_interest_rate(self):
        return self._interest_rate

    def get_loan_term(self):
        return self._loan_term

    def get_loan_type(self):
        return self._loan_type

    def get_loan_status(self):
        return self._loan_status

    def set_loan_id(self, loan_id):
        self._loan_id = loan_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_principal_amount(self, principal_amount):
        self._principal_amount = principal_amount

    def set_interest_rate(self, interest_rate):
        self._interest_rate = interest_rate

    def set_loan_term(self, loan_term):
        self._loan_term = loan_term

    def set_loan_type(self, loan_type):
        self._loan_type = loan_type

    def set_loan_status(self, loan_status):
        self._loan_status = loan_status

    def display(self):
        print(f"Loan ID: {self.loan_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Principal Amount: {self.principal_amount}")
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Loan Term: {self.loan_term} months")
        print(f"Loan Type: {self.loan_type}")
        print(f"Loan Status: {self.loan_status}")

