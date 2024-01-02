# Example 1
class Myclass(object):
	def show(self):
		print("I am a Method")

x = Myclass()
x.show()
# Example 2
class Myclass:
	def show(self):
		print("I am a Method")

x = Myclass()
x.show()


# Example 3
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    def show_model(self):
        print("Model:", self.model)


# Creating Object of Class
realme = Mobile()

# Accessing Variable from outside class
print(realme.model)

# Assign Variable a new value
realme.model = 'RealMe Pro2'

print(realme.model)

# Accessing Method from outside class
realme.show_model()


# Example 4
class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    def show_model(self):
        price = 1000  # Local Varaible
        print("Model:", self.model, "and Price:", price)


realme = Mobile()

# Accessing Method from outside Class
realme.show_model()


# Example 5
class Mobile:
    # Constructor
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        price = p  # Local Varaible
        print("Model:", self.model, "and Price:", price)


# Passing Argument to Constructor
realme = Mobile('Realme X')

# Accessing Method from outside Class
realme.show_model(1000)


# Example 6
class Mobile:
    # Constructor
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        price = p
        print("Model:", self.model, "and Price:", price)


realme = Mobile('RealMe X')
realme.show_model(1000)
print(id(realme))

realme1 = Mobile('RealMe X')
realme1.show_model(1000)
print(id(realme1))

redmi = Mobile('Redmi 7s')
redmi.show_model(2000)
print(id(redmi))

geek = Mobile('Python')
geek.show_model(49)
print(id(geek))


#constructor
class mobile:
    def __init__(self):
        print("mobile constructor called")
copy = mobile()
#constructor without parameter
class mobile:
    def __init__(self):
        self.model = 'realme'
    def show_model(self):
        print("model:",self.model)
realme = mobile()
realme.show_model()
#constructor with parameter
class mobile:
    def __init__(self,m,v=70):
        self.model = m
        self.valumn = v
    def show_model(self,p):
        price = p   #local varaible
        print("model:",self.model,"price:",price)
        print("valumn:",self.valumn)
#passing argument to constructor
realme = mobile('relame')
#accessing method from outside class
realme.show_model(1000)
#instance variable
class mobile:
    def __init__(self):
     self.model='realme'      #instance variable
    def show_model(self):
        print(self.model)     #Acessing instance variable
realme=mobile()
redmi=mobile()
rekha=mobile()
print(realme.model)
print(redmi.model)
print(rekha.model)
print()
redmi.model='redmi 7s'
print(redmi.model)
#class variable/static variable
class mobile:
    fb = 'yes'       #class variable
    def __init__(self):
     self.model='realme'      #instance variable
    def show_model(self):     #instance method
        print(self.model)     #Acessing instance variable
    @classmethod
    def is_fb(cls):            #class method
      print("finger print:",cls.fb)  #Accessing class variable

realme=mobile()
realme.show_model()
mobile.is_fb()
print()
mobile.fb='no'
mobile.is_fb()

#instance method witrh parameter
class mobile:
    def __init__(self):
     self.model='realme'      #instance variable
    def show_model(self,p):   #instance method
        self.price = p
        print("model:",self.model,"price:",self.price)     #Acessing instance variable
realme=mobile()
redmi=mobile()
realme.show_model(1000)
redmi.show_model(2000)

#class method with parameter
class Mobile:
    fb = 'yes'      #class variable

    @classmethod               #decorator
    def show_model(cls,r):     #class method
        cls.ram = r
        print("fingerprint:",cls.fb)
        print("ram:",cls.ram)

realme = mobile()
Mobile.show_model('4GM')

#static method with parameter

class Mobile:

    @staticmethod               #decorator
    def show_model(m,p):     #static method
        model = m
        price = p

        print("model:", model, "price:",price)

realme = Mobile()
Mobile.show_model('realme',1000)      #calling static method

#passing members of one class to another class

class Student:
  # constructor
  def __init__(self , n , r):       #formal aurgment
     self.name = n
     self.roll = r
  # instance method
  def disp(self):
      print("student name:",self.name)
      print("student roll:",self.roll)
