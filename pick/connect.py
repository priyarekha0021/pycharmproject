# Create Database
import mysql.connector as conn
mydb = conn.connect(
        user='root',
        password='Rekhapriya@12345',
        host='localhost',
        port=3306
)

sql = 'CREATE DATABASE python_db'
myc = mydb.cursor()
myc.execute(sql)
myc.close()

