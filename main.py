print("hello")
a=30
print(a)
#built-in data..
y=10
print(y)
type(y)
str="rekha"
print(str)
# arithmetic operators
print(4+5)
print(5-4)
print(5*4)
print(5%2)
print(5//2)
a=18     #variable
b=9
value = (a/b)
print(value)
print(5**2)
#reletional or comparison operator
a=7
b=5
value = (a>b)
print(value)
print(5<2)
print(5>=2)
print(5<=2)
print(5==2)
print(5!=2)
#logical & operators
a=5
b=2
c=3
d=200
print(a>b and a>c)
print(a>b and a<c)
print(a<b and a<c)
print(a>b and d)
print(a<b and d)
#logical || operators
a=7
b=3
c=4
d=400
print(a>b or a>c)
print(a>b or a<c)
print(a<b or a<c)
print(a>b or d)
print(a<b or d)
#logical ! operators
print(not(5>2))
print(not(5<2))
#assignment operator
m=15
m+=10
print(m)
#bitwise operators
a=10
b=15
print('a<<2 =',a<<2)
print('a>>2 =',a>>2)
print('a&b =',a&b)
print('~a =', ~a)
print('a|b =',a|b)
#membership  (in) operators
st1="welcome to rekha "
print( "to" in st1)    #sequence
#membership  ( not in) operators
st1="welcome to rekha "
print( "to" not in st1)
st2="welcome to rekha "
print( "are" not in st2)
#identity (is) operators
a=11
b=11
print(a is b)
a=2
b='2'
print(a is b)
#identity (is not) operators
a=15
b=15
print(a is not b)
a=4
b='4'
print(a is not b)
#operator precedence
a= (1+1)*2**4//3+4-1
print(a)
#implicit conversion
a=5
b=2
value =a/b
print(value)
print(type(value))
a="hello"
b="saurabh"
total =a+b
print(total)
print(type(total))
#explicit conversion
a=5
b=2
value=a/b
int_value=int(value)
print( type(int_value))
print(int_value)
#string to tuple()
n="saurabh"
vn=tuple(n)
print(vn)
print(type(vn))
#string to list[]
n="saurabh"
vn=list(n)
print(vn)
print(type(vn))
#tuple to list
n=("ram","sita","lakhan")
vn= list(n)
print(vn)
print(type(vn))
print(type(n))
#output statement
name="saurabh"
age=26
print("my name is",name,"\n my age is",age)
#getting input from user or input
'''name=input("my name is")
print(name)
mb=int(input("enter your mobile number:"))
print(mb)'''
#if (condition is true)statement
if 9>7:
  print("nine is greater than seven")
if 8>7:print("eight is greater than seven")
a =int(input("enter number greater than 2:"))
if(a>2):
    print("you have entered",a)
#nested if
if 5>3:
    print("greater")
    print("5 is greater than 3")
    if(6>2):
        print("6 grater than 3")
        print("rest of code")
'''a =int(input("enter number greater than 2:"))
if(a>2):
    print("you have entered",a)
    b = int(input("enter number greater than 4:"))
    if (b > 4):
        print("you have entered", b)
        print("rest of code")'''
#if statement logical operator
if 5>2 and 6>3:
    print("if statement with logical ")
    print("rest of code")
'''a = int(input("enter number greater than 3:"))
b = int(input("enter number greater than 4:"))
if(a>3 & b>4):
    print("you have entered",a,b)'''
#if else
if 5<2:
    print("greater")
else:
    print("smaller")
'''a = int(input("enter number greater than 4:"))
if a<=4:
    print("correct! you have entered:",a)
else:
    print("wrong! you haw entered:",a)'''
#nested if else
a=5
b=2
c=6
d=3
if a>b:
    print("greater")
    if c>d:
        print("c is greater than d")
    else:
        print("d greater than c")
else:
    print("b is greater than a")
#if elif statement
a=20
b=10
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
elif a<b:
    print("a is less than b")
'''a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
elif a < b:
    print("a is less than b")'''
# if elif  else statement
day = "friday"
if(day == "monday"):
    print("today is monday")
elif (day == "tuesday"):
    print("today is tuesday")
elif (day == "wednesday"):
   print("to day is wednesday")
else:
    print("today is holiday")
    # If elif else with User Input
    day = input("Enter Day: ")
    if day == "Monday":
        print("Today is Monday")
    elif day == "Tuesday":
        print("Today is Tuesday")
    elif day == "Wednesday":
        print("Today is Wednesday")
    else:
        print("Today is Holiday")
#while loop
a=2
while a<=20:
    print(a)
    a+=2
# while loop with else
a=1
while a<=5:
    print(a)
    a+=1
else:
    print(" while condition false")
print("rest of code")
#nested while loop
i=1
while i<=3:
    print("outer loop",i)
    i+=1
    j=1
    while j<=5:
        print("inner loop",j)
        j+=1
#range function (i,j-1)
a=range(1,10,2)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
#for loop
for x in "banana":
  print(x)
#for loop with range
a=range(1,5)
for i in a:
    print(i)
#for loop with else
st="rekha"
for ch in st:
    print(ch)
else:
    print("else part")
    print("rest of code")
#nested for loop
for i in range(2):
    print("outer loop",i)
    for j in range(3):
        print("inner loop",j)
#break statement
for i in range(10):
    print(i)
    if(i==5):
        break
# break statement/#particular line skip
        for i in range(9):
            if i == 3:
                continue
            print(i)
#pass statement
if 5>2:
    pass
else:
    print("else part")
#create array one dimentional array
import array as ar
stu_roll = ar.array ('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
#create array example 2
from array import *
stu_roll = array ('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
#create array example3
from array import *
stu_roll = array ('f',[10.1,1.2,12.3,16.4,15.6])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
#create array example3
from  array import *
stu_roll=array('i',[101,102,103,104,105])
for el in stu_roll:
    print(el)
# create array example4
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
# while loop array example
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
#append
from array import *
stu_roll = array('i', [102, 103, 104, 105, 106])
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
    print("array after append")
    stu_roll.append(2006)
    n = len(stu_roll)
    i = 0
    while i < n:
        print(stu_roll[i])
        i += 1
#getting user input array using for loop
'''from array import *
stu_roll=array('i',[])
n=int(input("enter number of element"))
for i in range(n):
    stu_roll.append(int(
    input("enter element")))
    for i in range(len(stu_roll)):
        print(stu_roll[i])'''
#getting user input array using while
'''from array import *
stu_roll=array('i',[])
n=int(input("enter number of element"))
i=0
j=0
while i<n:
    stu_roll.append(int(
    input("enter element")))
    i+=1
    while(j< len(stu_roll)):
        print(stu_roll[j])
        j+=1'''
#insert()
from array import *
stu_roll = array('i', [102, 103, 104, 105, 106])
n = len(stu_roll)
i = 0
while i < n:
   print(stu_roll[i])
   i+=1
   print("array after insert")
   stu_roll.insert(1,109)
   stu_roll.insert(3, 107)
   n=len(stu_roll)
   i=0
   while i<n:
       print(stu_roll[i])
       i+=1
#pop()
from array import *
stu_roll = array('i', [102, 103, 104, 105, 106])
n = len(stu_roll)
i = 0
while i < n:
   print(stu_roll[i])
   i+=1
   print("array after pop")
   r= stu_roll.pop(3 )
   n=len(stu_roll)
   i=0
   while i<n:
       print(stu_roll[i])
       i+=1
       print("r")
#remove()
# remove (element)
from array import *
stu_roll = array('i', [101, 102, 101, 104, 105])
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i +=1

print("Array After Remove")
stu_roll.remove(101)
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1
#index()
from array import *
stu_roll=array('i',[101,102,101,104,105])
print(stu_roll.index(104))
#reverse()
print("array after pop")
stu_roll.reverse()
n=len(stu_roll)
i=0
while i<n:
    print(stu_roll[i])
    i+=1
#extend()
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
arr = array('i', [107, 108, 109])
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1

print("Array After Extend")
stu_roll.extend(arr)
n = len(stu_roll)
i = 0
while(i<n):
	print(stu_roll[i])
	i+=1
#slicing on array
# numpy
# 1D Array using array Function Numpy Example 1
from array import *

stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107])
print("Original Array")
n = len(stu_roll)
for i in range(n):
    print(i, "=", stu_roll[i])

print("From 1st Position to 4th Position")
a = stu_roll[1:5]
for i in a:
    print(i)

print("From 0th Position to last Position")
b = stu_roll[0:]
for i in b:
    print(i)

print("From 0th Position to 4th Position")
c = stu_roll[:5]
for i in c:
    print(i)

print("Last 4 Elements")
d = stu_roll[-4:]
for i in d:
    print(i)

print("From 0th Position to 6th Position stride 2")
e = stu_roll[0:7:2]
for i in e:
    print(i)

print("Last 5 Elements with [-5-(-3)]= 2 elements towards right")
f = stu_roll[-5:-3]
for i in f:
    print(i)

# 1D Array with Float Number using array Function Numpy Example 2
import numpy
stu_roll = numpy.array([101, 102, 103, 104, 105], dtype=float)
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# 1D Array with Implicit Float Conversion using array Function Numpy Example 3
import numpy
stu_roll = numpy.array([101, 102, 103, 104, 10.5])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# 1D Array with Character using array Function Numpy Exmaple 4
import numpy
stu_roll = numpy.array(['a', 'b', 'c', 'd', 'e'])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# 1D Array with string using array Function Numpy Example 5
import numpy
stu_roll = numpy.array(['Rahul', 'Sonam', 'Raj', 'Rani', 'Sumit'])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# 1D Array using array Function Numpy Example 6
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
# 1D Array using array Function Numpy for loop
#without index
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])