class user:
    #static method
    @staticmethod       #decorator
    def show(s):
        print("user name:",s.name)
        print("user roll:",s.roll)
        s.disp()

# creating object of student class
stu = Student ('rahul',101)     #actual auegment
user.show(stu)


#INHERITANCE
#Single inheritance
class Father:
    money = 1000     #class variable

    def show (self):    #instance method
        print("parent class instance method")

    @classmethod
    def showmoney(cls):
        print("parent class class method :",cls.money)

    @staticmethod
    def stat():
        a = 10
        print("parent class static method:",a)

class Son(Father):
    def disp(self):
        print("child class instance method")
s = Son()
s.disp()
s.show()
s.showmoney()
s.stat()
print()

#constructor in inheritance

class Father:
    def  __init__(self,m):
        self.money= m
        print("father class constructor")
    def show(self):
        print("father class instance method")
class Son(Father):
    def disp(self):
        print("son class instance method ",self.money)
s = Son(1000)
s.show()
s.disp()
print(s.money)
print()

#constructor overiding with parameter
class Father:
    def  __init__(self,m):
        self.money= m
        print("father class constructor")
    def show(self):
        print("father class instance method")
class Son(Father):
    def __init__(self,r):
        self.money = r
        self.car = 'BMW'
        print("son class constructor")
    def disp(self):
        print("son class instance method ",self.money)
s = Son(2000)
s.show()
s.disp()
print(s.money)
print(s.car)
print()

#constructor with super  method

class Father:
    def  __init__(self,m):
        self.money= m
        print("father class constructor")
    def show(self):
        print("father class instance method")
class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)       #calling parent class constructor
        self.job = j
        print("son class constructor")
    def disp(self):
        print("son class instance method ",self.money,self.job)
s = Son(2000,'python')
s.disp()
print()

#multi-level inheritance
class Father:
    def __init__(self):   #use constructor
        print("father class constructor")
    def showF(self):
       print("father class method")
class Son(Father):
    def __init__(self):
        super().__init__()  #calling father class constructor
        print("Son class constructor")
    def showS(self):
       print("son class method")
class GrandSon(Son):
    def __init__(self):
        super().__init__()       #calling son class constructor
        print("Grandson class constructor")
    def showG(self):
       print("Grandson class method")

g = GrandSon()
g.showF()
g.showG()
g.showS()
print()


#hirerchical inheritance
class Father:
    def __init__(self):   #use constructor
        print("father class constructor")
    def showF(self):
       print("father class method")
class Son(Father):
    def __init__(self):
        super().__init__()  #calling father class constructor
        print("Son class constructor")
    def showS(self):
       print("son class method")
class Daughter(Father):
    def __init__(self):
        super().__init__()       #calling son class constructor
        print("Daughter class constructor")
    def showD(self):
       print("Daughter class method")

S = Son()
D = Daughter()
print()

#multiple inheritance
class Father:
    def __init__(self):   #use constructor
        super().__init__()  # calling father class constructor
        print("father class constructor")
    def showF(self):
       print("father class method")
class Mother:
    def __init__(self):      #(MRO)
        super().__init__()  #calling mother class constructor
        print("mother class constructor")
    def showM(self):
       print("son class method")
class Son(Father,Mother):
    def __init__(self):
        super().__init__()       #calling son class constructor
        print("Son class constructor")
    def showS(self):
       print("Daughter class method")

S = Son()
S.showS()
S.showF()
S.showM()
print()
#Polymorphism
#Duck type

class Duck():
    def walk(self):
        print("thapak thapak")
class Hourse():
    def walk(self):
        print("tabdak tabdak")
class Cat():
    def talk(self):
        print("meow meow")
def myfunction(obj):
    obj.walk()

D = Duck()
myfunction(D)
H = Hourse()
myfunction(H)
'''C = Cat()
myfunction(C)'''
print()

#strong type
class Duck():
    def walk(self):
        print("thapak thapak")
class Hourse():
    def walk(self):
        print("tabdak tabdak")
