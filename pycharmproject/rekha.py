import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="Rekhapriya@12345")

print("connect")

# Create Database

mydb = conn.connect(
        user='root',
        password='Rekhapriya@12345',
        host='localhost',
        port=3306
)

sql = 'CREATE DATABASE yz'
myc = mydb.cursor()
myc.execute(sql)
myc.close()

def deco(fx):
    def inner():
        print('hello rekha')
        fx()
        print('hii priya')
        return inner

    def hello():
        print('hello saurabh')
        deco(hello())



