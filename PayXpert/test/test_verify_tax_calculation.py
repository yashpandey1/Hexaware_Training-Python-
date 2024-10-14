import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

import unittest
from decimal import Decimal
from dao.ITaxServiceImpl import TaxServiceImpl

class TestVerifyTaxCalculation(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.tax_service = TaxServiceImpl()

    def test_verify_tax_calculation_for_high_income_employee(self):
        """Test case for verifying tax calculation for a high-income employee."""
        high_income = Decimal('100000.00')
        tax_rate = Decimal('0.2')  # 20% tax rate
        expected_tax = high_income * tax_rate
        actual_tax = self.tax_service.calculate_tax_amount(high_income, tax_rate)
        self.assertEqual(actual_tax, expected_tax, "Tax calculation for high-income employee is incorrect.")

if __name__ == '__main__':
    unittest.main()
