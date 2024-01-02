'''print("hello world")
print("hello moon")
a = 10
print(id(a))
full_name=("saurabh kumar")
print(full_name)
#list
data =[10,20,-50,21.3,'Rekha']
print(data)
print(data[3])
#tuple
data =(10,30,50,60,'saurabh')
print(data)
print(data[2])
#range
rg=range(5)
print(rg)
rg=range(10,20,2)
print(rg)
#set type
data ={10,20,30,"saurabh","golu",40}
data ={10,20,50,"saurabh","golu",40}
# not modify  data[2]=70
print(data)
#dictonary,mapping
mp ={101: 'rahul',102: 'sonu',103: 'monu'}
print(mp)
print(mp[101])
#declecaring and initializing variable
a =10
print(a)
b =20.30
print(b)
c ='saurabh'
print(c)

a=b=c=d=10
print(a)
print(b)
print(c)
print(d)
a=b=c=d= True
print(a)
print(b)
print(c)
print(d)
a=10
b=20.5
c="saurabh"
d='saurabh'
print(a)
print(b)
print(c)
print(d)
a,b,c,d =20, 30.55, "saurabh" ,'golu'
print(a)
print(b)
print(c)
print(d)
#operator(arithmethic)
print(4+2)
a=4
b=5
total=a+b
print(total)
print(9-8)
a=9
b=6
total =a-b
print(total)
a=3
b=2
value =a*b
print(value)
print(4/2)
a=6
b=2
value=6/2
print(value)
a=9
b=3
value=9%3
print(value)
a=5
b=2
value=5**2
print(value)
a=7
b=3
value=7//3
print(value)
a=-5
b=2
value=-5//2
print(value)
#operator(relational)
a=5
b=2
result=5<2
print(result)
a=6
b=9
result=a<b
print(result)
a=5
b=6
total=(a<=b)
print(total)
a=9
b=8
total=(a>=b)
print(total)
a=8
b=6
total=(a==b)
print(total)
a=9
b=8
total=(a!=b)
print(total)
a=8
b=9
total=(8<9)and(8>9)
print(total)
a=9
b=6
value=not(9>6)
print(value)
#operator(assignment)
a=10
b=20
c=(a+b)
print(c)
#membership in operator
st1="welcome to saurabh"
print("to" in st1)
#membership notin operator
st1="welcome to golu"
print("ot" not in st1)
#identify is operator
a=10
b=10
print(a is b)
#identify is not operator
a=20
b=30
print(a is not b)
#operator precedence and associativity
value =(1+1)*2**4//3+4-1
print(value)
#implicit conversion
a=5
b=2
value=a/b
print(value)
print(type(value))
a=10
b=5.5
total=a-b
print(total)
print(type(value))
a="hello"
b="geeky shows"
c=a+b
print(c)
print(type(c))
a=20
b='geekyshows'
#c=a+b
print(c)
#explicit conversion
a=5
b=2
value=(a/b)
print(type(value))
int_value =int(value)
print(int_value)
print(type(int_value))
#def swap(a,b):
a= 5
b=20
a=a+b
b=a-b
a=a-b
print(a )
print(b)
#output statements
#print(objects,sep='character',end='character',file=sys.stdout,flush=false)
print("saurabh kumar")
print('welcome to  saurabh kumar')
print("like","share","subscribe")
print(19)
data=[20,30,40,50]
print(data)
print("like","share","subscrribe" ,sep='***')
print('welcome', end=' ')
print("to", end=' ')
print("saurabh", end='\n ')
print('welcome', end=' \t')
print("to", end=' \t')
print("saurabh", end='\t ')
#output statement
a= 10
print(a)
a=20
b=30
print (a,b ,sep='$')
a= 20
print("value:",a)
name="saurabh"
age=20
print("my name is:",name,"and my age is:" ,age)
#input statement
name= input("what is your name")
print(name)
name=input("what is your name")
print("your name is",name)
#input statement integer you have to use type conversion
age=int(input("what is your age"))
print(age)
mobile=int(input("enter your mobile number"))
print(mobile)
print()
print("welcome to \nhouse")
print("welcome to \"home\" ")
#if statement
if(4>3):
    print("greater")
    print("4 is greater than 3 ")
print("welcome")
#user input if statement
a=int(input("enter your greater than 5: "))
if(a>5):
    print("you have entered :",a)
#nested if statement
if(5>2):
    print("greater")
    print("5 is greater than 2")
    if(10>9):
        print("10 is greater than 9")
print("welcome")
#if statement with logical operaror
if(9>7):
    print("9 is greater than 7")
    print("welcome to our country")
#nested if statement
if(9>8):
    print("9 is greater than 8")
    if(6>4):
        print("true")
print("true")
if 5>6:
	print("Greater")
	print("5 is greater than 2")
print("Rest of The Code")
#if statement with logical statement
if((2>1)and(1<2)):
    print("If statement with Logical Operator")
    print("Statement 2")
#user input
a = int(input("Enter Number Greater than 2: "))
if(a<2):
    print(a)
#indentation
if 7 > 4:
    print("Greater")
    print("7 is greater than 4")
    if (6 > 3):
        print("6 is Greater than 3")
print("welcome is home")
#if else statement
if(8<9):
    print("9 is greater than 8")
else:
    print("none")
print("last line of code1")
#nested if else statement
a=6
b=1
c=7
d=3
if(a<b):
    print("a is greater than b")
    if(c<d):
        print("c is greater than d")
    else:
        print("d is greater than c")
else:
    print("b is greater than a")
print("last  of code")
#user if else statement
a = int(input("Enter Number Greater than 2: "))
if(a>=2):
    print("Correct!! You have Entered:", a)
else:
    print("wrong!! you have entered:",a)
#if elif statement
if(9<10):
    print("10 is greater than 9")
elif(9==10):
    print("9 and 10 is equal")
elif(9>10):
    print("9 is less than 10")
print("last line of code")
# If elif with User Input
a = int(input("Enter Value of 9: "))
b = int(input("Enter Value of 10: "))
if 9 < 10:
	print("10 is greater than 9")
elif 9 == 10:
	print("9 and 10 are equal")
elif 9 < 10:
	print("9 is less than 10")
#while loop
a=1
while(a<=10):
    print(a)
    a+=1
print("line of code")
b=3
while(b<=30):
    print(b)
    b+=3
c=4
while(c<=40):
    print(c)
    c+=4
#while else loop
a=6
while(a<=60):
    print(a)
    a+=6
else:
    print("while condition false so else part executed")
print("line of code")
#infinite while loop
#while(True):
 #   print("geeky shows")
#infinite while loop
i=0
while (True):
    i+=1
    print(i)
    if(i == 5):
        break
    print(" line of code")
#nested while loop
a=10
while(a<=30):
    print("outer loop",a)
    a+=10
b=5
while(b<=25):
    print("inner loop",b)
    b+=5
#range
a=range(5)
print(a)
b=range(6)
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
b = range(1, 5)
print(b[0])
print(b[1])
print(b[2])
print(b[3])
c=range(2,5,10)
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
n = range(-1, -10, -2)
print(n[0])
print(n[1])
print(n[2])
print(n[3])
print(n[4])
#for loop
st=("saurabhkumar")
for bh in st:
    print(bh)
print("code of line")
#for loop with range
ct=("saurabhkumar")
n=len(ct)
for ch in range(n):
    print(ch,"=",ct[ch])
#for loop with else
for bh in st:
    print(bh)
else:
    print("Else Part Executed")
print("Rest of the Code")
#nested for loop
for i in range(3):
		print("Outer Loop", i)
		for j in range(5):
			print("Inner Loop", j)
print("of the Code")
#break statement
for i in range(6):
    if(i ==30):
        break
    print(i)
print("line of code")
for i in range(30):
        if (i == 6):
            continue
        print(i)
        print("line of code")
#ARRAY
stu_roll=101,102,103,104,105
print(stu_roll)
stu_roll=101,102,103,104,105
from array import*
stu_roll= array('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
import array
stu_roll= array.array('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
from array import *
stu_roll= array('f',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
for element in stu_roll:
	print(element)
# Create Array and iterate using for Loop with index
from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
for i in range (n):
    print(i,"=",stu_roll[i])
# Create Array and iterate using while Loop with index
from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
#Append

from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
stu_roll.append(106)
stu_roll.append(107)
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
#insert
from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
#pop
from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
    stu_roll.pop()
    n=len(stu_roll)
    i=0
    while(i<n):
        print(stu_roll[i])
        i+=1
#pop(position number)
from array import*
stu_roll=array('i',[101,102,103,104,105])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
    r=stu_roll.pop(3)
    n=len(stu_roll)
    i=0
    while(i<n):
        print(stu_roll[i])
        i+=1
#remove element
from array import*
stu_roll=array('i',[101,102,103,104,105,101])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
    stu_roll.remove(101)
    n=len(stu_roll)
    i=0
    while(i<n):
        print(stu_roll[i])
        i+=1
#index (element)
from array import*
stu_roll=array('i',[101,102,103,104,105])
print(stu_roll.index(103))
#reverse array
from array import*
stu_roll=array('i',[101,102,103,104,105,101])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
    stu_roll.reverse()
    n=len(stu_roll)
    i=0
    while(i<n):
        print(stu_roll[i])
        i+=1
from array import*
stu_roll=array('i',[101,102,103,104,105,101])
arr=array('i',[107,108,109,110])
n=len(stu_roll)
i=0
while(i<n):
    print(stu_roll[i])
    i+=1
    stu_roll.extend(arr)
    n=len(stu_roll)
    i=0
    while(i<n):
        print(stu_roll[i])
        i+=1
#slicing on array
from array import *
stu_roll =array('i',[101,102,103,104,107])
print("original array")
n=len(stu_roll)
for i in range(n):
    print(i,"_",stu_roll[i])
a=stu_roll[2:5]
for i in a:
    print(i)
from array import *
stu_roll =array('i',[101,102,103,104,107])
print("original array")
n=len(stu_roll)
for i in range(n):
    print(i,"_",stu_roll[i])
a=stu_roll[0:]
for i in a:
    print(i)
from array import *
stu_roll =array('i',[101,102,103,104,107])
print("original array")
n=len(stu_roll)
for i in range(n):
    print(i,"_",stu_roll[i])
a=stu_roll[3:]
for i in a:
    print(i)
    from array import *

    stu_roll = array('i', [101, 102, 103, 104, 107])
    print("original array")
    n = len(stu_roll)
    for i in range(n):
        print(i, "_", stu_roll[i])
    a = stu_roll[-4:]
    for i in a:
        print(i)
#one dimensional numpy array
import numpy
stu_roll =numpy.array([101,102,103,104,105])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
#1D array with float number using array function numpy
import numpy
stu_roll= numpy.array([101,102,103,104,105],dtype=float)
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
#1D arrray with implicit float converrsion using array function numpy
import numpy
stu_roll=numpy.array([101,102,103,104,10.5])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
#1D array with  character using array function numpy
import numpy
stu_roll=numpy.array(['a','b','c','d','e'])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
#1D array with string using array function numpy
import numpy
stu_roll=numpy.array(['rahul','sonam','sonu','badal','ropcky','golu'])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
print(stu_roll[5])
#1D array using array function
from numpy import*
stu_roll=array([101,102,103,104,105])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
#1D array using array function numpy USING FOR LOOP
from numpy import *
stu_roll=array([101,102,103,104,105])
for element in stu_roll:
    print(element)
#1D array using array function numpy using for loop weith index
from numpy import *
stu_roll=array([101,102,103,104,105])
n=len(stu_roll)
for i in range(n):
    print('index',i,"=",stu_roll[i])
#1D array using array function numpy using while loop
from numpy import *
stu_roll =array([101,102,103,104,105])
n= len(stu_roll)
i=0
while i<n:
    print('index',i,'=',stu_roll[i])
i+=1
#modifying 1D array numpy
from numpy import*
stu_roll=array([101,102,103,104,105])
stu_roll[1]=200
n = len(stu_roll)
for i in range(n):
    print('index',i,"=",stu_roll[i])
 #1D array using linspace function numpy
from numpy import *
a = linspace(1,10,5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
#1d array using logspace function numpy
from numpy import *
a = logspace(1,3,5)
print("individual element")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
for el in a :
    print(el)
print()
n =len(a)
for i in  range (n):
    print('index',i,'=',a[i])
print()
n =len(a)
i = 0
while i<n:
    print('index',i,'=',a[i])
    i+=1
#arrange function
from numpy import *
a = arange(5)
print(a)
b= arange(1,10)
print(b)
from numpy import *
c= arange(1,6)
for el in c:
        print(el)
print()
#zeros function
from numpy import *
a = zeros(5)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
print("accessing for loop")
for el in a:
    print(el)
print()
print("accessing for loop with index")
n =len(a)
for i in range(n):
    print('index',i,'=',a[i])
print()
print("accessing while loop")
n=len(a)
i=0
while i<n:
    print('index',i,'=',a[i])
    i+=1
#ones function
from numpy import *
a= ones(5)
print(a)
print("accessing individual elements")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
print("accessing for loop with index")
n=len(a)
for i in range (n):
    print('index',i,'=',a[i])
print()
print("while loop")
n=len(a)
i=0
while i<n:
    print('index',i,'=',a[i])
    i+=1
#math operation add number
from numpy import *
a=array([101,102,103,104,105])
a= a+5
print(a)
for el in a :
    print(el)
from numpy import *
b=array([101,102,103,104,105])
c=array([1,2,3,4,5])
d=b+c
print(d)
for el in a:
    print(el)
print()
#numpy comparing array
a=array([101,102,103,104,105])
b=array([101,102,10,104,105])
#result = a==b
result =a<b
print(result)
#any and all function
a=array([101,102,103,104,105])
b=array([101,10,103,104,105])
result =a==b
print(any(result))
print(all(result))
#where function
from numpy import *
a = array([101, 12, 300, 4, 500])
b = array([100, 20, 30, 400, 50])
result = where(a>b, a, b)
print(result)
#nonzero function
a=array([100,200,13,0,400,500,0])
result =nonzero(a)
print(result)
from numpy import *
a=array([10,20,30,40,50])
b=a
print(a)
print(b)
print("",id(a))
print("",id(b))
from numpy import *
a=array([10,20,30,40,50])
b=a.view()
a[4]=80
print(a)
print(b)
print("a",id(a))
print("b",id(b))
from numpy import *
a=array([10,20,30,40,50])
b=copy(a)
a[4]=80
b[1]=30
print(a)
print(b)
print("a",id(a))
print("b",id(b))
#numpy input from user 1d array
from numpy import *
n= int(input("enter number of elements:"))
a= zeros(n,dtype=int)
for i in range(len(a)):
	x = int(input("Enter Element: "))
	a[i] = x
print(a)
from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype=int)
u = len(a)
i = 0
j = 0
while (i < u):
    x = int(input("Enter Element: "))
    a[i] = x
    i += 1
#numpy two D array function
import numpy
a =numpy.array([[10,20,30,40],[30,20,10,80]])
print(a)
from numpy import *
b =array([[90,100,102,103],[50,60,70,80]])
print(b)
print(b.dtype)
print(b[0][0])
print(b[0][1])
print(b[0][2])
print(b[0][3])
print(b[1][0])
print(b[1][1])
print(b[1][2])
print(b[1][3])'''
#accessing 2D array using for loop
from numpy import  *
a =array([[10,20,30,40],[30,20,10,80]])
for r in a:
    for c in r:
        print(c)
        print()
