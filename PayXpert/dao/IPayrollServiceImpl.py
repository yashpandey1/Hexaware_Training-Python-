import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

from dao.IPayrollService import IPayrollService
from util.db_conn_util import DBConnUtil
from exception.PayrollGenerationException import PayrollGenerationException
from dao.validation_service import ValidationService


class PayrollServiceImpl(IPayrollService):
    def generate_payroll_test(self, employee_id, start_date, end_date, basic_salary, overtime_pay, deductions):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            net_salary = basic_salary + overtime_pay - deductions
            ValidationService.validate_salary_data(basic_salary, overtime_pay, deductions)
            cursor.execute(
                "INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (employee_id, start_date, end_date, basic_salary, overtime_pay, deductions, net_salary)
            )
            connection.commit()
            return net_salary
        except Exception as e:
            raise PayrollGenerationException(f"Failed to generate payroll: {e}")
        finally:
            cursor.close()
            connection.close()
    
    
    def generate_payroll(self, employee_id, start_date, end_date, basic_salary, overtime_pay, deductions):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()

            net_salary = basic_salary + overtime_pay - deductions

            cursor.execute(
                "INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (employee_id, start_date, end_date, basic_salary, overtime_pay, deductions, net_salary)
            )
            connection.commit()
            print("Payroll record created successfully.")
            
        except Exception as e:
            raise PayrollGenerationException(f"Failed to generate payroll: {e}")
        finally:
            cursor.close()
            connection.close()

    def get_payroll_by_id(self, payroll_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE PayrollID = ?", (payroll_id,))
            row = cursor.fetchone()
            if row:
                return {
                    "PayrollID": row[0],
                    "EmployeeID": row[1],
                    "PayPeriodStartDate": row[2],
                    "PayPeriodEndDate": row[3],
                    "BasicSalary": row[4],
                    "OvertimePay": row[5],
                    "Deductions": row[6],
                    "NetSalary": row[7]
                }
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def get_payrolls_for_employee(self, employee_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = ?", (employee_id,))
            rows = cursor.fetchall()
            payrolls = []
            for row in rows:
                payrolls.append({
                    "PayrollID": row[0],
                    "EmployeeID": row[1],
                    "PayPeriodStartDate": row[2],
                    "PayPeriodEndDate": row[3],
                    "BasicSalary": row[4],
                    "OvertimePay": row[5],
                    "Deductions": row[6],
                    "NetSalary": row[7]
                })
            return payrolls
        finally:
            cursor.close()
            connection.close()

    def get_payrolls_for_period(self, start_date, end_date):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM Payroll WHERE PayPeriodStartDate >= ? AND PayPeriodEndDate <= ?",
                (start_date, end_date)
            )
            rows = cursor.fetchall()
            payrolls = []
            for row in rows:
                payrolls.append({
                    "PayrollID": row[0],
                    "EmployeeID": row[1],
                    "PayPeriodStartDate": row[2],
                    "PayPeriodEndDate": row[3],
                    "BasicSalary": row[4],
                    "OvertimePay": row[5],
                    "Deductions": row[6],
                    "NetSalary": row[7]
                })
            return payrolls
        finally:
            cursor.close()
            connection.close()
