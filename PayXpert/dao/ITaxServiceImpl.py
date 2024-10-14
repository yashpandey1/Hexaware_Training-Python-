import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

from decimal import Decimal
from dao.ITaxService import ITaxService
from util.db_conn_util import DBConnUtil
from exception.TaxCalculationException import TaxCalculationException


class TaxServiceImpl(ITaxService):
    def calculate_tax(self, employee_id, tax_year):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT BasicSalary FROM Payroll WHERE EmployeeID = ? AND YEAR(PayPeriodEndDate) = ?", (employee_id, tax_year))
            row = cursor.fetchone()
            if not row:
                raise TaxCalculationException("No payroll data found for the given year.")

            taxable_income = Decimal(row[0])
            tax_rate = Decimal(0.2) 
            tax_amount = taxable_income * tax_rate  
            print("Tax is : ", round(tax_amount,2))

            # Insert tax record
            cursor.execute(
                "INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount) "
                "VALUES (?, ?, ?, ?)",
                (employee_id, tax_year, taxable_income, tax_amount)
            )
            connection.commit()
        finally:
            cursor.close()
            connection.close()

    def get_tax_by_id(self, tax_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxID = ?", (tax_id,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def get_taxes_for_employee(self, employee_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Tax WHERE EmployeeID = ?", (employee_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()

    def get_taxes_for_year(self, tax_year):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", (tax_year,))
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()
    def calculate_tax_amount(self, taxable_income, tax_rate):
        """Calculates the tax amount based on taxable income and tax rate."""
        if not isinstance(taxable_income, Decimal) or not isinstance(tax_rate, Decimal):
            raise ValueError("Taxable income and tax rate must be of type Decimal.")
        return taxable_income * tax_rate