for element in stu_roll:
	print(element)
# 1D Array using array Function Numpy for loop
#with index
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
n=len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])
# 1D Array using array Function Numpy while loop
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
n=len(stu_roll)
i=0
while i< n:
    print(i,"=",stu_roll[i])
    i+=1
# 1D Array using linspace Function Numpy
from numpy import *
stu_roll=linspace(1,8,5)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
print("**** Accessing by For Loop ****")
for el in a:
	print(el)
print()

print("**** Accessing by For Loop with Index ****")
n = len(a)
for i in range(n):
	print('index',i,'=',a[i])
print()

print("**** Accessing by While Loop ****")
n = len(a)
i = 0
while i < n:
	print('index',i,'=',a[i])
	i+=1
# 1D Array using logspace Function Numpy

from numpy import *
a = logspace(1, 3, 5)

print("**** Accessing Individual Elements ****")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()

print("**** Accessing by For Loop ****")
for el in a:
	print(el)
print()

print("**** Accessing by For Loop with Index ****")
n = len(a)
for i in range(n):
	print('index',i,'=',a[i])
print()

print("**** Accessing by While Loop ****")
n = len(a)
i = 0
while i < n:
	print('index',i,'=',a[i])
	i+=1
# 1D Array using arange Function Numpy
from numpy import *
a = arange(5)
#a = arange(5.0)
#a = arange(1, 6)
#a = arange(1, 10, 2)

print("**** Accessing Individual Elements ****")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()

print("**** Accessing by For Loop ****")
for el in a:
	print(el)
print()

print("**** Accessing by For Loop with Index ****")
n = len(a)
for i in range(n):
	print('index',i,'=',a[i])
print()

print("**** Accessing by While Loop ****")
n = len(a)
i = 0
while i < n:
	print('index',i,'=',a[i])
	i+=1
# 1D Array using zeros Function Numpy
from numpy import *
a = zeros(5)

print("**** Accessing Individual Elements ****")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()

print("**** Accessing by For Loop ****")
for el in a:
	print(el)
print()

print("**** Accessing by For Loop with Index ****")
n = len(a)
for i in range(n):
	print('index',i,'=',a[i])
print()

print("**** Accessing by While Loop ****")
n = len(a)
i = 0
while i < n:
	print('index',i,'=',a[i])
	i+=1
# 1D Array using ones Function Numpy
from numpy import *
a = ones(5)
print("**** Accessing Individual Elements ****")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()

print("**** Accessing by For Loop ****")
for el in a:
	print(el)
print()

print("**** Accessing by For Loop with Index ****")
n = len(a)
for i in range(n):
	print('index',i,'=',a[i])
print()
#math operation on array using numpy
#add array
from numpy import *
a = array([101, 102, 103, 104, 105])
a = a + 5
print(a)
print("using for loop")
for el in a:
	print(el)
print()
#add two array
from numpy import *
a = array([101, 102, 103, 104, 105])
b = array([1, 2, 3, 4, 5])
c = a + b

for el in c:
	print(el)
print()
#comparing numpy array
from numpy import *
a = array([100, 200, 13, 400, 500])
b = array([100, 20, 30, 400, 50])
result1 = a == b
result2 = a < b
result3 = a > b
result4 = a <= b
result5 = a >= b
result6 = a != b
print("a", a)
print("b", b)
print("a==b",result1)
print("a<b",result2)
print("a>b",result3)
print("a<=b",result4)
print("a>=b",result5)
print("a!b",result6)
#Any and All function
from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
result = a == b
print(any(result))
print(all(result))
#Where function
from numpy import *
a = array([101, 12, 300, 4, 500])
b = array([100, 20, 30, 400, 50])
result = where(a>b, a, b)
print(result)
#Nonzero function
a=array([100,200,13,0,400,500,0])
result=nonzero(a)
print(result)
#Aliasing array
a=array([10,20,30,40,50])
b=a
print(a)
print(b)
print("a",id(a))
print("b",id(b))
#View method
from numpy import *

a = array([10, 20, 30, 40, 50])
b = a.view()
a[1] = 80
b[1] = 300
print(a)
print(b)
print("a", id(a))
print("b", id(b))
#Copy method
from numpy import *

a = array([10, 20, 30, 40, 50])
b = copy(a)
a[1] = 80
b[2] = 300
print(a)
print(b)
print("a", id(a))
print("b", id(b))
'''# Getting Input from User in 1D Array numpy
from numpy import *
n = int(input("Enter Number of Elements: "))
a = zeros(n, dtype=int)
for i in range(len(a)):
	x = int(input("Enter Element: "))
	a[i] = x
for i in range(len(a)):
	print(a[i])'''
'''# Getting Input from user in 1D Array using While Loop Numpy
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
    while (j < (len(a))):
    print(a[j])
    j += 1
print(type(a))'''
# 2D Array using Array Function Numpy
import numpy
a = numpy.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(a)
print(a.dtype)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a[1][3])

# 2D Array with Float Number using array Function Numpy Example 2
import numpy
a = numpy.array([[10, 20, 30, 40], [50, 60, 70, 80]], dtype=float)
print(a)
print(a.dtype)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a[1][3])

# 2D Array with Implicit Float Conversion using array Function Numpy Example 3
import numpy
a = numpy.array([[10, 20, 30, 40], [50, 60, 70, 8.0]])
print(a)
print(a.dtype)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a[1][3])
 
# 2D Array with String using array Function Numpy Exmaple 4
import numpy
a = numpy.array([['Rahul', 'Sonam', 'Raj', 'Rani'], ['Dell', 'Asus', 'Lenovo', 'HP']])
print(a)
print(a.dtype)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a[1][3])

# 2D Array using array Function Numpy Example 5
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(a)
print(a.dtype)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[0][3])
print(a[1][0])
print(a[1][1])
print(a[1][2])
print(a[1][3])
print()
# Accessing 2D Array using for Loop
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

for r in a:
	for c in r:
		print(c)
	print()
# Accessing 2D Array using for Loop with Index
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()

# Modifying 2D Array Element
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

a[1][2] = 100

n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()

# Accessing 2D Array using While Loop
print("while loop")
from numpy import *
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

n = len(a)
i = 0
while i < n :
	j = 0
	while j < len(a[i]):
		print('index',i,j,"=",a[i][j])
		j+=1
	i+=1
	print()
# 2D Array using zeros Function Numpy
from numpy import *
a = zeros((3,2))

print("**** Accessing Individual Elements ****")
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
print()

print("**** Accessing by For Loop ****")
for r in a:
	for c in r:
		print(c)
	print()

print("**** Accessing by For Loop with Index ****")
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print('index',i,j,"=",a[i][j])
	print()

print("**** Accessing by While Loop ****")
n = len(a)
i = 0
while i < n :
	j = 0
	while j < len(a[i]):
		print('index',i,j,"=",a[i][j])
		j+=1
	i+=1
	print()

# 2D Array using ones Function Numpy
from numpy import *
a = ones((3,2), dtype=int)

print("**** Accessing Individual Elements ****")
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
print()

print("**** Accessing by For Loop ****")
for r in a:
	for c in r:
		print(c)
	print()

print("**** Accessing by For Loop with Index ****")
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print('index',i,j,"=",a[i][j])
    print()

print("**** Accessing by While Loop ****")
n = len(a)
i = 0
while i < n :
	j = 0
	while j < len(a[i]):
		print('index',i,j,"=",a[i][j])
		j+=1
	i+=1
	print()

# reshape ( ) Function
# 1D to 2D
from numpy import *
a = array([1, 2, 3, 4, 5, 6])
b = reshape(a, (2, 3))
print(a)
print(b)
print()

# 1D to 3D
c = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
d = reshape(c, (2, 3, 2))
print(c)
print(d)
print()

#2D to 1D
e = array([[1, 2, 3], [4, 5, 6]])
f = reshape(e, (6))
print(e)
print(f)
# flatten ( ) Function
#2D to 1D
from numpy import *
e = array([[1, 2, 3], [4, 5, 6]])
f = e.flatten()
print(e)
print(f)
'''# Getting input from user in 2D Array using for Loop Numpy
from numpy import *

m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
a = zeros((m, n), dtype=int)
u = len(a)

# Input from user
for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter Element: "))
        a[i][j] = x

# Accessing 2D Array with index
for i in range(u):
    for j in range(len(a[i])):
        print('index', i, j, "=", a[i][j])

# Accessing 2D Array without index
for r in a:
    for c in r:
        print(c)

print(type(a))
# Getting input from user in 2D Array using while Loop Numpy
from numpy import *

m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))
a = zeros((m, n), dtype=int)
u = len(a)
i = 0
while (i < u):
    j = 0
    while j < len(a[i]):
        x = int(input("Enter Element: "))
        a[i][j] = x
        j += 1
    i += 1

i = 0
while i < u:
    j = 0
    while j < len(a[i]):
        print('index', i, j, "=", a[i][j])
        j += 1
    i += 1

print(type(a))'''
# Slicing 2D Array
from numpy import *
n = array([[10, 20, 30],
		   [40, 50, 60],
		   [70, 80, 90]])
