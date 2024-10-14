class DatabaseConnectionException(Exception):
    def __init__(self, message = "DatabaseConnectionException"):
        self.message = message
        super().__init__(self.message)