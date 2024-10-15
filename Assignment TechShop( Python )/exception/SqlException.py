class SqlException(Exception):
    def __init__(self, message="An error occurred while interacting with the database"):
        super().__init__(message)
