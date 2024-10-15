class IOException(Exception):
    def __init__(self, message="An error occurred during file I/O operations"):
        super().__init__(message)