print("Original Array")
print(n)

print("0th Row All Columns")
# 0th Row All Columns
a = n[0, :]
for i in a:
		print(i)

print("1st Row All Columns")
# 1st Row All Columns
b = n[1, :]
for i in b:
		print(i)

print("2nd Row All Columns")
# 2nd Row All Columns
c = n[2, :]
for i in c:
		print(i)

print("0th Column All Rows")
# 0th Column All Rows
d = n[:, 0]
for i in d:
		print(i)

print("1st Column All Rows")
# 1st Column All Rows
e = n[:, 1]
for i in e:
		print(i)

print("2nd Column All Rows")
# 2nd Column All Rows
f = n[:, 2]
for i in f:
		print(i)


print("Element 10, 0th row 0th column")
g = n[0:1, 0:1]
print(g)

print("Element 90, 2nd row 2nd column")
h = n[2:3, 2:3]
print(h)

print("0th row and 1st row of 1st column and 2nd column")
h = n[0:2, 1:3]
print(h)
#string//
str1 = 'GeekyShows'
str2 = "GeekyShows"
str3 = '''Hello Guys
Please Subscribe
GeekyShows'''
str4 = """Hello Guys
Please Subscribe
GeekyShows"""
str5 = 'Hello "Geeky Shows" How are you'
str6 = "Hello 'Geeky Shows' How are you"
str7 = "Hello \nHow are you"
str8 = r"Hello \nHow are you"

print(str1)
print("**************************")
print(str2)
print("**************************")
print(str3)
print("**************************")
print(str4)
print("**************************")
print(str5)
print("**************************")
print(str6)
print("**************************")
print(str7)
print("**************************")
print(str8)
#memory alloction 1//
str1 = "GeekyShows"
str2 = "GeekyShows"
str3 = "Python"
str4 = str3
print("str1=", str1, id(str1))
print("str2=", str2, id(str2))
print("str3=", str3, id(str3))
print("str4=", str4, id(str4))
#memory alloction 2//
str1 = "GeekyShows"
print("str1=", id(str1))
str1 = "Python"
print("str1=", id(str1))
print()
#access char//
str1 = "GeekyShows"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
print(str1[7])
print(str1[8])
print(str1[9])
print(str1)
print()
#string length//
str1 = "GeekyShows"
n = len(str1)
print(n)
print()
#Access string using for loop without index//
str1 = "GeekyShows"
for c in str1:
    print(c)
print()
##Access string using for loop with index//
str1 = "GeekyShows"
for i in range(len(str1)):
	print(str1[i])
print()
##Access string using while loop //
str1 = "GeekyShows"
i = 0
while i < len(str1) :
	print(str1[i])
	i+=1
print()
'''## It will show TypeError, you can not modify String
str1 = "GeekyShows"
str1 [4] = "i"
for c in str1:
	print(c)
print()'''
#repetition operator//
print("$" * 7)
str1 = "GeekyShows "
print(str1 * 5)

print(str1[0:5]* 3)
print()
#concatenation operator//
print("Geeky" + "Shows")
str1 = "Geeky "
str2 = "Shows"
str3 = str1 + str2
print(str3)
print()
#comparing srting//
str1 = "GeekyShows"
str2 = "GeekyShows"
str3 = "Python"
str4 = "A"
str5 = "B"
result1 = str1 == str2
result2 = str1 == str3
result3 = str4 < str5
print(result1)
print(result2)
print(result3)
print()
print("****** Upper Function ******")
name = "geekyshows"
str1 = name.upper()
print(name)
print(str1)

print("****** Lower Function ******")
name = "GEEKYSHOWS"
str1 = name.lower()
print(name)
print(str1)

print("****** Swapcase Function ******")
name = "geekyshows"
str1 = name.swapcase()
print(name)
print(str1)

print("****** Title Function ******")
name = "hello geekyshows how are you"
str1 = name.title()
print(name)
print(str1)
print()
print("****** isupper Function ******")
name = "GEEKYSHOWS"
str1 = name.isupper()
print(name)
print(str1)

print("****** islower Function ******")
name = "geekyshows"
str1 = name.islower()
print(name)
print(str1)

print("****** istitle Function ******")
name = "Hello Geekyshows How Are You"
str1 = name.istitle()
print(name)
print(str1)
print()
print("****** isdigit Function ******")
name = "342343"
str1 = name.isdigit()
print(name)
print(str1)

print("****** isalpha Function ******")
name = "GEEKyshows"
str1 = name.isalpha()
print(name)
print(str1)

print("****** isalnum Function ******")
name = "GEEKyshows2343"
str1 = name.isalnum()
print(name)
print(str1)
print()
print("****** isspace Function ******")
name = "  "
str1 = name.isspace()
print(name)
print(str1)
print("****** lstrip Function ******")
name = "   Geekyshows"
str1 = name.lstrip()
print(name)
print(str1)

print("****** rstrip Function ******")
name = "Geekyshows  "
str1 = name.rstrip()
print(name)
print(str1)

print("****** strip Function ******")
name = "   Geekyshows  "
str1 = name.strip()
print(name)
print(str1)
print()
#Function
# Write once and use it as many time as you need
# Defining Function one time
def disp():
    name = "GeekyShows"
    print("Welcome to", name)
# Calling Function as many time as we need
disp()
disp()
disp()
# Divide Large task into many small task, helpful for debuging code
# Seprate Function for Addition
def add():
    x = 10
    y = 20
    c = x + y
    print(c)
add()
# Seprate Function for Subtraction
def sub():
    x = 10
    y = 20
    c = y - x
    print(c)
sub()
print()

# Function without Argument and Parameter
# Defining a Function without Parameter
def add():
    x = 10
    y = 20
    c = x + y
    print(c)
# Calling a Function without Argument
add()
# Defining a Function with Parameter
def add(y):
    x = 10
    c = x + y
    print(c)
# Calling a Function with Argument
add(20)
# Defining a Function with Parameter
def add(y):
    x = 10.2334
    print(x + y)
    print(f"Formatted Output {x + y:5.2f}")
# Calling a Function with Argument
add(20)
print()


# Return Statement Single Value
# Defining a Function
def add():
    x = 10
    y = 20
    c = x + y
    return c
# Calling a Function
sum = add()
print(sum)
# Defining a Function
def add():
    x = 10
    y = 20
    return x + y
# Calling a Function
sum = add()
print(sum)
# Defining a Function with Parameter
def add(y):
    x = 10
    return (x + y)
# Calling a Function with Argument
sum = add(20)
print(sum)
# Return Statement Multiple Values
# Defining a Function
def add(y):
    x = 10
    c = x + y
    d = y - x
    return c, d, 50
# Calling a Function
sum, sub, a = add(20)
print(sum)
print(sub)
print(a)
print()

#Nested Function
# Example 1
def disp():
	def show():
		print("Show Function")
	print("Disp Function")
	show()

disp()

# Example 2 With Return Statement
def disp():
	def show():
		return "Show Function "
	result = show() + "Disp Function"
	return result
print(disp())

# Example 3 With Return Statement and Parameter
def disp(st):
	def show():
		return "Show Function "
	result = show() + st + " Disp Function"
	return result
print(disp("GeekyShows"))
print()

# Pass a Function as Parameter
# Example 1
def disp(sh):
    print(type(sh))
    print("Disp Function" + sh())
def show():
    return " Show Function"
disp(show)
# Example 2 with return
def disp(sh):
    return "Disp Function" + sh()
def show():
    return " Show Function"
result = disp(show)
print(result)

#Function Return another Function
# Example 1
def disp():
	def show():
		return "Show Function"
	print("Disp Function")
	return show

r_sh = disp()
print(r_sh())

# Example 2
def disp(sh):
	print("Disp Function")
	return sh

def show():
	return "Show Function"

r_sh = disp(show)
print(r_sh())
print()


# Positional Arguments
# Example 1
def pw(x, y):
    z = x ** y
    print(z)


pw(5, 2)


# Example 2
def pw(x, y):
    z = x ** y
    print(z)


pw(2, 5)

# Example 3 will show Error
# def pw(x, y):
#	z = x**y
#	print(z)

# pw(5, 2, 3)
print()


# Keyword Arguments
# Example 1
def show(name, age):
    print(f"Name: {name} Age: {age}")


show(name="GeekyShows", age=62)


# Example 2
def show(name, age):
    print(f"Name: {name} Age: {age}")


show(age=62, name="GeekyShows")

# Example 3 will show Error
# def show(name, age):
#	print(f"Name: {name} Age: {age}")

