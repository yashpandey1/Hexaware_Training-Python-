
class Payroll:
    def __init__(self, payroll_id=None, employee_id=None, pay_period_start_date=None,
                 pay_period_end_date=None, basic_salary=0.0, overtime_pay=0.0,
                 deductions=0.0, net_salary=0.0):
        self.__payroll_id = payroll_id
        self.__employee_id = employee_id
        self.__pay_period_start_date = pay_period_start_date
        self.__pay_period_end_date = pay_period_end_date
        self.__basic_salary = basic_salary
        self.__overtime_pay = overtime_pay
        self.__deductions = deductions
        self.__net_salary = net_salary

    # Getters and Setters
    def get_payroll_id(self):
        return self.__payroll_id

    def set_payroll_id(self, payroll_id):
        self.__payroll_id = payroll_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_pay_period_start_date(self):
        return self.__pay_period_start_date

    def set_pay_period_start_date(self, pay_period_start_date):
        self.__pay_period_start_date = pay_period_start_date

    def get_pay_period_end_date(self):
        return self.__pay_period_end_date

    def set_pay_period_end_date(self, pay_period_end_date):
        self.__pay_period_end_date = pay_period_end_date

    def get_basic_salary(self):
        return self.__basic_salary

    def set_basic_salary(self, basic_salary):
        self.__basic_salary = basic_salary

    def get_overtime_pay(self):
        return self.__overtime_pay

    def set_overtime_pay(self, overtime_pay):
        self.__overtime_pay = overtime_pay

    def get_deductions(self):
        return self.__deductions

    def set_deductions(self, deductions):
        self.__deductions = deductions

    def get_net_salary(self):
        return self.__net_salary

    def set_net_salary(self, net_salary):
        self.__net_salary = net_salary
