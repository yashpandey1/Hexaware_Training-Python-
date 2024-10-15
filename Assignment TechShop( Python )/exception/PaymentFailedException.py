class PaymentFailedException(Exception):
    def __init__(self, message="Payment processing failed"):
        super().__init__(message)
