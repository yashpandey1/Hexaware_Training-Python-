import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

import unittest
from decimal import Decimal

class TestCalculateGrossSalary(unittest.TestCase):
    def test_calculate_gross_salary_for_employee(self):
        """Test case to verify gross salary calculation."""
        basic_salary = Decimal('5000.00')
        overtime_pay = Decimal('500.00')
        gross_salary = basic_salary + overtime_pay
        self.assertEqual(gross_salary, Decimal('5500.00'), "Gross salary calculation is incorrect.")

if __name__ == '__main__':
    unittest.main()

