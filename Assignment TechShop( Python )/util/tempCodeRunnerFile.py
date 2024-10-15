
import sys
sys.path.append("C:\\Users\\yyash\\Documents\\hexaware\\Assignment TechShop( Python )")

import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_db_conn():
        conn_str = DBPropertyUtil.get_db_conn_str()
        return pyodbc.connect(conn_str)