# show(name="GeekyShows", age=62, roll=101)
# Default Arguments
# Example 1
def show(name, age):
    print(f"Name: {name} Age: {age}")


show(name="GeekyShows", age=62)


# Example 2
def show(name, age=27):
    print(f"Name: {name} Age: {age}")


show(name="GeekyShows")


# Example 3
def show(name, age=27):
    print(f"Name: {name} Age: {age}")


show(name="GeekyShows", age=62)

# Example 4 will show Error
# def show(name, age=27):
#	print(f"Name: {name} Age: {age}")

# show(name="GeekyShows", age=62, roll=101)

# Variable Length Arguments
# Example 1
def add(x, y):
    z = x + y
    print("Addition:", z)


add(5, 2)


# Example 2
def add(*num):
    z = num[0] + num[1] + num[2]
    print("Addition:", z)


add(5, 2, 4)


# Example 3
def add(x, *num):
    z = x + num[0] + num[1]
    print("Addition:", z)


add(5, 2, 4)


# Keyword Variable Length Arguments
# Example 1
def add(**num):
    z = num['a'] + num['b'] + num['c']
    print("Addition:", z)


add(a=5, b=2, c=4)


# Example 2
def add(x, **num):
    z = x + num['a'] + num['b']
    print("Addition:", z)


add(3, a=5, b=2)
print()
# Anonymous Function or Lambda Function
#Example 1 Single Argument
show = lambda x : print(x)
show(5)

#Example 2 Two Arguments
add = lambda x,y : (x+y)
print(add(5, 2))

#Example 3 Return Multiple
add_sub = lambda x,y : (x+y, x-y)
a, s = add_sub(5, 2)
print(a)
print(s)

#Example 2 with Default Argument
add = lambda x,y=3 : (x+y)
print(add(5))
# Nested Lambda Function
add = lambda x=10 : (lambda y : x + y)
a = add()
print(a)
print(a(20))
# Return Lambda Function
def add():
	y = 20
	return (lambda x : x+y)

a =add()
print(a(10))
print()
# Local Variable
# Example 1
def show():
	x = 10		# Local Variable
	print(x)	# Accessing Local Variable inside Function
show()
#Accessing Local Variable outside Function
# print(x)		# It will show error

# Example 2
def add(y):
	x = 10		# Local Variable
	print(x)	# Accessing Local Variable inside Function
	print(x+y)	# Accessing Local Variable inside Function

add(20)
#Accessing Local Variable outside Function
# print(x)		# It will show error


# Global Variable
# Example 1
a = 50


def show():
    x = 10  # Local Variable
    print(x)  # Accessing Local Variable inside Function
    print(a)  # Accessing Global Variable inside Function


show()
# Accessing Global Variable outside Function
print("Global Variable A:", a)

# Accessing Local Variable outside Function, show error
# print("Global Variable X:",x)

# Example 2
i = 0


def myfun():
    a = i + 1
    print("My Function", a)


myfun()

# Example 3
i = 0


def myfun():
    # We are trying to increase global variable
    # but remember here i is treated as local variable with same name
    # and as we dont referenced it show it will show error
    #i = i + 1
    print("My Function", a)
myfun()
# Global Keyword
#Example 1
a = 50
def show():
	a = 10
	print("A:",a)		# It will show local variable value
show()
print("A:",a)			# It will show global variable value

#Example 2
a = 50
def show():
	global a
	print("A:",a)
	a = 20				# Modifiying Global Variable value
	print("A:",a)
show()
print("A:",a)			# It will show modified global variable value

# globals ( ) Function
a = 50
def show():
	a = 10
	print("Local Variable A:",a)
	x = globals()['a']
	print("X:",x)
	x = 40
	print("X:",x)
show()
print("Global Variable A:",a)
#print("X:",x)
# Recursion
# Example 1
i = 0


def myfun():
    global i
    i += 1
    print("My Function", i)
    myfun()

# Example 2
import sys

# get recursion limit
print("Default:", sys.getrecursionlimit())

# set recursion limit
sys.setrecursionlimit(3000)

print("After setting:", sys.getrecursionlimit())

from math import *

print(floor(4.5))
print(ceil(4.5))
print(sqrt(49))
print(factorial(5))
print(pow(5, 2))
#list in python
a = [10, 20, -50, 21.3, 'Geekyshows']
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
#modify of list python
a = [10, 20, -50, 21.3, 'Geekyshows']
print(a, id(a))
print(a[1])
a[1] = 40
print(a[1])
print(a, id(a))
# Accessing List using for loop
a = [10, 20, -50, 21.3, 'Geekyshows']

# without index
print("Accessing List using for Loop without index")
for element in a:
    print(element)

print()

# With Index
print("Accessing List using for Loop with index")
n = len(a)
for i in range(n):
    print(i, "=", a[i])
# Accessing List using while loop
    a = [10, 20, -50, 21.3, 'Geekyshows']

    print("Accessing List using while Loop")
    n = len(a)
    i = 0
    while i < n:
        print(i, "=", a[i])
        i += 1
# Append Method
a = [10, 20, -50, 21.3, 'Geekyshows']

print("Before Appending:")
for element in a:
	print (element)

# Appending an element
a.append(100)
print()
print("After Appending")
for element in a:
	print (element)
'''#getting list input from user in python
a = []
n = int(input("Enter Number of Elements: "))
for i in range(n):
    a.append(int(input("Enter Element:")))

print("List:")
for element in a:
    print(element)
#insert() Method
a = [10, 20, 30, 10, 90, 'Geekyshows']

print("Before:",a)

a.insert(3, 'Subscribe')

print("After:",a)

for element in a:
	print (element)'''

#pop() method

a = [10, 20, 30, 10, 90, 'Geekyshows']

print("Before POP:", a)

a.pop()

print("After POP:", a)

for element in a:
	print(element)
# pop(positon_number) method
a = [10, 20, 30, 10, 90, 'Geekyshows']

print("Before POP:", a)

n = a.pop(2)

print("After POP:", a)

for element in a:
    print(element)

print("Removed Element:", n)
#remove(element) method

a = [70, 10, 30, 10, 90, 'Geekyshows']

print("Before Remove:", a)

a.remove(10)

print("After Remove:", a)

for element in a:
	print(element)

#index() Method
a = [10, 20, 30, 10, 90, 'Geekyshows']
num = a.index(10)
print(num)
#reverse() Method
a = [10, 20, 30, 10, 90, 'GeekyShows']

print("Before Reverse:", a)

a.reverse()

print("After Reverse:", a)

for element in a:
	print(element)
# extend() Method
a = [10, 20, 30, 10, 90, 'GeekyShows']
b = [100, 200, 300]

print("Before Extend:", a)

a.extend(b)

print("After Extend:", a)

for element in a:
    print(element)

# count() Method
a = [10, 20, 30, 10, 90, 'GeekyShows']
num = a.count(10)
print(num)
#sort() Method
a = [10, 5, 90, 10, 30]

print("Before Sort",a)

a.sort()

print("After Sort",a)

for element in a:
	print(element)
# clear() Method
a = [10, 5, 90, 10, 30]

print("Before Clear", a)

a.clear()

print("After Clear", a)
#slicing on list
x = [101, 102, 103, 104, 105, 106, 107]
print("Original List")
n = len(x)
for i in range(n):
    print(i, "=", x[i])
print()

print("From 1st Position to 4th Position")
a = x[1:5]
for i in a:
    print(i)
print()

print("From 0th Position to last Position")
b = x[0:]
for i in b:
    print(i)
print()

print("From 0th Position to 4th Position")
c = x[:5]
for i in c:
    print(i)
print()

print("Last 4 Elements")
d = x[-4:]
for i in d:
    print(i)
print()

print("From 0th Position to 6th Position stride 2")
e = x[0:7:2]
for i in e:
    print(i)
print()

print("Last 5 Elements with [-5-(-3)]= 2 elements towards right")
f = x[-5:-3]
for i in f:
    print(i)

#list concatenation
    a = [10, 20, 30]
    b = [1, 2, 3]
    c = [101, 102, 103]

    print(a)
    print(b)
    print(c)

    result = a + b + c

    print(result)
#repetition of list
a = [1, 2, 3]

print(a)

result = a * 3

print(result)
#aliasing list
a = [10, 20, 30, 40, 50]
b = a
print("A:", a)
print("B:", b)

print()
print("Modifying A")
a[1] = 55
print("A:", a)
print("B:", b)

print()
print("Modifying B")
b[2] = 66
print("A:", a)
print("B:", b)

#copying and cloning list
a = [10, 20, 30, 40, 50]
b = a.copy()
print("A:", a)
print("B:", b)

print()
print("Modifying A")
a[1] = 55
print("A:", a)
print("B:", b)

print()
print("Modifying B")
b[2] = 66
print("A:", a)
print("B:", b)
#cloning list
a = [10, 20, 30, 40, 50]
b = a[:]
print("A:", a)
print("B:", b)

print()
print("Modifying A")
a[1] = 55
print("A:", a)
print("B:", b)

print()
print("Modifying B")
b[2] = 66
print("A:", a)
print("B:", b)
# Nested List
# Example 1
a = [10, 20, 30, [50, 60]]
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])

