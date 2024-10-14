import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

import unittest
from dao.validation_service import ValidationService

class TestVerifyErrorHandling(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.validation_service = ValidationService()

    def test_verify_error_handling_for_invalid_employee_data(self):
        """Test case for ensuring system handles invalid employee data gracefully."""
        invalid_employee_data = (
            "",  # First Name is empty
            "Smith",  # Last Name
            "1985-05-20",  # Date of Birth
            "M",  # Gender
            "invalid-email",  # Invalid email address
            "123",  # Invalid phone number
            "123 Main St",  # Address
            "Engineer",  # Position
            "2024-01-01"  # Joining Date
        )
        with self.assertRaises(ValueError):
            self.validation_service.validate_employee_data(invalid_employee_data)

if __name__ == '__main__':
    unittest.main()