from numpy import *
a =array([[10,20,30,40],[30,20,10,80]])
n=len(a)
for i in range(n):
    for j in range(len(a[i])):
        print('index',i,j,"=",a[i][j])
        print()
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

a[1][2] = 100

n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()
from numpy import *

a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print('index', i, j, "=", a[i][j])
        j += 1
    i += 1
    print()
#zeros function
from  numpy import  *
a=zeros((3,2))
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
print()
#accessing 2d array using for loop
a=zeros((3,2))
for r in a:
    for c in r:
        print(c)
        print()
#with index
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()

print(" Aessing by While Loop ")
n = len(a)
i = 0
while i < n :
	j = 0
	while j < len(a[i]):
		print('index',i,j,"=",a[i][j])
		j+=1
	i+=1
	print()
#creating 2d array using ones function
from numpy import *
a=ones((3,2))
print(a[0],[0])
print(a[0],[1])
print(a[1],[0])
print(a[1],[1])
print(a[2],[0])
print(a[2],[1])
print()
#using for loop
for r in a:
    for c in r:
        print(c)
        print()
#using while  loop
n = len(a)
i = 0
while i < n :
	j = 0
	while j < len(a[i]):
		print('index',i,j,"=",a[i][j])
		j+=1
	i+=1
	print()