class Cat():
    def talk(self):
        print("meow meow")
def myfunction(obj):
    if hasattr(obj,'walk'):
      obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
D = Duck()
myfunction(D)
H = Hourse()
myfunction(H)
C = Cat()
myfunction(C)


# This Method Overloading Concept is not available in Python
# So it will show error
class Myclass:
    def sum(self, a):
        print("1st Sum Method", a)

    def sum(self):
        print("2nd Sum Method")


obj = Myclass()
obj.sum()



# Method Overloading
class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = 'Provide at least Two Numbers'
        return s


obj = Myclass()
print(obj.sum(10, 20, 30))


# Method Overriding 1
class Add:
    def result(self, a, b):
        print('Addition:', a + b)


class Multi(Add):
    def result(self, a, b):
        print('Multiplication:', a * b)


m = Multi()
m.result(10, 20)

m = Add()
m.result(10, 20)


# Method Overriding 2
class Add:
    def result(self, a, b):
        print('Addition:', a + b)


class Multi(Add):
    def result(self, a, b):
        super().result(10, 20)  # Calling Parent Class's Method
        print('Multiplication:', a * b)


m = Multi()
m.result(10, 20)


# Operator Overloading
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


class B:
    def __init__(self, x):
        self.x = x


a = A(100)
b = B(200)
print(a + b)  # A.__add__(a, b)

# 10+20			int.__add__(10, 20)
# 'a'+'b'			str.__add__('a', 'b')
# a+b				A.__add__(a, b)

#module###
# hain.py <--- Main Module

import rekha				# Importing hain Module

print("cal Module's variable:", rekha.a)	# Accessing Cal Module's Variable

rekha.name()								# Accessing Cal Module's Function

a = rekha.add(10,20)						# Accessing Cal Module's Function
print(a)

b = rekha.sub(20, 10)						# Accessing Cal Module's Function
print(b)
print()
# hain.py <--- Main Module

import rekha							# Importing Cal Module

print("cal Module's variable:", rekha.a)	# Accessing Cal Module's Variable

rekha.name()								# Accessing Cal Module's Function

add = rekha.add		# Accessing and Assigning Module's Function to Variable
a = add(10, 20)							# Accessing Cal Module's Function
print(a)

b = rekha.sub(20, 10)						# Accessing Cal Module's Function
print(b)
#hain.py <--- Main Module

import rekha as r							# Importing Cal Module

print("cal Module's variable:", r.a)	# Accessing Cal Module's Variable

r.name()								# Accessing Cal Module's Function

a = r.add(10,20)						# Accessing Cal Module's Function
print(a)

b = r.sub(20, 10)						# Accessing Cal Module's Function
print(b)
# hain.py <--- Main Module

from rekha import a, name, add, sub			# Importing Cal Module

print("cal Module's variable:", a)	# Accessing Cal Module's Variable

name()								# Accessing Cal Module's Function

a = add(10,20)						# Accessing Cal Module's Function
print(a)

b = sub(20, 10)						# Accessing Cal Module's Function
print(b)
# geekyshows.py <--- Main Module

from rekha import a, name, add as s, sub			# Importing Cal Module

print("cal Module's variable:", a)	# Accessing Cal Module's Variable

name()								# Accessing Cal Module's Function

add = s(10,20)						# Accessing Cal Module's Function
print(add)

b = sub(20, 10)						# Accessing Cal Module's Function
print(b)
# geekyshows.py <--- Main Module

from rekha import *					# Importing Cal Module

print("cal Module's variable:", a)	# Accessing Cal Module's Variable

name()								# Accessing Cal Module's Function

a = add(10,20)						# Accessing Cal Module's Function
print(a)

b = sub(20, 10)						# Accessing Cal Module's Function
print(b)
#ABSTRACT METHOD
#EXAMPLE 1
from abc import ABC, abstractmethod


class Father(ABC):

    @abstractmethod
    def disp(self):  # Abstract Method
        pass

    def show(self):  # Concrete Method
        print('Concrete Method')


# my = Father()						# Not possible to create object of a abstract class

