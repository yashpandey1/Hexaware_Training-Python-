import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\PayXpert")

from dao.IEmployeeServiceImpl import EmployeeServiceImpl
from dao.IPayrollServiceImpl import PayrollServiceImpl
from dao.ITaxServiceImpl import TaxServiceImpl
from dao.IFinancialRecordServiceImpl import FinancialRecordServiceImpl

from exception.PayrollGenerationException import PayrollGenerationException
from exception.EmployeeNotFoundException import EmployeeNotFoundException
from exception.TaxCalculationException import TaxCalculationException

from dao.validation_service import ValidationService


class MainModule:
    def __init__(self):
        self.employee_service = EmployeeServiceImpl()
        self.payroll_service = PayrollServiceImpl()
        self.tax_service = TaxServiceImpl()
        self.financial_record_service = FinancialRecordServiceImpl()

    def display_menu(self):
        print("\n--- PayXpert Payroll Management System ---")
        print("1. Employee Management")
        print("2. Payroll Processing")
        print("3. Tax Calculation")
        print("4. Financial Reporting")
        print("5. Exit")
        choice = input("Enter your choice: ")
        return choice

    def employee_management_menu(self):
        print("\n--- Employee Management ---")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. View All Employees")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        return choice

    def payroll_processing_menu(self):
        print("\n--- Payroll Processing ---")
        print("1. Generate Payroll")
        print("2. View Payroll by ID")
        print("3. View Payrolls for Employee")
        print("4. View Payrolls for Period")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        return choice

    def tax_calculation_menu(self):
        print("\n--- Tax Calculation ---")
        print("1. Calculate Tax")
        print("2. View Tax by ID")
        print("3. View Taxes for Employee")
        print("4. View Taxes for Year")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        return choice

    def financial_reporting_menu(self):
        print("\n--- Financial Reporting ---")
        print("1. Add Financial Record")
        print("2. View Financial Record by ID")
        print("3. View Financial Records for Employee")
        print("4. View Financial Records for Date")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        return choice

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == "1":
                self.handle_employee_management()
            elif choice == "2":
                self.handle_payroll_processing()
            elif choice == "3":
                self.handle_tax_calculation()
            elif choice == "4":
                self.handle_financial_reporting()
            elif choice == "5":
                print("Exiting the system. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    def handle_employee_management(self):
        while True:
            choice = self.employee_management_menu()
            if choice == "1":
                employee_data = (
                    input("First Name: "),
                    input("Last Name: "),
                    input("Date of Birth (YYYY-MM-DD): "),
                    input("Gender: "),
                    input("Email: "),
                    input("Phone Number: "),
                    input("Address: "),
                    input("Position: "),
                    input("Joining Date (YYYY-MM-DD): ")
                )
                termination_date = input("Termination Date (YYYY-MM-DD, optional): ")
                termination_date = termination_date if termination_date.strip() else None


                try:            
                    ValidationService.validate_employee_data(employee_data) #addition statement
                    self.employee_service.add_employee(employee_data, termination_date)
                
                except ValueError as ve:
                    print(f"Error: {ve}")
            
            
            elif choice == "2":
                employee_id = input("Enter Employee ID: ")
                try:
                    employee = self.employee_service.get_employee_by_id(employee_id)
                    print(employee)
                except EmployeeNotFoundException as e:
                    print(e)
            elif choice == "3":
                employee_data = (
                    input("First Name: "),
                    input("Last Name: "),
                    input("Date of Birth (YYYY-MM-DD): "),
                    input("Gender: "),
                    input("Email: "),
                    input("Phone Number: "),
                    input("Address: "),
                    input("Position: "),
                    input("Joining Date (YYYY-MM-DD): "),
                    input("Employee ID: ")
                )
                self.employee_service.update_employee(employee_data)
                print("Employee updated successfully.")
            elif choice == "4":
                employee_id = input("Enter Employee ID to delete: ")
                self.employee_service.remove_employee(employee_id)
            elif choice == "5":
                employees = self.employee_service.get_all_employees()
                for emp in employees:
                    print(emp)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

    def handle_payroll_processing(self):
        while True:
            choice = self.payroll_processing_menu()
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                start_date = input("Enter Pay Period Start Date (YYYY-MM-DD): ")
                end_date = input("Enter Pay Period End Date (YYYY-MM-DD): ")
                basic_salary = float(input("Enter Basic Salary: "))
                overtime_pay = float(input("Enter Overtime Pay: "))
                deductions = float(input("Enter Deductions: "))
                try:
                    self.payroll_service.generate_payroll(employee_id, start_date, end_date, basic_salary, overtime_pay, deductions)
                    print("Payroll generated successfully.")
                except PayrollGenerationException as e:
                    print(e)
            elif choice == "2":
                payroll_id = input("Enter Payroll ID: ")
                payroll = self.payroll_service.get_payroll_by_id(payroll_id)
                if payroll:
                    print(payroll)
                else:
                    print("Payroll not found.")
            elif choice == "3":
                employee_id = input("Enter Employee ID: ")
                payrolls = self.payroll_service.get_payrolls_for_employee(employee_id)
                for payroll in payrolls:
                    print(payroll)
            elif choice == "4":
                start_date = input("Enter Start Date (YYYY-MM-DD): ")
                end_date = input("Enter End Date (YYYY-MM-DD): ")
                payrolls = self.payroll_service.get_payrolls_for_period(start_date, end_date)
                for payroll in payrolls:
                    print(payroll)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def handle_tax_calculation(self):
        while True:
            choice = self.tax_calculation_menu()
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                tax_year = input("Enter Tax Year: ")
                try:
                    self.tax_service.calculate_tax(employee_id, tax_year)
                    print("Tax calculated successfully.")
                except TaxCalculationException as e:
                    print(e)
            elif choice == "2":
                tax_id = input("Enter Tax ID: ")
                tax = self.tax_service.get_tax_by_id(tax_id)
                if tax:
                    print(tax)
                else:
                    print("Tax record not found.")
            elif choice == "3":
                employee_id = input("Enter Employee ID: ")
                taxes = self.tax_service.get_taxes_for_employee(employee_id)
                for tax in taxes:
                    print(tax)
            elif choice == "4":
                tax_year = input("Enter Tax Year: ")
                taxes = self.tax_service.get_taxes_for_year(tax_year)
                for tax in taxes:
                    print(tax)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

    def handle_financial_reporting(self):
        while True:
            choice = self.financial_reporting_menu()
            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                description = input("Enter Description: ")
                amount = float(input("Enter Amount: "))
                record_type = input("Enter Record Type (income/expense): ")
                self.financial_record_service.add_financial_record(employee_id, description, amount, record_type)
                print("Financial record added successfully.")
            elif choice == "2":
                record_id = input("Enter Financial Record ID: ")
                record = self.financial_record_service.get_financial_record_by_id(record_id)
                if record:
                    print(record)
                else:
                    print("Financial record not found.")
            elif choice == "3":
                employee_id = input("Enter Employee ID: ")
                records = self.financial_record_service.get_financial_records_for_employee(employee_id)
                for record in records:
                    print(record)
            elif choice == "4":
                record_date = input("Enter Date (YYYY-MM-DD): ")
                records = self.financial_record_service.get_financial_records_for_date(record_date)
                for record in records:
                    print(record)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()