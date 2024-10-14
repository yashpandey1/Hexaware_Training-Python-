class InvalidInputException(Exception):
    def __init__(self, message = "InvalidInputException"):
        self.message = message
        super().__init__(self.message)