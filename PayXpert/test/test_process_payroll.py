import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

import unittest
from decimal import Decimal
from dao.IPayrollServiceImpl import PayrollServiceImpl

class TestProcessPayroll(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.payroll_service = PayrollServiceImpl()

    def test_process_payroll_for_multiple_employees(self):
        """Test case for end-to-end payroll processing for multiple employees."""
        employees_data = [
            {'employee_id': 1, 'basic_salary': Decimal('5000.00'), 'overtime_pay': Decimal('500.00'), 'deductions': Decimal('1000.00')},
            {'employee_id': 2, 'basic_salary': Decimal('6000.00'), 'overtime_pay': Decimal('300.00'), 'deductions': Decimal('800.00')}
        ]
        for employee in employees_data:
            employee_id = employee['employee_id']
            basic_salary = employee['basic_salary']
            overtime_pay = employee['overtime_pay']
            deductions = employee['deductions']
            net_salary = self.payroll_service.generate_payroll_test(employee_id, "2024-01-01", "2024-01-31", basic_salary, overtime_pay, deductions)
            

            self.assertIsNotNone(net_salary, f"Payroll processing failed for employee {employee_id}")
            
            self.assertGreater(net_salary, Decimal('0.00'), "Net salary should be positive")

if __name__ == '__main__':
    unittest.main()