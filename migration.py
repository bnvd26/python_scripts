import constant
import mysql.connector
from mysql.connector import errorcode

class Migration:
    def __init__(self):
        self.cnx = mysql.connector.connect(host=constant.DB_HOST,user=constant.DB_USERNAME,password=constant.DB_PASSWORD)

    def create_database(self):
        myCursor = self.cnx.cursor()
        myCursor.execute("CREATE DATABASE python")
        myCursor.execute("USE python")
        myCursor.execute("CREATE TABLE users (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(100), email VARCHAR(100) )")

m = Migration()
m.create_database()
    