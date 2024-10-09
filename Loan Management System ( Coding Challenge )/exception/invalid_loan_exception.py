class CustomerNotFoundException(Exception):
    def __init__(self, message="CustomerNotFoundException"):
        self.message = message
        super().__init__(self.message)

class LoanNotFoundException(Exception):
    def __init__(self, message="LoanNotFoundException"):
        self.message = message
        super().__init__(self.message)