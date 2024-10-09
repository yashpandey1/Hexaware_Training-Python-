import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\Loan Management System ( Coding Challenge )")

import pyodbc
from util.db_conn_util import DBConnUtil
from entity.loan import Loan
from entity.customer import Customer
from dao.loan_repository import ILoanRepository
from exception.invalid_loan_exception import CustomerNotFoundException
from exception.invalid_loan_exception import LoanNotFoundException

class LoanRepository(ILoanRepository):

    def __init__(self):
        self.conn = DBConnUtil.get_db_conn()
        self.cursor = self.conn.cursor()

    def apply_loan(self, loan):
        try:
            # Confirm the customer exists
            self.cursor.execute("SELECT COUNT(*) FROM Customer WHERE customer_id = ?", (loan.customer_id,))
            if self.cursor.fetchone()[0] == 0:
                raise CustomerNotFoundException()

            query = """
                INSERT INTO Loan 
                (customer_id, principal_amount, interest_rate, loan_term, loan_type, loan_status, propertyAddress, propertyValue, carModel, carValue)
                OUTPUT INSERTED.loan_id
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            # Prepare the data based on loan type
            if loan.loan_type == "HomeLoan":
                values = (loan.customer_id, loan.principal_amount, loan.interest_rate, loan.loan_term, loan.loan_type, loan.loan_status, 
                        loan.property_address, loan.property_value, None, None)
            elif loan.loan_type == "CarLoan":
                values = (loan.customer_id, loan.principal_amount, loan.interest_rate, loan.loan_term, loan.loan_type, loan.loan_status, 
                        None, None, loan.car_model, loan.car_value)
            else:
                values = (loan.customer_id, loan.principal_amount, loan.interest_rate, loan.loan_term, loan.loan_type, loan.loan_status, 
                        None, None, None, None)

            self.cursor.execute(query, values)
            loan_id_row = self.cursor.fetchone()
            loan_id = loan_id_row[0] if loan_id_row else None

            if loan_id:
                self.conn.commit()
                print(f"Loan application successful. Loan ID: {loan_id}")
                return loan_id
            else:
                raise LoanNotFoundException
            
        except Exception as e:
            print(f"Error applying loan: {e}")
            self.conn.rollback()



    def calculate_interest(self, loan_id):
        try:
            self.cursor.execute("SELECT principal_amount, interest_rate, loan_term FROM Loan WHERE loan_id = ?", (loan_id,))
            loan = self.cursor.fetchone()
            if loan:
                principal, interest_rate, loan_term = loan
                interest = (principal * interest_rate * loan_term) / 12
                return interest
            else:
                raise LoanNotFoundException
        except Exception as e:
            print(f"Error calculating interest: {e}")

    def loan_status(self, loan_id):
        try:
            
            self.cursor.execute("SELECT customer_id FROM Loan WHERE loan_id = ?", (loan_id,))
            loan = self.cursor.fetchone()
            
            if loan:
                customer_id = loan[0]
                print(f"Customer ID: {customer_id}")
                               
                self.cursor.execute("SELECT COUNT(*) FROM Customer WHERE customer_id = ?", (customer_id,))
                customer_exists = self.cursor.fetchone()[0]               
                if customer_exists == 0:
                    raise Exception(f"Customer with ID {customer_id} does not exist in the database.")

                self.cursor.execute("SELECT credit_score FROM Customer WHERE customer_id = ?", (customer_id,))
                result = self.cursor.fetchone()
                
                if result:
                    credit_score = result[0]
                    print(f"Credit Score: {credit_score}")  # Log Credit Score

                    # Determine loan status based on credit score
                    status = "Approved" if credit_score > 650 else "Rejected"
                    self.cursor.execute("UPDATE Loan SET loan_status = ? WHERE loan_id = ?", (status, loan_id))
                    self.conn.commit()
                    print(f"Loan status updated: {status}")
                else:
                    raise Exception("Customer credit score not found")
            else:
                raise Exception(f"Loan with ID {loan_id} not found.")
                
        except Exception as e:
            print(f"Error checking loan status: {e}")
    

    def calculate_emi(self, loan_id):
        try:
            self.cursor.execute("SELECT principal_amount, interest_rate, loan_term FROM Loan WHERE loan_id = ?", (loan_id,))
            loan = self.cursor.fetchone()
            if loan:
                P, R, N = loan[0], loan[1] / 12 / 100, loan[2]
                EMI = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)
                return int(EMI)
            else:
                raise Exception("Loan not found")
        except Exception as e:
            print(f"Error calculating EMI: {e}")

    def loan_repayment(self, loan_id, amount):
        try:
            self.cursor.execute("SELECT loan_id, principal_amount, loan_status FROM Loan WHERE loan_id = ?", (loan_id,))
            loan = self.cursor.fetchone()
            if loan:
                loan_status = loan[2]
                if loan_status == "Approved":
                    emi_amount = self.calculate_emi(loan_id)
                    if amount < emi_amount:
                        print("Payment rejected: Amount is less than the EMI.")
                    else:
                    
                        new_principal = loan[1] - amount
                        if new_principal <= 0:
                            self.cursor.execute("UPDATE Loan SET principal_amount = 0, loan_status = 'Completed' WHERE loan_id = ?", (loan_id,))
                            print("Loan repayment completed. Loan status updated to 'Completed'.")
                        else:
                            self.cursor.execute("UPDATE Loan SET principal_amount = ? WHERE loan_id = ?", (new_principal, loan_id))
                            print(f"Loan repayment processed. Remaining principal amount: {new_principal}")
                        self.conn.commit()
                else:
                    print("Payment rejected: Loan is not approved.")
            else:
                raise Exception("Loan not found")
        except Exception as e:
            print(f"Error processing loan repayment: {e}")

    
    def get_all_loans(self):
        try:
            self.cursor.execute("SELECT * FROM Loan")
            loans = self.cursor.fetchall()
            print("Loan id , CustomerID, LoanAmount, Months, Rate, Category, Status, PropertyAddress, PropertyValue, CarModel, CarValue")
            for loan in loans:
                print(loan)
            return loans
        except Exception as e:
            print(f"Error retrieving loans: {e}")

    def get_loan_by_id(self, loan_id):
        try:
            self.cursor.execute("SELECT * FROM Loan WHERE loan_id = ?", (loan_id,))
            loan = self.cursor.fetchone()
            print("Loan id , CustomerID, LoanAmount, Months, Rate, Category, Status, PropertyAddress, PropertyValue, CarModel, CarValue")
            if loan:
                return loan
            else:
                raise Exception("Loan not found")
        except Exception as e:
            print(f"Error retrieving loan: {e}")


    def get_customer_by_id(self, cid):
        try:
            self.cursor.execute("SELECT * FROM Customer WHERE customer_id = ?", (cid,))
            customer = self.cursor.fetchone()
            if customer:
                return customer
            else:
                raise CustomerNotFoundException
        except Exception as e:
            print(f"Error retrieving customer: {e}")