#reshape function 1d to 2d
from numpy import *
a = array([1,2,3,4,5,6])
b= reshape(a,(2,3))
print(a)
print(b)
print()
#reshape function 1d to 3d
b=array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
c=reshape(b,(2,3,2))
print(b)
print(c)
print()
#2d to 1 d
e = array([[1, 2, 3], [4, 5, 6]])
f = reshape(e, (6))
print(e)
print(f)
#flatten function
from numpy import *
e = array([[1, 2, 3], [4, 5, 6]])
f = e.flatten()
print(e)
print(f)
#attributes of numpy array
from numpy import *
a = array([101, 102, 103, 104, 105])
b = array([[10, 20, 30, 40], [50, 60, 70, 80]])
print()
print("1d array ndim:",a.ndim)
print("1d array ndim:",b.ndim)
print()
print("1D Array shape:",a.shape)
print("2D Array shape:",b.shape)
print()
print("1D Array size:",a.size)
print("2D Array size:",b.size)
print()
print("1D Array itemsize:",a.itemsize)
print("2D Array itemsize:",b.itemsize)
print()
print("1D Array dtype:",a.dtype)
print("2D Array dtype:",b.dtype)
print()
print("1D Array nbytes:",a.nbytes)
print("2D Array nbytes:",b.nbytes)
print()
#STRING V86 S35
str1='saurabh kumar'
str2='saurabhkumar'
str3="saurabh kumar"
str4='''hello guys
please subscribe
saurabhkumar'''
print(str1)
print(str2)
print(str3)
print(str4)




























