# Example 2
b = [50, 60]
a = [10, 20, 30, b]
print("A:",a)
print("B:",b)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
# Nested List
a = [[10, 20, 30], [40, 50, 60]]
print("A:",a)
print("a[0]:",a[0])
print("a[1]:",a[1])
print()
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[1][2])
# Nested List - Modification
a = [10, 20, 30, [50, 60]]

print("Before Modification A:",a)
print()
a[1] = 100
a[3][0] = 5
print("After Modification A:",a)

# Nested List - Modification
a = [10, 20, 30, [50, 60]]

print("Before Modification A:",a)
print()
a[1] = 100
a[3][0] = 5
print("After Modification A:",a)
# Nested List - Modification
a = [[10, 20, 30], [40, 50, 60]]
print("Before Modification A:",a)
print()
a[0][1] = 2
a[1][2] = 6
print("After Modification A:",a)
# Nested List - for loop
a = [10, 20, 30, [50, 60]]
n = len(a)
for i in range(n):
	if type(a[i]) is list:
		if len(a[i])>1:
			m = len(a[i])
			for j in range(m):
				print(i,j, a[i][j])
	else:
		print(i, a[i])
# Nested List - for loop
a = [[10, 20, 30], [40, 50, 60]]

# without index
for r in a:
    for c in r:
        print(c)
    print()

# With Index
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i, j, a[i][j])
    print()
# Nested List - While loop
a = [10, 20, 30, [50, 60]]

n = len(a)
i = 0
while i < n:
    # checking a[i] is a list type or not
    if type(a[i]) is list:
        if len(a[i]) > 1:
            j = 0
            m = len(a[i])
            while j < m:
                print(i, j, a[i][j])
                j += 1
            i += 1
    else:
        print(i, a[i])
        i += 1

# Nested List - While loop
a = [[10, 20, 30], [40, 50, 60]]

n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print(i, j, a[i][j])
        j += 1
    i += 1
# Slicing Nested List
x = [[10, 20, 30],
     [40, 50, 60],
     [70, 80, 90],
     [11, 22, 33],
     [44, 55, 66],
     [77, 88, 99],
     [12, 13, 14]]
print("Original List")
print(x)
print()

print("From 1st Position to 4th Position")
a = x[1:5]
print(a)
print()

print("From 0th Position to last Position")
b = x[0:]
print(b)
print()

print("From 0th Position to 4th Position")
c = x[:5]
print(c)
print()

print("Last 4 List")
d = x[-4:]
print(d)
print()

print("From 0th Position to 6th Position stepsize 2")
e = x[0:7:2]
print(e)
print()

print("Last 5 Lists with [-5-(-3)]= 2 Lists towards right")
f = x[-5:-3]
print(f)
print()

print("*****************************************************")
print("Slice Nested 2nd position, 0th position")
m = x[2:3]
print(m)
g = x[2:3][0]
print(g)
print()

print("Slice 2nd List then extract elements")
# Extracting only one specific element
h = x[2:3][0][0]
print(h)
# Extracting all elements of 2nd List
i = x[2:3][0]
for el in i:
    print(el)
print()

print("Last Nested 4 Lists then 1st position")
n = x[-4:]
print(n)
j = x[-4:][1]
print(j)
print()

print("Last Nested 4 Lists then 1st position then extract elements")
# Extracting only one specific element
k = x[-4:][1][0]
print(k)
# Extracting all elements of 2nd position
l = x[-4:][1]
for el in l:
    print(el)
print()
# Passing List to Function
def show(l):
	print(l)
	print(type(l))
	for i in l:
		print(i)

lst = [10, 20, 30, 'GeekyShows']
show(lst)
# Passing and Returning List
def show(l):
	print(l)
	print(type(l))
	for i in l:
		print(i)
	return l

lst = [10, 20, 30, 'GeekyShows']
new_lst = show(lst)
print(new_lst)
print(type(new_lst))
#higher order function filter
a = [10, 50, 60, 80, 90, 5, 45, 65]

# Without Lambda
def high_marks(n):
	if n >= 60:
		return True

result = list(filter(high_marks,a))
print(result)
print(type(result))

print()

# With Lambda
result = list(filter(lambda n : (n>=60),a))
print(result)
print(type(result))
#True and False
a = [True, False, False, True, False, True, True]

result = list(filter(None,a))
print(result)
print(type(result))

#map function
a = [10, 20, 30, 40, 50]
# Without Lambda
def inc(n):
    return n + 2


result = list(map(inc, a))
print(result)
print(type(result))

# With Lambda
result = list(map(lambda n: n + 2, a))
print(result)
print(type(result))
#dobule addition
a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]

# With Lambda
result = list(map(lambda n, m: m+n, a, b))
print(result)
print(type(result))
#reduce function
from functools import reduce
a = [10, 20, 30, 40, 50]

result = reduce(lambda n, m: m+n, a)
print(result)
print(type(result))
#generator 1
# Example 1
def disp(a,b):
	yield a
	yield b
x,y = disp(10, 20)
print(x)
print(y)
print()

# Example 2
def disp(a,b):
	yield a
	yield b
result = disp(10, 20)
print(result)
print(type(result))
# converting to list
lst = list(result)
print(lst)
print(type(lst))
#generator 2
def disp(a, b):
    yield a
    yield b
result = disp(10, 20)

print(result)
print(type(result))

print(next(result))
print(next(result))
#generator 3
def show(a, b):
    while a <= b:
        yield a
        a += 1
result = show(1, 5)
print(result)
print(type(result))

print(next(result))
print(next(result))
print(next(result))

for i in result:
    print(i)
    print()
# Tuple
# Creating Empty Tuple
a = ()

# Creating Tuple with one element
b = (10)			# It will become an integer
c = (10,)			# for creating single element tuple write comma

# Creating Tuple with Multiple element
d = (10, 20, 30, 40)
e = (10, 20, -50, 21.3, 'GeekyShows')
f = 10, 20, -50, 21.3, 'GeekyShows'			# tuple e and f are same

print()
# Access using index
print("Accessing Tuple d:")
print("d[0] =", d[0])
print("d[1] =", d[1])
print("d[2] =", d[2])
print("d[3] =", d[3])
print()

print("Accessing Tuple e:")
print("e[0] =", e[0])
print("e[1] =", e[1])
print("e[2] =", e[2])
print("e[3] =", e[3])
print("e[4] =", e[4])
print()

print("Accessing Tuple f:")
print("f[0] =", f[0])
print("f[1] =", f[1])
print("f[2] =", f[2])
print("f[3] =", f[3])
print("f[4] =", f[4])

# Access Tuple using for Loop
a = (10, 21.3, 'Geekyshows')

# Without Index
print("Access Without Index")
for element in a:
    print(element)

print()

# With Index
print("Access With Index")
n = len(a)
for i in range(n):
    print(i, a[i])

# Access Tuple using while Loop
a = (10, 21.3, 'Geekyshows')

n = len(a)
i = 0
while i<n:
	print(a[i])
	i+=1
# tuple in slicing
x = (101, 102, 103, 104, 105, 106, 107)
print("Original Tuple")
n = len(x)
for i in range(n):
    print(i, "=", x[i])
print()

print("From 1st Position to 4th Position")
a = x[1:5]
for i in a:
    print(i)
print()

print("From 0th Position to last Position")
b = x[0:]
for i in b:
    print(i)
print()

print("From 0th Position to 4th Position")
c = x[:5]
for i in c:
    print(i)
print()

print("Last 4 Elements")
d = x[-4:]
for i in d:
    print(i)
print()

print("From 0th Position to 6th Position stride 2")
e = x[0:7:2]
for i in e:
    print(i)
print()

print("Last 5 Elements with [-5-(-3)]= 2 elements towards right")
f = x[-5:-3]
for i in f:
    print(i)
#tuple  in concate
a = (10, 20, 30)
b = (1, 2, 3)
c = (101, 102, 103)

print(a)
print(b)
print(c)

result = a + b + c

print(result)

# Modifying Tuple

a = (10, 20, -50, 21.3, 'GeekyShows')
print(a)
print()

# Not Possible to Modify like below line
#a[1] = 40		# Show TypeError

# It is not possible to modify a tuple but we can concate or slice
# to achieve desired tuple

# By concatenation
print("Modification by Concatenation")
b = (40, 50)
tup1 = a + b
print(tup1)

print()

# By Slicing
print("Modification by Slicing")
tup2 = a[0:3]
print(tup2)

print()

# By Concatenation and Slicing
print("Modification by Concatenation and Slicing")
c = (101, 102)
s1 = a[0:2]
s2 = a[3:]
tup3 = s1+c+s2
print(tup3)

print()
# Deleting Tuple
a = (10, 20, -50, 21.3, 'GeekyShows')
print(a)
print()

# Not Possible to delete one element like below line
#del a[1] 		# Show TypeError

# We can delete entire tuple
#del a

#print(a)		# after deleting entire tuple a become undefined

# It is not possible to delete one element but we can concate or slice
# to achieve desired tuple
print()
# By Slicing
print("Deletion by Slicing")
tup1 = a[0:3]
print(tup1)

