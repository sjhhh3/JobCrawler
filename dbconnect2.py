import mysql.connector
from mysql.connector import errorcode

config = {
  'host':'jstest.mysql.database.azure.com',
  'port':3306,
  'user':'sjhhh3@jstest',
  'password':'xxxxxxxx',
  'database':'mysql'
}
DB_NAME = 'sjhdb'

try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)
        
def create_table(cursor):
   cursor.execute("USE {}".format(DB_NAME))
   table = (
    "CREATE TABLE `jobs` ("
    "  `ID` int(11) NOT NULL AUTO_INCREMENT,"
    "  `JID` int(11) NOT NULL,"
    "  `NAME` varchar(255) NOT NULL,"
    "  `LOC` varchar(255) NOT NULL,"
    "  `DEP` varchar(255) NOT NULL,"
    "  `ABB` varchar(255) NOT NULL,"
    "  `DES` text(5000) NOT NULL,"
    "  `REQ` text(5000) NOT NULL,"
    "  `PRF` text(5000) NOT NULL,"
    "  PRIMARY KEY (`ID`)"
    ") ENGINE=InnoDB")
   cursor.execute(table)
   cursor.close()

def insert_date(cursor):
   query = ("INSERT INTO jobs "
       "(JID, NAME, LOC, DEP, ABB, DES, REQ, PRF) "
       "VALUES ('1000', 'test', 'test', 'test', 'test', 'test', 'test', 'test')")
   cursor.execute(query)

cursor = conn.cursor()
cursor.execute("USE {}".format(DB_NAME))
#create_database(cursor)
#create_table(cursor)
#insert_date(cursor)
query = ("SELECT * FROM jobs")
cursor.execute(query)
for a in cursor:
   print(a)
conn.close()
