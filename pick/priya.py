# show Database
import mysql.connector as conn

mydb = conn.connect(
        user='root',
        password='Rekhapriya@12345',
        host='localhost',
        port=3306
)
sql = 'SHOW DATABASES'
myc = mydb.cursor()
myc.execute(sql)
for d in myc:
    print(d)
myc.close()
