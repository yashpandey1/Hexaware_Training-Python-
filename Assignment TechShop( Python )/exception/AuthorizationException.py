class AuthorizationException(Exception):
    def __init__(self, message="You do not have permission to access this resource"):
        super().__init__(message)
