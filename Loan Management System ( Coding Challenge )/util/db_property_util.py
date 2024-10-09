class DBPropertyUtil:
    @staticmethod
    def get_db_conn_str():
        return ('Driver={SQL Server};'
                'Server=LAPTOP-6VDH2AJJ\SQLEXPRESS;'
                'Database=LoanManagementSystem;'
                'Trusted_Connection=yes;')
            