class Child(Father):
    def disp(self):
        print("Defining Abstract Method")


c = Child()
c.disp()
c.show()
#EXAMPLE 2
from abc import ABC, abstractmethod


class DefenceForce(ABC):
    def __init__(self):
        self.id = 101

    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun = AK47")


class Army(DefenceForce):
    def area(self):
        print("Army Area = Land", self.id)


class AirForce(DefenceForce):
    def area(self):
        print("AirForce Area = Sky", self.id)


class Navy(DefenceForce):
    def area(self):
        print("Navy Area = Sea", self.id)


a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()
#INTERFACE
#EXAMPLE 1
from abc import ABC, abstractmethod


class Father(ABC):

    @abstractmethod
    def disp(self):  # Abstract Method
        pass


# my = Father()						# Not possible to create object of a abstract class

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")


c = Child()
c.disp()
#Interface
#EXAMPLE 2
from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass

    @abstractmethod
    def disp2(self):
        pass


class Child(Father):
    def disp1(self):
        print("Child Class")
        print("Disp 1 Abstract Method")


class Granchild(Child):
    def disp2(self):
        print("GrandChild Class")
        print("Disp 2 Abstract Method")


gc = Granchild()
gc.disp1()
gc.disp2()
#TIME MODULE
from time import time, ctime, localtime
epoch = time()
print()

print("epoch seconds:", epoch)
print()

et = ctime(epoch)
print("Epoch Date and Time:", et)
print()

ct = ctime()
print("Current Date and Time:", ctime())
print()

stobj = localtime()
print("struct_time Object:", stobj)
print()

print("Year:", stobj.tm_year)
print("Month:", stobj.tm_mon)
print("Date:", stobj.tm_mday)
print("Hour:", stobj.tm_hour)
print("Minute:", stobj.tm_min)
print("Second:", stobj.tm_sec)
print()
print(stobj.tm_mday, end="/")
print(stobj.tm_mon, end="/")
print(stobj.tm_year)
print(stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print(stobj.tm_sec)
print()

# Creating Object of datetime Class
from datetime import datetime
dt1 = datetime(year=2019, month=6, day=30)
dt2 = datetime(year=2018, month=5, day=29, hour=15, minute=34)
dt3 = datetime(2017, 4, 28)
dt4 = datetime(2016, 3, 27, 14, 30)
print(dt1)
print(dt2)
print(dt3)
print(dt4)
print(dt1.year)
print(dt2.month)
print(dt3.day)
print(dt4.hour)

#DATETIME module

from datetime import datetime
ct = datetime.now()					# Calling Method using class name
print("Current Date and Time:", ct)
print("Date:", ct.day)
print("Month:", ct.month)
print("Year:", ct.year)
print("Hour:", ct.hour)
print("Minute:", ct.minute)
print("Second:", ct.second)
print("Microsecond:", ct.microsecond)
print()

ct1 = datetime.today()				# Calling Method using class name
print("Current Date and Time:", ct1)
print("Date:", ct1.day)
print("Month:", ct1.month)
print("Year:", ct1.year)
print("Hour:", ct1.hour)
print("Minute:", ct1.minute)
print("Second:", ct1.second)
print("Microsecond:", ct1.microsecond)
print()

# Creating Object of date Class
from datetime import date
d1 = date(year=2019, month=6, day=30)
d2 = date(2017, 4, 28)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)
print()
print(d2)
print(d2.year)
print(d2.month)
print(d2.day)
#dateclass module
from datetime import date
cd1 = date.today()				# Calling Method using class name
print("Current Date:", cd1)
print("Date:", cd1.day)
print("Month:", cd1.month)
print("Year:", cd1.year)
print()

# Creating Object of time Class
from datetime import time
t1 = time(hour=15, minute=34, second=12)
t2 = time(16, 40, 15)
print(t1)
print(t1.hour)
print(t1.minute)
print(t1.second)
print(t1.microsecond)
print()
print(t2)
print(t2.hour)
print(t2.minute)
print(t2.second)

