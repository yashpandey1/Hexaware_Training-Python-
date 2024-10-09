from loan import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, loan_type, loan_status, property_address, property_value):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, loan_type, loan_status)
        self.property_address = property_address
        self.property_value = property_value

    def __str__(self):
        return f"HomeLoan [PropertyAddress={self.property_address}, PropertyValue={self.property_value}]"
