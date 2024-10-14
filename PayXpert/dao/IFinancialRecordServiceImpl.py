import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

from dao.IFinancialRecordService import IFinancialRecordService
from util.db_conn_util import DBConnUtil

class FinancialRecordServiceImpl(IFinancialRecordService):
    def add_financial_record(self, employee_id, description, amount, record_type):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType) "
                "VALUES (?, GETDATE(), ?, ?, ?)",
                (employee_id, description, amount, record_type)
            )
            connection.commit()
        finally:
            cursor.close()
            connection.close()

    def get_financial_record_by_id(self, record_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID = ?", (record_id,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                return None
        finally:
            cursor.close()
            connection.close()

    def get_financial_records_for_employee(self, employee_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()

    def get_financial_records_for_date(self, record_date):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE RecordDate = ?", (record_date,))
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()