print()
# By Concatenation and Slicing
print("Deletion by Slicing and Concatenation")
s1 = a[0:2]
s2 = a[4:]
tup2 = s1+s2
print(tup2)

print()

# Getting input from users - Tuple
a = []

n = int(input("Enter Number of Elements: "))

for i in range(n):
	a.append(int(input("Enter Element:")))

print(type(a))
# convert list to tuple
a = tuple(a)

print(type(a))
print("Tuple:")
for element in a:
	print(element)
#repettion tuple
a = (1, 2, 3)
print(a)
result = a * 3
print(result)

#aliasing tuple
a = (10, 20, 30, 40, 50)
b = a
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))

print()
a = a[:3]
print("Id of A:", id(a))
print("Id of B:", id(b))
# Copying Tuple
a = (10, 20, 30, 40, 50)
b = a
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))

# if Same data then same object same id
# if data modified it creates new object new id

print()
b = a[0:5]
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))
# Nested Tuple
# Example 1
a = (10, 20, 30, (50, 60))
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
print()
# Example 2
b = (50, 60)
a = (10, 20, 30, b)
print("A:",a)
print("B:",b)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])
# Nested Tuple
a = ((10, 20, 30), (40, 50, 60))
print("A:",a)
print("a[0]:",a[0])
print("a[1]:",a[1])
print()
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])
print(a[1][1])
print(a[1][2])

# Nested Tuple - for loop
a = (10, 20, 30, (50, 60))
n = len(a)
for i in range(n):
	if type(a[i]) is tuple:
		if len(a[i])>1:
			m = len(a[i])
			for j in range(m):
				print(i,j, a[i][j])
	else:
		print(i, a[i])
# Nested Tuple - for loop
a = ((10, 20, 30), (40, 50, 60))

# without index
for r in a:
    for c in r:
        print(c)
    print()

# With Index
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i, j, a[i][j])
    print()

# Nested Tuple - While loop
a = (10, 20, 30, (50, 60))

n = len(a)
i = 0
while i < n:
    # checking a[i] is a tuple type or not
    if type(a[i]) is tuple:
        if len(a[i]) > 1:
            j = 0
            m = len(a[i])
            while j < m:
                print(i, j, a[i][j])
                j += 1
            i += 1
    else:
        print(i, a[i])
        i += 1
# Nested Tuple - While loop
a = ((10, 20, 30), (40, 50, 60))

n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print(i, j, a[i][j])
        j += 1
    i += 1

# Slicing Nested Tuple
x = ((10, 20, 30),
     (40, 50, 60),
     (70, 80, 90),
     (11, 22, 33),
     (44, 55, 66),
     (77, 88, 99),
     (12, 13, 14))
print("Original Tuple")
print(x)
print()

print("From 1st Position to 4th Position")
a = x[1:5]
print(a)
print()

print("From 0th Position to last Position")
b = x[0:]
print(b)
print()

print("From 0th Position to 4th Position")
c = x[:5]
print(c)
print()

print("Last 4 Tuples")
d = x[-4:]
print(d)
print()

print("From 0th Position to 6th Position stepsize 2")
e = x[0:7:2]
print(e)
print()

print("Last 5 Tuples with [-5-(-3)]= 2 Tuples towards right")
f = x[-5:-3]
print(f)
print()

print("*****************************************************")
print("Slice Nested 2nd position, 0th position")
m = x[2:3]
print(m)
g = x[2:3][0]
print(g)
print()

print("Slice 2nd tuple then extract elements")
# Extracting only one specific element
h = x[2:3][0][0]
print(h)
# Extracting all elements of 2nd tuple
i = x[2:3][0]
for el in i:
    print(el)
print()

print("Last Nested 4 Tuples then 1st position")
n = x[-4:]
print(n)
j = x[-4:][1]
print(j)
print()

print("Last Nested 4 Tuples then 1st position then extract elements")
# Extracting only one specific element
k = x[-4:][1][0]
print(k)
# Extracting all elements of 2nd position
l = x[-4:][1]
for el in l:
    print(el)
print()

# Passing Tuple to Function
def show(t):
	print(t)
	print(type(t))
	for i in t:
		print(i)

tup = (10, 20, 30, 'GeekyShows')
show(tup)

# Passing and Returning Tuple
def show(t):
	print(t)
	print(type(t))
	for i in t:
		print(i)
	return t

tup = (10, 20, 30, 'GeekyShows')
new_tup = show(tup)
print(new_tup)
print(type(new_tup))

# List of Tuples
a = [10, 20, (30,40)]

print("Original List A:", a)
print(id(a))
print()

# Appending a new Tuple
a.append((50, 60))
print("After Appending a tuple A:",a)
print(id(a))

# Accessing List of Tuple using for loop
n = len(a)
for i in range(n):
	if type(a[i]) is tuple:
		if len(a[i])>1:
			m = len(a[i])
			for j in range(m):
				print(i,j, a[i][j])
	else:
		print(i, a[i])

# Tuple of Lists
a = ([10, 20], [30,40])

print("Original Tuple A:", a)
print(id(a))
print()

# Modifying List
a[0][0] = 80
print("After Modification:",a)
print(id(a))

# Accessing Tuple of Lists using for loop
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print(i, j, a[i][j])
	print ()

# Tuple of Lists
a = (10, 20, [30,40])

print("Original Tuple A:", a)
print(id(a))
print()

# Modifying Tuple
a[2][0] = 90
print("After Modifying Tuple:",a)
print(id(a))

# Accessing Tuple of Lists using for loop
n = len(a)
for i in range(n):
	if type(a[i]) is list:
		if len(a[i])>1:
			m = len(a[i])
			for j in range(m):
				print(i,j, a[i][j])
	else:
		print(i, a[i])

# Tuple of Lists
a = ([10, 20], [30,40])

print("Original Tuple A:", a)
print(id(a))
print()

# Modifying List
a[0][0] = 80
print("After Modification:",a)
print(id(a))

# Accessing Tuple of Lists using for loop
n = len(a)
for i in range(n):
	for j in range(len(a[i])):
		print(i, j, a[i][j])
	print ()

# Sets

#Creating Empty Set
x = set()

#Cretaing Set with elements
a = {10, 20, 'GeekyShows', 'Raj', 40}

# Cant access using index
# print(a[0])		# It will show error
print(a)
print(id(a))
print()

# Duplicates are avoided
b = {10, 20, 'GeekyShows', 'Raj', 40, 10, 10}
print(b)
print()

# Adding one Element
print("Adding one Element:")
a.add('Python')
print(a)
print(id(a))
print()

#Adding Multiple Elements
print("Adding Multiple Element:")
a.update([101, 102, 103])
print(a)
print(id(a))
print()

#Deleting Element using discard() method
print("Removing Element using discard:")
a.discard('GeekyShows')
print(a)
print(id(a))
print()

#Deleting Element using remove() method
print("Removing Element using remove:")
a.remove('Raj')
print(a)
print(id(a))
print()

# Access Set using for loop

#Cretaing Set with elements
a = {10, 20, 'GeekyShows', 'Raj', 40}

for i in a:
	print(i)
# Getting input from user
# Empty Set
'''a = set()
print(id(a))
n = int(input("Enter number of Elements: "))

for i in range(n):
	el = input("Enter Element: ")
	a.add(el)

# Accessing set
for i in a:
	print(i)

print(id(a))'''

# Sets - clear() Method

a = {10, 20, 'GeekyShows'}
print("Before Clear",a)
print(id(a))
print()

a.clear()

print("After Clear",a)
print(id(a))

# Sets - copy() Method

a = {10, 20, 'GeekyShows'}
print("Before Copy",a)
print(id(a))
print()

new_a = a.copy()

print("After Copy", new_a)
print(id(new_a))

# Set Methods

a = {'Rahul', 'Raj', 'Sonam', 'Rani'}
b = {'Sumit', 'Rahul', 'Rani', 'Python', 'Java'}

print("A:",a)
print("B:",b)
print()

# intersection() Method
	# returns item which exists in both sets
ism = a.intersection(b)
print("Intersection:", ism)
print()

# union() Method
	# Returns all item from original set and all items from specified set
um = a.union(b)
print("Union:", um)
print()

# difference() Method
	# Returns items that exist only in first set, and not in both sets
dm = a.difference(b)
print("Difference:", dm)
print()

# issubset() Method
	#Returns True if all items in the set exists in the specified set
isub = a.issubset(b)
print("issubset:", isub)
print()

# issuperset() Method
  # Returns True if all items in the specified set exists in the original set
isup = a.issuperset(b)
print("issuperset:", isup)
print()
# Passing Set to Function
def show(s):
	print(s)
	print(type(s))
	for i in s:
		print(i)

st = {10, 20, 30, 'GeekyShows'}
show(st)

# Passing and Returning Set
def show(s):
	print(s)
	print(type(s))
	for i in s:
		print(i)
	return s

st = {10, 20, 30, 'GeekyShows'}
new_st = show(st)
print(new_st)
print(type(new_st))

# Modifying Dictionary

stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Before Modification:")
print(stu)
print(id(stu))
print()

stu[102] = 'Python'
print("After Modification:")
print(stu)
print(id(stu))
print()

