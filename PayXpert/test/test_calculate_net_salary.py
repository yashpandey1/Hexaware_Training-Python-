import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

import unittest
from decimal import Decimal

class TestCalculateNetSalary(unittest.TestCase):
    def test_calculate_net_salary_after_deductions(self):
        """Test case to ensure net salary is correctly calculated after deductions."""
        basic_salary = Decimal('5000.00')
        overtime_pay = Decimal('500.00')
        deductions = Decimal('1000.00')
        gross_salary = basic_salary + overtime_pay
        net_salary = gross_salary - deductions
        self.assertEqual(net_salary, Decimal('4500.00'), "Net salary calculation is incorrect.")

if __name__ == '__main__':
    unittest.main()