# Creating Object of timedelta Class
from datetime import timedelta, date
td = timedelta(days=10)
d = date.today()
print(d+td)

# Comparing Two Dates
from datetime import date
d1 = date(2019, 6, 30)
d2 = date(2010, 6, 30)
print(d1==d2)
print(d1>d2)
print(d1<d2)
print(d1!=d2)

# Formatting Date and Time
from datetime import datetime
dt = datetime.today()
print(dt)
newd1 = dt.strftime("%B %d, %Y")
print(newd1)
newd2 = dt.strftime("%d/%b/%Y")
print(newd2)
newd3 = dt.strftime("%d-%m-%Y")
print(newd3)

newt1 = dt.strftime("%H:%M:%S")
print(newt1)
newt2 = dt.strftime("%I:%M:%S")
print(newt2)

# sleep () Method is used to stop execution of a program temporarily for a given amount of time. When this function is called, PVM stops program execution for given amount of time.
# It belongs to time module

import time
for i in range(20):
	print(i)
	if(i == 10):
		time.sleep(5)
#calculate age
from datetime import date

dob = date(1993, 10, 15)
t = date.today()
age = t.year - dob.year - ((t.month, t.day) < (dob.month, dob.day))
print(age)
#THREAD
#Main thred
'''import threading
t = threading.current_thread().getName()
print(t)'''

# Importing Thread Class from threading Module
from threading import Thread

def disp():
	print("Thread Running")

# Creating Thread Class Object
t = Thread(target=disp)

# Starting Thread
t.start()

# Importing Thread Class from threading Module
from threading import Thread

def disp(a, b):
	print("Thread Running:", a, b)

# Creating Thread Class Object
t = Thread(target=disp, args=(10, 20))

# Starting Thread
t.start()

# Importing Thread Class from threading Module
from threading import Thread

def disp(a, b):
	print("Thread Running:", a, b)

for i in range(5):
	# Creating Thread Class Object
	t = Thread(target=disp, args=(10, 20))

	# Starting Thread
	t.start()

# Importing Thread Class from threading Module
from threading import Thread

def disp():
	for i in range(5):
		print("Child Thread")

# Creating Thread Class Object
t = Thread(target=disp)

# Starting Thread
t.start()

for i in range(5):
	print("Main Thread")

'''# Importing Thread Class from threading Module
from threading import Thread, current_thread


def disp():
    print("Child Thread", current_thread())

    print("Default Child Thread Name:", current_thread().getName())

    current_thread().setName('Doc Thread')
    print("New Child Thread Name:", current_thread().getName())

    current_thread().name = 'Flying Thread'

    print(current_thread().name)


# Creating Thread Class Object
t = Thread(target=disp)

# Starting Thread
t.start()

print("Main Thread", current_thread())

print("Default Main Thread Name:", current_thread().getName())

current_thread().setName('GeekyShows Thread')
print("New Main Thread Name:", current_thread().getName())

current_thread().name = 'Geek Thread'

print(current_thread().name)'''

'''# Importing Thread Class from threading Module
from threading import Thread

def disp():
	pass

# Creating Thread Class Object
t = Thread(target=disp)
print("Default Child Thread Name:",t.getName())
t.setName('Doc Thread')
print("New Child Thread Name:",t.getName())
t.name = 'Flying Thread'
print(t.name)'''

# Importing Thread Class from threading Module
from threading import Thread

def disp():
	pass

# Creating Thread Class Object
t = Thread(target=disp, name='Raj Thread')
print(t.name)

# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	pass

t = Mythread()
print(t.name)
# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def run(self):
		print("Run Method")

t = Mythread()
t.start()
# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def run(self):
		for i in range(5):
			print("Child Thread")

t = Mythread()
t.start()
t.join()
for i in range(5):
	print("Main Thread")

# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def __init__(self):
		Thread.__init__(self)		# Calling Thread Class(Parent) Constructor
		print("Child Thread Constructor")
	def run(self):
		pass

t = Mythread()
t.start()
print("Main Thread")

# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def __init__(self, a):
		Thread.__init__(self)		# Calling Thread Class(Parent) Constructor
		print("Thread Constructor", a)
	def run(self):
		pass

