class IncompleteOrderException(Exception):
    def __init__(self, message="Order is incomplete"):
        super().__init__(message)
