import csv
import constant
import mysql.connector
from mysql.connector import errorcode

class UsersInCsv:
    
    def __init__(self):
        self.cnx = mysql.connector.connect(host=constant.DB_HOST,user=constant.DB_USERNAME,password=constant.DB_PASSWORD,database="python")
    
    def write(self):
        with open('users.csv', 'w', newline='') as file:
            cursor = self.cnx.cursor()
            cursor.execute("SELECT * FROM users")
            writer = csv.writer(file)
            for user in cursor:
                writer.writerow([user[0], user[1], user[2]])

u = UsersInCsv()
u.write()

            