t = Mythread(10)
t.start()
print("Main Thread")

# Creating a thread Without creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread:
	def disp(self, a, b): print(a,b)

myt = Mythread()

t = Thread(target=myt.disp, args=(10, 20))
t.start()

# Single Tasking using a Thread
from threading import Thread
from time import *


class MyExam:
    def solve_question(self):
        self.task1()
        self.task2()
        self.task3()

    def task1(self):
        print("Question 1 Solved")

    def task2(self):
        print("Question 2 Solved")

    def task3(self):
        print("Question 3 Solved")


mye = MyExam()
t = Thread(target=mye.solve_question)
t.start()

# Multitasking using Multiple Thread
# Two task using Two Threads
from threading import Thread


class Hotel:
    def __init__(self, t):
        self.t = t

    def food(self):
        for i in range(1, 6):
            print(self.t, i)


h1 = Hotel('Take Order From Table: ')
h2 = Hotel('Serve Order to Table: ')
t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()

# Multitasking using Multiple Thread
# Two Threads acting on same method
# Race thread
from threading import Thread, current_thread


class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat

    def reserve(self, need_seat):
        print('Available Seats:', self.available_seat)
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{self.available_seat} seat is alloted for {name}')
            self.available_seat -= need_seat

        else:
            print('Sorry! All seats has alloted')


f = Flight(1)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
t1.start()
t2.start()

# Multitasking using Multiple Thread
# Two Threads acting on same method
# Lock thread
from threading import *


class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = Lock()

    def reserve(self, need_seat):
        self.l.acquire(blocking=True)
        print('Available Seats:', self.available_seat)
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
        else:
            print('Sorry! All seats has alloted')
        self.l.release()


f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
t3 = Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")

# Multitasking using Multiple Thread
# Two Threads acting on same method
# Rlock thread
from threading import *


class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = RLock()

    # print(self.l)

    def reserve(self, need_seat):
        self.l.acquire()
        self.l.acquire()
        # print(self.l)
        print('Available Seats:', self.available_seat)
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
        else:
            print('Sorry! All seats has alloted')
        self.l.release()
        self.l.release()


f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
t3 = Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")

# Multitasking using Multiple Thread
# Two Threads acting on same method
# Semaphore
from threading import *


