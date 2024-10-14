import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

class ReportGenerator:
    def __init__(self, db_context):
        self.db_context = db_context

    def generate_payroll_report(self, employee_id=None):
        """Generates a payroll report for a specific employee or all employees."""
        try:
            with self.db_context as connection:
                cursor = connection.cursor()
                if employee_id:
                    cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
                else:
                    cursor.execute("SELECT * FROM Payroll")

                rows = cursor.fetchall()
                report = []
                for row in rows:
                    report.append({
                        "PayrollID": row[0],
                        "EmployeeID": row[1],
                        "PayPeriodStartDate": row[2],
                        "PayPeriodEndDate": row[3],
                        "BasicSalary": row[4],
                        "OvertimePay": row[5],
                        "Deductions": row[6],
                        "NetSalary": row[7]
                    })
                return report
        except Exception as e:
            print(f"Error generating payroll report: {e}")
            raise

    def generate_tax_report(self, tax_year=None):
        """Generates a tax report for a specific year or all years."""
        try:
            with self.db_context as connection:
                cursor = connection.cursor()
                if tax_year:
                    cursor.execute("SELECT * FROM Tax WHERE TaxYear = ?", (tax_year,))
                else:
                    cursor.execute("SELECT * FROM Tax")

                rows = cursor.fetchall()
                report = []
                for row in rows:
                    report.append({
                        "TaxID": row[0],
                        "EmployeeID": row[1],
                        "TaxYear": row[2],
                        "TaxableIncome": row[3],
                        "TaxAmount": row[4]
                    })
                return report
        except Exception as e:
            print(f"Error generating tax report: {e}")
            raise

    def generate_financial_record_report(self, employee_id=None, record_type=None):
        """Generates a financial record report filtered by employee and/or record type."""
        try:
            with self.db_context as connection:
                cursor = connection.cursor()
                query = "SELECT * FROM FinancialRecord WHERE 1=1"
                params = []

                if employee_id:
                    query += " AND EmployeeID = ?"
                    params.append(employee_id)
                if record_type:
                    query += " AND RecordType = ?"
                    params.append(record_type)

                cursor.execute(query, tuple(params))
                rows = cursor.fetchall()
                report = []
                for row in rows:
                    report.append({
                        "RecordID": row[0],
                        "EmployeeID": row[1],
                        "RecordDate": row[2],
                        "Description": row[3],
                        "Amount": row[4],
                        "RecordType": row[5]
                    })
                return report
        except Exception as e:
            print(f"Error generating financial record report: {e}")
            raise
