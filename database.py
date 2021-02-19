import constant
from ApiService import ApiService
import mysql.connector
from mysql.connector import errorcode

class Database:
    def __init__(self, name):
        self.name = name
        self.cnx = mysql.connector.connect(host=constant.DB_HOST,user=constant.DB_USERNAME,password=constant.DB_PASSWORD)

    def check_connection(self):
        try:
            print('Connection to the database is OK')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print('Connection is not OK : ')
                print(err)
        else:
            self.cnx.close()


    # def show_database_tables(database: str, table: str):
    #     myCursor = connection.cursor()
    #     myCursor.execute("USE " + database)
    #     myCursor.execute("SELECT * from " + table)
    #     for x in myCursor:
    #     print(x)

    def test(self): 
        print(self.name)

# Instanciate the class
db = Database('Benjamin')
# p1.check_connection();
db.test();

# Call to Another class method
ApiService.get()