class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = BoundedSemaphore(2)
        print(self.l)

    def reserve(self, need_seat):
        self.l.acquire()
        print(self.l._value)
        print('Available Seats:', self.available_seat)
        if (self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat
        else:
            print('Sorry! All seats has alloted')
        self.l.release()


f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')
t3 = Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("Main Thread")

# DaemonThread EX 1
'''from threading import Thread


def disp():
    print('Daemon Thread')


t1 = Thread(target=disp)
print('Before:', t1.isDaemon())
t1.setDaemon(True)
print('After:', t1.isDaemon())
t1.start()'''
#Example 2
from threading import Thread


def disp():
    print('Daemon Thread')


t1 = Thread(target=disp)
print('Before:', t1.daemon)
t1.daemon = True
print('After:', t1.daemon)
t1.start()
'''# Example 3
from  threading import current_thread
print(current_thread().getName())
mt = current_thread()
print(mt.daemon)'''

'''# NonDaemon parentchlid
from threading import Thread, current_thread
def disp():
	print('Disp Function')

mt = current_thread()	
print(mt.getName())
print(mt.isDaemon())
t1 = Thread(target=disp)	# Child of Main Thread becoz created by Main Thread
print(t1.isDaemon())
t1.start()'''

'''# Daemon Parentchild
from threading import Thread, current_thread

def disp():
	print('Disp Function')
	t2 = Thread(target=show)	# Child of t1 Thread becoz created by t1 Thread
	print('T2:', t2.isDaemon())
	t2.start()

def show():
	print('Show Function')

mt = current_thread()	
print(mt.getName())
print('MT:', mt.isDaemon())
t1 = Thread(target=disp)	# Child of Main Thread becoz created by Main Thread
print('T1 Before:', t1.isDaemon())
t1.setDaemon(True)
print('T1 After:', t1.isDaemon())
t1.start()
t1.join()'''

'''# WithoutDaemon
from threading import Thread, current_thread
from time import sleep


def teacher():
    for i in range(1, 11):
        print('Teaching Session', i)
        sleep(1)


t1 = Thread(target=teacher)  # Non-Daemon Thread
t1.start()
sleep(6)
print('Exam Finished', current_thread().name)  # Non-Daemon Thread'''

'''# WithDaemon
from threading import Thread, current_thread
from time import sleep


def teacher():
    for i in range(1, 11):
        print('Teaching Session', i)
        sleep(1)


t1 = Thread(target=teacher)
t1.setDaemon(True)  # t1 is Daemon
t1.start()
sleep(6)
print('Exam Finished', current_thread().name)  # Non-Daemon Thread (Main)'''

'''# WithDaemonJoin
from threading import Thread, current_thread
from time import sleep


def teacher():
    for i in range(1, 11):
        print('Teaching Session', i)
        sleep(1)


t1 = Thread(target=teacher)
t1.setDaemon(True)  # t1 is Daemon
t1.start()
sleep(6)
t1.join()
print('Exam Finished', current_thread().name)  # Non-Daemon Thread (Main)'''

# TextMode BinaryMode

f = open('student.txt', mode='w')
f.write('Hello\n')
f.write('GeekyShows\n')
f.write('How are you')
f.close()
print('Writing Success')

f = open('student.txt', mode='r')
data = f.read()
print(data)
f.close()

f = open('student.txt', mode='rb')
data = f.read()
print(data)
f.close()
# file object variable
f = open('student.txt', mode='r', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
# Opening for Reading
f = open('student.txt', mode='r', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
# Opening for Writing
f = open('student.txt', mode='w', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
# Opening for Appending
f = open('student.txt', mode='a', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
'''# Opening for Exclusive Creation
f = open('student.txt', mode='x', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)'''
# Open for reading and then writing
f = open('student.txt', mode='r+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
# Open for writing and then reading
f = open('student.txt', mode='w+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
# Open for appending and then reading
f = open('student.txt', mode='a+', encoding = 'utf-8')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)
# Binary Read mode
# Open for reading
f = open('rekha.jpg.jpg', mode='rb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)

# Open for Writing
f = open('pythona.jpg', mode='wb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)

# Open for Appending
f = open('pythona.jpg', mode='ab')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)

'''# Open for Exlusive Creation
f = open('pythona.jpg', mode='xb')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)'''

# Open for reading and then writing
f = open('pythona.jpg', mode='rb+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)

# Open for writing and then reading
f = open('pythona.jpg', mode='wb+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)

# Open for Appending and then reading
f = open('pythona.jpg', mode='ab+')
print('File Name:', f.name)
print('File Mode:', f.mode)
print('File Readable:', f.readable())
print('File Writable:', f.writable())
print('File Closed:', f.closed)
f.close()
print('File Closed:', f.closed)

# Check File exists or not
# Exmaple 1
import os
print(os.path.isfile('student.txt'))

# Example 2
import os
if os.path.isfile('student.txt'):
	f = open('student.txt')
	print('File Opened')
	f.close()
else:
	print('File Not Found')

# Writing Data with w mode Example 1
f = open('student.txt', mode='w')
f.write('Hello')
f.write('GeekyShows')
f.write('How are you')
f.close()
print('Success')

# Writing Data with w mode Example 2
f = open('student.txt', mode='w')
f.write('Hello ')
f.write('GeekyShows ')
f.write('How are you')
f.close()
print('Success')

'''# Writing Data with x mode
f = open('student4.txt', mode='x')
f.write('Hello\n')
f.write('GeekyShows\n')
f.write('How are you')
f.close()
print('Success')'''

# Writing Data with w mode Example 3
f = open('student.txt', mode='w')
f.write('Hello\n')
f.write('GeekyShows\n')
f.write('How are you')
f.close()
print('Success')

# Writing Data with a mode
f = open('student1.txt', mode='a')
f.write('good ')
f.close()
print('Success')
# Writelines
# Writing Data with w mode Ex 1
f = open('student0.txt', mode='w')
lst = ['Rahul', 'Sonam', 'Sumit', 'Rani', 'Raj']
f.writelines(lst)
f.close()
print('Success')

# Writing Data with w mode
f = open('student0.txt', mode='w')
lst = ['Rahul\n', 'Sonam\n', 'Sumit\n', 'Rani\n', 'Raj\n']
f.writelines(lst)
f.close()
print('Success')

# Writing Data with a mode
f = open('student0.txt', mode='a')
lst = ['Rahul\n', 'Sonam\n', 'Sumit\n', 'Rani\n', 'Raj\n']
f.writelines(lst)
f.close()
print('Success')
# Reading Data with r mode
f = open('student0.txt', mode='r')
data = f.read()
print(data)
f.close()
print('Completed!!!!')

# Reading Data with r mode
f = open('student.txt', mode='r')
data1 = f.read(2)
data2 = f.read(2)
print(data1)
print(data2)
f.close()

# Reading Data with r mode
f = open('student0.txt', mode='r')
data1 = f.readline()
data2 = f.readline()
print(data1)
print(data2)
f.close()
# Reading Data with r mode
f = open('student0.txt', mode='r')
data = f.readlines()
print(data)
for i in data:
	print(i, end='')
f.close()
# Tell method
f = open('student4.txt', mode='r')
print(f.tell())
data1 = f.read(5)
print(data1)
print(f.tell())
data2 = f.read(3)
print(data2)
print(f.tell())

# Seek method
f = open('student4.txt', mode='r')
print(f.tell())
f.seek(3)
print(f.tell())
data1 = f.read()
print(data1)
f.seek(2)
print(f.tell())
data2 = f.read()
print(data2)
# Read then Write
f = open('student11.txt', mode='r+')
print(f.tell())
data = f.read()
print(f.tell())
f.write('Youtube')
print(f.tell())
print(data)
print(f.tell())
# writing and then reading It will overwrite existing data
f = open('student11.txt', mode='w+')
print(f.tell())
f.write('Youtube')
print(f.tell())
data = f.read()
print(f.tell())
print(data)

# writing and then reading It will overwrite existing data
f = open('student11.txt', mode='w+')
print(f.tell())
f.write('Youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data = f.read()
print(f.tell())
print(data)

# appending and then reading It wont overwrite existing data
f = open('student11.txt', mode='a+')
print(f.tell())
f.write('Youtube')
print(f.tell())
data = f.read()
print(f.tell())
print(data)

# Appending and then reading It wont overwrite existing data
f = open('student11.txt', mode='a+')
print(f.tell())
f.write('Youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data = f.read()
print(f.tell())
print(data)

# Copy Contents of a file to another file
f1 = open('student11.txt', mode='r')
f2 = open('student12.txt', mode='w')
data = f1.read()
f2.write(data)
print('Success')

# With statemenet

with open('student1.txt') as f:
	data = f.read()
	print(data)
	print('File Closed:',f.closed)
print('File Closed:',f.closed)
# Directory
# getcwd
import os
print(os.getcwd())
'''# mkdir
import os
os.mkdir('mydir')
os.mkdir('mydir/mkchilddir')

# makedirs
import os
os.makedirs('parentdir/childdir/grandchilddir')
#change chdir
import os
print(os.getcwd())
os.chdir('mydir')
print(os.getcwd())
# rename
import os
os.rename('mydir', 'yourdir')
# remove
import os
os.rmdir('newdir')					# It will remove newdir
os.rmdir('mydir/mychilddir')'''		# It will remove only mychilddir
# all remove
import os
# It will remove all mentioned
os.removedirs('parentdir/childdir/grandchilddir')

# walk
import os
w = os.walk('.')
for i in w:
	print(i)
print()

w = os.walk('yourdir')
for i in w:
	print(i)
print()

w = os.walk('yourdir', topdown=False)
for i in w:
	print(i)


