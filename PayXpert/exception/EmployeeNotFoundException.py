class EmployeeNotFoundException(Exception):
    def __init__(self, message = "Employee not found exception"):
        self.message = message
        super().__init__(self.message)
