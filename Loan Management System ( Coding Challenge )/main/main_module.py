import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\Loan Management System ( Coding Challenge )")

from entity.customer import Customer
from entity.loan import Loan
from entity.carloan import CarLoan
from entity.homeloan import HomeLoan
from dao.loan_repository_impl import LoanRepository
from exception.invalid_loan_exception import CustomerNotFoundException
from exception.invalid_loan_exception import LoanNotFoundException

def main():
    lp = LoanRepository()
    while True:
        print("\n----------Main Menu----------")
        print("Press-1 to Apply for a Loan")
        print("Press-2 to Check Loan Status")
        print("Press-3 to Calculate Interest")
        print("Press-4 to Calculate EMI")
        print("Press-5 to Loan Repayment")
        print("Press-6 to View All Loans")  
        print("Press-7 to View Loan by ID")  
        print("Press-8 to View Customer by ID")  
        print("Press-9 to Exit")  
        ch = int(input())
        
        if ch == 1:
            c = int(input('\nEnter Your Customer ID : '))
            cust = lp.get_customer_by_id(c)

            if not cust:
                n = input('Enter Your Name : ')
                eml = input('Enter Your Email Address : ')
                pno = input("Enter Your Phone Number : ")
                add = input('Enter Your Address : ')
                cscore = int(input('Enter Your Credit Score : '))
                c = Customer(customer_id=None, name=n, email=eml, phone=pno, address=add, credit_score=cscore)
                customer_id = c.insert_new_customer()
                
                if customer_id is None:
                    print("Error: Could not insert customer.")
                    return
            else:
                customer_id = cust.customer_id

            pa = int(input('Enter the Principal Amount : '))
            ltm = int(input('Enter the Loan Term in Months : '))
            lty = input('Enter the Loan Type (CarLoan/HomeLoan) : ')
            interest_rate = float(input("Enter Interest Rate: "))

            if lty == "HomeLoan":
                prop_addr = input("Enter the Property Address: ")
                prop_val = int(input("Enter the Property Value: "))
                loan = HomeLoan(loan_id=None, customer_id=customer_id, principal_amount=pa, interest_rate=interest_rate, 
                            loan_term=ltm, loan_type=lty, loan_status="Pending", property_address=prop_addr, property_value=prop_val)
            elif lty == "CarLoan":
                car_model = input("Enter the Car Model: ")
                car_val = int(input("Enter the Car Value: "))
                loan = CarLoan(loan_id=None, customer_id=customer_id, principal_amount=pa, interest_rate=interest_rate, 
                            loan_term=ltm, loan_type=lty, loan_status="Pending", car_model=car_model, car_value=car_val)
            else:
                loan = Loan(loan_id=None, customer_id=customer_id, principal_amount=pa, interest_rate=interest_rate, 
                            loan_term=ltm, loan_type=lty, loan_status="Pending")

            try:
                decision = input("Are Your Sure You Want to apply for the loan (y/n): ")
                if decision == 'y':
                    loan_id = lp.apply_loan(loan)
                    print(f"Loan applied successfully for Customer ID: {customer_id} and Loan Id {loan_id}")
            except Exception as e:
                print(f"Error applying for loan: {e}")


        elif ch == 2:
            lid = int(input('\nEnter Your Loan ID : '))
            lp.loan_status(lid)

        elif ch == 3:
            lid = int(input('\nEnter Your Loan ID : '))
            print(f"Total Interest of this Loan Amounts to : {lp.calculate_interest(lid)}")

        elif ch == 4:
            lid = int(input('\nEnter Your Loan ID : '))
            print(f"The EMI amounts to : {lp.calculate_emi(lid)}")

        elif ch == 5:
            lid = int(input('\nEnter Your Loan ID : '))
            am = int(input('Enter Your Total Amount : '))
            lp.loan_repayment(lid, am)

        elif ch == 6:
            print("\nDisplaying All Loans:")
            lp.get_all_loans()

        elif ch == 7:
            lid = int(input('\nEnter the Loan ID to view: '))
            loan = lp.get_loan_by_id(lid)
            if loan:
                print(loan)

        elif ch == 8:
            cid = int(input('\nEnter the Customer ID to view: '))
            customer = lp.get_customer_by_id(cid)
            if customer:
                print(customer)

        elif ch == 9:
            print("\n----------Thank You----------\n")
            break

        else:
            print('\nInvalid Choice!!\nPlease Try Again...\n')

if __name__ == "__main__":
    main()
