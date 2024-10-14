import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

from datetime import datetime
from dao.IEmployeeService import IEmployeeService
from util.db_conn_util import DBConnUtil
from exception.EmployeeNotFoundException import EmployeeNotFoundException


class EmployeeServiceImpl(IEmployeeService):
    # def get_employee_by_id(self, employee_id):
        # try:
        #     connection = DBConnUtil.get_connection()
        #     cursor = connection.cursor()
        #     cursor.execute("SELECT * FROM Employee WHERE EmployeeID = ?", (employee_id,))
        #     row = cursor.fetchone()
        #     if row:
        #         return row
        #     else:
        #         raise EmployeeNotFoundException("Employee not found.")
        # finally:
        #     cursor.close()
        #     connection.close()
    def get_employee_by_id(self, employee_id: int):
        """Fetch employee data by employee ID."""
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Employee WHERE EmployeeID = ?"
            cursor.execute(query, (employee_id,))
            row = cursor.fetchone()

            if row:
                employee_data = {
                    'employee_id': row[0],         # EmployeeID
                    'first_name': row[1],          # FirstName
                    'last_name': row[2],           # LastName
                    'date_of_birth': row[3],       # DateOfBirth
                    'gender': row[4],              # Gender
                    'email': row[5],               # Email
                    'phone_number': row[6],        # PhoneNumber
                    'address': row[7],             # Address
                    'position': row[8],            # Position
                    'joining_date': row[9],        # JoiningDate
                    'termination_date': row[10]
                }
                return employee_data
            
            return EmployeeNotFoundException("Employee not found") 
        except Exception as e:
            print(f"Failed to fetch employee: {e}")
            return None
        finally:
            cursor.close()

    def get_all_employees(self):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Employee")
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()

    def add_employee(self, employee_data, termination_date=None):
        """
        Adds a new employee to the database.
        :param employee_data: Tuple containing employee details.
        :param termination_date: Optional termination date.
        """
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            # Parse the date fields from employee_data
            date_of_birth = datetime.strptime(employee_data[2], "%Y-%m-%d")  # DateOfBirth
            joining_date = datetime.strptime(employee_data[8], "%Y-%m-%d")   # JoiningDate
            termination_date_obj = (
                datetime.strptime(termination_date, "%Y-%m-%d") if termination_date else None
            )

            # Validate that the joining date is not before the date of birth
            if joining_date < date_of_birth:
                raise ValueError("Joining date cannot be earlier than date of birth.")

            # Validate that the termination date (if provided) is not before the joining date
            if termination_date_obj and termination_date_obj < joining_date:
                raise ValueError("Termination date cannot be earlier than joining date.")

            # Proceed with the database insertion if validations pass
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()

            # Insert the employee data, including TerminationDate
            cursor.execute(
                "INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                employee_data + (termination_date,)
            )

            # Fetch the newly inserted EmployeeID
            cursor.execute("SELECT TOP 1 EmployeeID FROM Employee ORDER BY EmployeeID DESC;")
            emp_id = cursor.fetchone()

            # Print the Employee ID of the newly added employee
            print("Employee entered with ID:", emp_id[0])

            # Commit the changes
            connection.commit()

        except ValueError as ve:
            # Handle validation errors specifically
            print(f"Validation Error: {ve}")

        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred: {e}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    # def add_employee(self, employee_data, termination_date=None):
    #     try:
    #         connection = DBConnUtil.get_connection()
    #         cursor = connection.cursor()
            
    #         # Insert the employee data, including TerminationDate
    #         cursor.execute(
    #             "INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) "
    #             "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    #             employee_data + (termination_date,)
    #         )
            
    #         # Fetch the newly inserted EmployeeID
    #         cursor.execute("SELECT TOP 1 EmployeeID FROM Employee ORDER BY EmployeeID DESC;")
    #         emp_id = cursor.fetchone()
            
    #         # Print the Employee ID of the newly added employee
    #         print("Employee entered with ID:", emp_id[0])
            
    #         # Commit the changes
    #         connection.commit()
    #     except Exception as e:
    #         # Handle exceptions
    #         print(f"An error occurred: {e}")
    #     finally:
    #         # Close the cursor and connection
    #         cursor.close()
    #         connection.close()

    def update_employee(self, employee_data):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE Employee SET FirstName=?, LastName=?, DateOfBirth=?, Gender=?, Email=?, PhoneNumber=?, Address=?, Position=?, JoiningDate=? "
                "WHERE EmployeeID=?",
                employee_data
            )
            connection.commit()
        finally:
            cursor.close()
            connection.close()

    def remove_employee(self, employee_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()

            payroll_deleted = cursor.execute("DELETE FROM Payroll WHERE EmployeeID = ?", (employee_id,)).rowcount
            loan_deleted = cursor.execute("DELETE FROM FinancialRecord WHERE EmployeeID = ?", (employee_id,)).rowcount
            tax_deleted = cursor.execute("DELETE FROM Tax WHERE EmployeeID = ?", (employee_id,)).rowcount
            
            # Delete from the main Employee table
            employee_deleted = cursor.execute("DELETE FROM Employee WHERE EmployeeID = ?", (employee_id,)).rowcount
            
            connection.commit()

            if employee_deleted > 0:
                print(f"Successfully deleted Employee with ID: {employee_id}.")
            else:
                print(f"No employee found with ID: {employee_id}.")
                
        except Exception as e:

            print(f"An error occurred: {e}")
        finally:

            cursor.close()
            connection.close()