# Adding new item to Dictionary

stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Before Adding:")
print(stu)
print(id(stu))
print()

stu[104] = 'GeekyShows'
print("After Adding:")
print(stu)
print(id(stu))
print()

# Deletion

stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Before Deletion:")
print(stu)
print(id(stu))
print()

del stu[102]
print("After Deletion:")
print(stu)
print(id(stu))
print()

# Testing Keys

stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }

print(101 in stu)

print(100 in stu)

print(100 not in stu)

print(101 not in stu)

# Dictionary - clear() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Before Clearing:")
print(stu)
print()

stu.clear()
print("After Clearing:")
print(stu)

# Dictionary - copy() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

new_stu = stu.copy()
print("Copied Dict:")
print(new_stu)
print(id(new_stu))

# Dictionary - fromkeys() Method
key = (101, 102, 103)
value = 'GeekyShows'
d = dict.fromkeys(key, value)
print("New Dict:")
print(d)
print(id(d))
print()

n = dict.fromkeys(key)
print("New Dict:")
print(n)
print(id(n))

# Dictionary - get() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

print(stu.get(101))

print(stu.get(104))

print(stu.get(104, 'GeekyShows'))

# Dictionary - get() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

print(stu.get(101))

print(stu.get(104))

print(stu.get(104, 'GeekyShows'))

# Dictionary - items() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

it = stu.items()
print(it)
print()
# converting into list
lst = list(it)
# printing converted list
print(lst)
print()
# accessing one element
print(lst[0])
print(lst[0][0])
print(lst[0][1])
print()
for r in lst:
	for c in r:
		print(c)
# Dictionary - keys() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

all_keys = stu.keys()
print(all_keys)
print()
# converting into list
keys_lst = list(all_keys)
# printing converted list
print(keys_lst)
print()
# accessing one element
print(keys_lst[0])
print(keys_lst[1])
print(keys_lst[2])
print()
for k in keys_lst:
		print(k)
# Dictionary - values() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print()

all_values = stu.values()
print(all_values)
print()
# converting into list
values_lst = list(all_values)
# printing converted list
print(values_lst)
print()
# accessing one element
print(values_lst[0])
print(values_lst[1])
print(values_lst[2])
print()
for v in values_lst:
		print(v)
# Dictionary - update() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

stu.update({106: 'Python'})
print("Updated Dict:")
print(stu)
print(id(stu))
print()

vals = {'name': 'Rahul', 'Address': 'Ranchi', 105: 'GeekyShows'}
stu.update(vals)
print("Updated Dict:")
print(stu)
print(id(stu))
print()

# Dictionary - pop() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

removed_value = stu.pop(102)
#removed_value = stu.pop(106)	# Key is not found so KeyError
print("After Removing Dict:")
print(stu)
print(id(stu))
print("Removed Value:", removed_value)
print()

default_value = stu.pop(106, 'GeekyShows')
print("After Removing Dict:")
print(stu)
print(id(stu))
print("Default Value:", default_value)
print()

# Dictionary - popitem() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

removed_item = stu.popitem()
print("After Removing Dict:")
print(stu)
print(id(stu))
print("Removed Value:", removed_item)
print()

# Dictionary - setdefault() Method
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam' }
print("Original Dict:")
print(stu)
print(id(stu))
print()

#returned_value = stu.setdefault(102)
returned_value = stu.setdefault(109, 'Rohit')
print("After Set Default Dict:")
print(stu)
print(id(stu))
print("returned Value:", returned_value)
print()

# Accessing Dictionary using for loop
stu = {101: 'Rahul', 102: 'Raj', 103: 'Sonam'}

# Accessing Single Value
print(stu[101])

# Display Keys
for k in stu:
    print(k)

# Display Values
for k in stu:
    print(stu[k])
print()
'''# Getting input from user

# Creating Empty Dict
a = {}

n = int(input("Number of Elements: "))

for i in range(n):
    k = input("Enter Key: ")
    v = input("Enter Value: ")
    a.update({k: v})

print(a)'''

# Nested Dictionary EX-1
a = {'course': 'Python', 'fees':15000, 1: {'course': 'JavaScript', 'fees': 10000 } }

# Accessing Nested Dictionary
print(a['course'])
print(a['fees'])
print(a[1]['course'])
print(a[1]['fees'])
print()

print("Original: ")
print(a)
print()

# Modifying Nested Dictionary
a['course'] = 'Machine Learning'
a[1]['fees'] = 200000
print("After Modification: ")
print(a)
print()

# Deletion
del a[1]['course']
print("After Deletion: ")
print(a)
print()

# Adding New item
a['duration'] = '6 months'
a[1]['Teacher'] = 'GeekyShows'
print("After Addition: ")
print(a)
print()

# Adding Dictionary inside Dictionary
a[2] = {'course': 'ReactJS', 'fees': 30000}
print("After Adding a Dict: ")
print(a)
print()

# Nested Dictionary EX-2
a = {1: {'course': 'Python', 'fees':15000},
	 2: {'course': 'JavaScript', 'fees': 10000 } }

# Accessing Nested Dictionary
print(a[1]['course'])
print(a[2]['fees'])
print()

print("Original: ")
print(a)
print()

# Modifying Nested Dictionary
a[1]['course'] = 'Machine Learning'
a[2]['fees'] = 200000
print("After Modification: ")
print(a)
print()

# Deletion
del a[1]['course']
print("After Deletion: ")
print(a)
print()

# Adding New item
a[1]['duration'] = '6 months'
a[2]['Teacher'] = 'GeekyShows'
print("After Addition: ")
print(a)
print()

# Adding Dictionary inside Dictionary
a[3] = {'course': 'ReactJS', 'fees': 30000}
print("After Adding a Dict: ")
print(a)
print()
#  EX-1 Accessing Nested Dictionary using For loop
a = {'course': 'Python', 'fees': 15000, 1: {'course': 'JavaScript', 'fees': 10000}}

# Accessing each id keys -- value
for i in a:
    if type(a[i]) is dict:
        for k in a[i]:
            print(k, '=', a[i][k])
    else:
        print(i, '=', a[i])

#  EX-2 Accessing Nested Dictionary using For loop
a = {1: {'course': 'Python', 'fees': 15000},
     2: {'course': 'JavaScript', 'fees': 10000}}

# Accessing ID
print("ID:")
for id in a:
    print(id)
print()

# Accessing each id keys
for id in a:
    for k in a[id]:
        print(k)
print()

# Accessing each id keys -- value
for id in a:
    for k in a[id]:
        print(id, '=', k, '=', a[id][k])

# Passing Dictionary to Function
def show(d):
	print(d)
	print(type(d))
	for k in d:
		print(k,'=',d[k])

dc = {101:'Rahul', 102:'Raj', 103:'Sonam'}
show(dc)

# Passing and Returning Dictionary
def show(d):
	print(d)
	print(type(d))
	for k in d:
		print(k,'=',d[k])
	return d

dc = {101:'Rahul', 102:'Raj', 103:'Sonam'}
new_dc = show(dc)
print(new_dc)
print(type(new_dc))

# List Comprehension

# Without List Comprehension
lst1 =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_lst1 =[]
for i in lst1:
	new_lst1.append(i+1)
print(new_lst1)

# With List Comprehension
lst2 =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_lst2 =[i+1 for i in lst2]
print(new_lst2)
print()

# Same as above in different way

# Without List Comprehension
lst1 =[]
for i in range(20):
	lst1.append(i+1)
print(lst1)

# With List Comprehension
lst2 =[i+1 for i in range(20)]
print(lst2)

# List Comprehension

# Without List Comprehension (Conditional)
lst1 =[]
for i in range(20):
	if(i%2==0):
		lst1.append(i)
print(lst1)

# With List Comprehension (Conditional)
lst2 =[i for i in range(20) if i%2==0]
print(lst2)

# List Comprehension

# Without List Comprehension (Conditional)
lst1 =[]
for i in range(20):
	if(i%2==0):
		if(i%3==0):
			lst1.append(i)
print(lst1)

# With List Comprehension (Conditional)
lst2 =[i for i in range(20) if i%2==0 if i%3==0]
print(lst2)

# List Comprehension

# Without List Comprehension (if else)
lst1 =[]
for i in range(10):
	if(i%2==0):
		lst1.append(i)
	else:
		lst1.append("Invalid")
print(lst1)

# With List Comprehension (if else)
lst2 =[i if i%2==0 else "Invalid" for i in range(10)]
print(lst2)

# Nested List Comprehension

lst = [[i * j for j in range(4, 7)] for i in range(6, 8)]
print(lst)

# Below Code is only for explanation you can ommit
a = [[24, 30, 36], [28, 35, 42]]
for i in range(6, 8):
    for j in range(4, 7):
        pass

