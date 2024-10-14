import re
from decimal import Decimal

class ValidationService:
    @staticmethod
    def validate_employee_data(employee_data):
        """
        Validates the employee data.
        :param employee_data: A tuple containing employee details.
        :raises ValueError: If any validation rule fails.
        """
        first_name, last_name, date_of_birth, gender, email, phone_number, address, position, joining_date = employee_data
        
        if not first_name or not last_name:
            raise ValueError("First name and last name are required.")
        
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", date_of_birth):
            raise ValueError("Date of birth must be in YYYY-MM-DD format.")       

        if gender not in ('Male', 'Female','male','female','others'):
            raise ValueError("Gender must be either 'M' or 'F'.")
        
        if not re.match(r"^\S+@\S+\.\S+$", email):
            raise ValueError("Invalid email address.")
        
        if not re.match(r"^\+?\d{10,15}$", phone_number):
            raise ValueError("Invalid phone number.")
        
        if not position:
            raise ValueError("Position is required.")
        
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", joining_date):
            raise ValueError("Joining date must be in YYYY-MM-DD format.")
        
    @staticmethod
    def validate_salary_data(basic_salary, overtime_pay, deductions):
        
        if not isinstance(basic_salary, (float, Decimal)) or basic_salary < 0:
            raise ValueError("Basic salary must be a positive number.")
        
        if not isinstance(overtime_pay, (float, Decimal)) or overtime_pay < 0:
            raise ValueError("Overtime pay must be a positive number.")
        
        if not isinstance(deductions, (float, Decimal)) or deductions < 0:
            raise ValueError("Deductions must be a positive number.")
