

class Employee():
    def __init__(self, employee_id, first_name, last_name, date_of_birth, gender, email, phone_number, address, position, joining_date, termination_date):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.position = position
        self.joining_date = joining_date
        self.termination_date = termination_date

    def calculate_age(self):
        from datetime import datetime
        if self.__date_of_birth:
            today = datetime.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.email = email

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.__position = position

    def get_joining_date(self):
        return self.__joining_date

    def set_joining_date(self, joining_date):
        self.joining_date = joining_date

    def get_termination_date(self):
        return self.termination_date

    def set_termination_date(self, termination_date):
        self.termination_date = termination_date