# Set Comprehension
# Without Set Comprehension
set1 ={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set1 =set()
for i in set1:
	new_set1.add(i+1)
print(new_set1)
print(type(new_set1))

# With Set Comprehension
set2 ={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set2 ={i+1 for i in set2}
print(new_set2)
print(type(new_set2))
print()

# Same as above in different way

# Without Set Comprehension
set1 =set()
for i in range(20):
	set1.add(i+1)
print(set1)
print(type(set1))

# With Set Comprehension
set2 ={i+1 for i in range(20)}
print(set2)
print(type(set2))

# Set Comprehension

# Without Set Comprehension (Conditional)
set1 =set()
for i in range(20):
	if(i%2==0):
		set1.add(i)
print(set1)
print(type(set1))

# With Set Comprehension (Conditional)
set2 ={i for i in range(20) if i%2==0}
print(set2)
print(type(set2))

# Set Comprehension

# Without Set Comprehension (Conditional)
set1 =set()
for i in range(20):
	if(i%2==0):
		if(i%3==0):
			set1.add(i)
print(set1)
print(type(set1))

# With Set Comprehension (Conditional)
set2 ={i for i in range(20) if i%2==0 if i%3==0}
print(set2)
print(type(set2))

# Set Comprehension

# Without Set Comprehension (if else)
set1 =set()
for i in range(10):
	if(i%2==0):
		set1.add(i)
	else:
		set1.add(i*1000)
print(set1)
print(type(set1))

# With Set Comprehension (if else)
set2 ={i if i%2==0 else i*1000 for i in range(10)}
print(set2)
print(type(set2))

# Nested Set Comprehension
st ={(i, j) for j in range(4,7) for i in range(6,8)}
print(st)
print(type(st))

# Nested Set Comprehension
st ={(i, j) for j in range(4,7) for i in range(6,8)}
print(st)
print(type(st))

# Dictionary Comprehension
lst = [(101, "Rahul"), (102, "Raj")]
dict1 = {k:v for k,v in lst}
print(dict1)

# Dictionary Comprehension

# Without Dict Comprehension
dict1 = {}
for n in range(10):
	dict1[n]=n*2
print(dict1)

# With DIct Comprehension
dict2 = {n:n*2 for n in range(10)}
print(dict2)

# Dictionary Comprehension

# Without Dict Comprehension (Conditional)
dict1 = {}
for n in range(10):
	if n%2==0 :
		dict1[n]=n*2
print(dict1)

# With Dictionary Comprehension (Conditional)
dict2 = {n:n*2 for n in range(10) if n%2==0}
print(dict2)
# Dictionary Comprehension

# Without Dict Comprehension (Nested Conditional)
dict1 = {}
for n in range(10):
	if n%2==0 :
		if n%3==0:
			dict1[n]=n*2
print(dict1)

# With Dictionary Comprehension (Nested Conditional)
dict2 = {n:n*2 for n in range(10) if n%2==0 if n%3==0}
print(dict2)

# Dictionary Comprehension

# Without Dict Comprehension (If Else)
dict1 = {}
for n in range(10):
	if n%2==0 :
		dict1[n]=n
	else:
		dict1[n]="Invalid"
print(dict1)

# With Dictionary Comprehension (If Else)
dict2 = {n:(n if n%2==0 else "Invalid") for n in range(10)}
print(dict2)

a = 10
b = 30.23
c = "String"
d = [10, 20, 30]
e = (10, 20, 30)
f = {10, 20, 30}
g = {101:'Rahul', 102:'Raj', 103:'Sonam'}

# id  () Function
print(id(a))
print()

# type() Function
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print()

# getsizeof() Function
from sys import getsizeof
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))
print(getsizeof(d))
print(getsizeof(e))
print(getsizeof(f))
print(getsizeof(g))

# int () Function
a = 10.56
print("Float:",a)
print(type(a))
new_a = int(a)
print("Int:",new_a)
print(type(new_a))
print()

b ="10"
print("String:",b)
print(type(b))
new_b = int(b)
print("Int:",new_b)
print(type(new_b))
print()

# Below code will show error
c ="GeekyShows"
print("String:",c)
print(type(c))
new_c = int(c)
print("Int:",new_c)
print(type(new_c))

# float () Function
a = 10
print("Int:",a)
print(type(a))
new_a = float(a)
print("Float:",new_a)
print(type(new_a))
print()

b ="10.56"
print("String:",b)
print(type(b))
new_b = float(b)
print("Float:",new_b)
print(type(new_b))
print()

# Below code will show error
c ="GeekyShows"
print("String:",c)
print(type(c))
new_c = float(c)
print("Float:",new_c)
print(type(new_c))

# str () Function
a = 10
print("Int:",a)
print(type(a))
new_a = str(a)
print("String:",new_a)
print(type(new_a))

print()

b = 10.56
print("Float:",b)
print(type(b))
new_b = str(b)
print("String:",new_b)
print(type(new_b))

# list() Function
a = (10,20,30)
print(a)
print(type(a))
new_a = list(a)
print(new_a)
print(type(new_a))
print()

b = {10,20,30}
print(b)
print(type(b))
new_b = list(b)
print(new_b)
print(type(new_b))
print()

c = "GeekyShows"
print(c)
print(type(c))
new_c = list(c)
print(new_c)
print(type(new_c))
print()

d = {101:'Rahul', 102:'Raj', 103:'Sonam'}
print(d)
print(type(d))
new_d = list(d)
print(new_d)
print(type(new_d))
print()

# tuple() Function
a = [10,20,30]
print(a)
print(type(a))
new_a = tuple(a)
print(new_a)
print(type(new_a))
print()

b = {10,20,30}
print(b)
print(type(b))
new_b = tuple(b)
print(new_b)
print(type(new_b))
print()

c = "GeekyShows"
print(c)
print(type(c))
new_c = tuple(c)
print(new_c)
print(type(new_c))
print()

d = {101:'Rahul', 102:'Raj', 103:'Sonam'}
print(d)
print(type(d))
new_d = tuple(d)
print(new_d)
print(type(new_d))
print()

# set() Function
a = [10,20,30]
print(a)
print(type(a))
new_a = set(a)
print(new_a)
print(type(new_a))
print()

b = (10,20,30)
print(b)
print(type(b))
new_b = set(b)
print(new_b)
print(type(new_b))
print()

c = "GeekyShows"
print(c)
print(type(c))
new_c = set(c)
print(new_c)
print(type(new_c))
print()

d = {101:'Rahul', 102:'Raj', 103:'Sonam'}
print(d)
print(type(d))
new_d = set(d)
print(new_d)
print(type(new_d))
print()

# dict() Function
a = [(101, 'Rahul'), (102, 'Raj'), (103, 'Sonam')]
print(a)
print(type(a))
new_a = dict(a)
print(new_a)
print(type(new_a))
print()

# len() Function
a = "GeekyShows"
b = [10, 20, 30]
c = (10, 20, 30, 40)
d = {10, 20, 30, 40, 50}
e = {101:'Rahul', 102:'Raj', 103:'Sonam'}
f = [[10, 20], [30, 40], [60, 70]]
g = [(101, 'Rahul'), (102, 'Raj'), (103, 'Sonam')]
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print(len(g))
print()

 # min() Function
b = [10, 20, 30, 5]
c = (10, 20, 30, 6, 40)
d = {10, 20, 30, 9,  40, 50}
e = {101:'Rahul', 102:'Raj', 103:'Sonam', 2:'Jay'}
f = [[10, 20], [30, 40], [60, 70], [2, 4]]
g = [(101, 'Rahul'), (102, 'Raj'), (2, 'Jay'), (103, 'Sonam')]
print(min(b))
print(min(c))
print(min(d))
print(min(e))
print(min(f))
print(min(g))
print()
# max() Function
b = [10, 20, 30, 5]
c = (10, 20, 30, 6, 40)
d = {10, 20, 30, 9,  40, 50}
e = {101:'Rahul', 102:'Raj', 103:'Sonam', 2:'Jay'}
f = [[10, 20], [30, 40], [60, 70], [2, 4]]
g = [(101, 'Rahul'), (102, 'Raj'), (2, 'Jay'), (103, 'Sonam')]
print(max(b))
print(max(c))
print(max(d))
print(max(e))
print(max(f))
print(max(g))
print()

# sorted() Function
b = [10, 20, 30, 5]
c = (10, 20, 30, 6, 40)
d = {10, 20, 30, 9,  40, 50}
e = {101:'Rahul', 102:'Raj', 103:'Sonam', 2:'Jay'}
f = [[10, 20], [60, 70], [2, 4], [30, 40]]
g = [(101, 'Rahul'), (102, 'Raj'), (2, 'Jay'), (103, 'Sonam')]
print(sorted(b))
print(sorted(c))
print(sorted(d))
print(sorted(e))
print(sorted(f))
print(sorted(g))
print()

# Membership
a = "GeekyShows"
b = [10, 20, 30, 5]
c = (10, 20, 30, 6, 40)
d = {10, 20, 30, 9,  40, 50}
e = {101:'Rahul', 102:'Raj', 103:'Sonam', 2:'Jay'}
print("String:")
print('G' in a)
print('G' not in a)
print()
print("List:")
print(10 in b)
print(10 not in b)
print()
print("Tuple:")
print(10 in c)
print(10 not in c)
print()
print("Set:")
print(10 in d)
print(10 not in d)
print()
print("Dictionary:")
print(101 in e)
print(101 not in e)
































































































































































 

























































































