class ConcurrencyException(Exception):
    def __init__(self, message="Concurrency error detected, please retry the operation"):
        super().__init__(message)
