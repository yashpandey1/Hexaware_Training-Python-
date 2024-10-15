class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed, please check your credentials"):
        super().__init__(message)
