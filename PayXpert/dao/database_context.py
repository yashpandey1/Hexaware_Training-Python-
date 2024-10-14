import pyodbc

class DatabaseContext:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def get_connection(self):
        """Establish a new database connection."""
        try:
            if not self.connection or self.connection.closed:
                self.connection = pyodbc.connect(
                    f"DRIVER={{SQL Server}};"
                    f"SERVER={self.server};"
                    f"DATABASE={self.database};"
                    f"UID={self.username};"
                    f"PWD={self.password};"
                )
            return self.connection
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            raise

    def close_connection(self):
        """Close the database connection."""
        if self.connection and not self.connection.closed:
            self.connection.close()

    def __enter__(self):
        """Support with-statement for automatic connection handling."""
        return self.get_connection()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close connection when exiting the with-statement."""
        self.close_connection()
