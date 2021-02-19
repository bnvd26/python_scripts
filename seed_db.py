from faker import Faker
import constant
import mysql.connector
from mysql.connector import errorcode

class SeedDb:
    def __init__(self):
        self.cnx = mysql.connector.connect(host=constant.DB_HOST,user=constant.DB_USERNAME,password=constant.DB_PASSWORD,database="python")
        self.faker = Faker()

    def test(self):
        print(self.faker.name())

    def seed_users(self):
        myCursor = self.cnx.cursor()
        
        for i in range(100):
            sql = "INSERT INTO users(name, email) VALUES('" + self.faker.name() + "', '" + self.faker.email() + "')"
            myCursor.execute(sql)
            self.cnx.commit()

a = SeedDb()
a.seed_users()