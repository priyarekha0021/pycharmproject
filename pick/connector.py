# Connect Database
import mysql.connector as conn

try:
    mydb =conn.connect(
        user='root',
        password='Rekhapriya@12345',
        host='localhost',
        database='pddb',
        port=3306
    )
    if (mydb.is_connected()):
        print('Connected')
except:
    print('Unable to Connect')

