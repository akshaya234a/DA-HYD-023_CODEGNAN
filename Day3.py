#Numeric data type --> int,float,complex along with boolean

#input formatting --> Accepting input from the user --> input()

#Accepting integer input from user
#by default input fun accepts any data in string format
#int(input()) accepts only in integer format
''''
age=int(input("enter age:")) #by default input fun accepts any data in string format
print(age)
print(type(age))

#float(input()) Accepts only in float format
age=float(input("enter age:"))
print(age)
print(type(age))

#Accepting string input from user
name=input("Enter name:")
print(name)
print(type(name))          

marks=int(input("Enter marks:")).split #split is used for split
print(marks)          

#space separated values
a=input().split() #now you enter spaces in output
print(a)

#commma separated values
a=input("Enter values:").split(',')
print(a)


#List of integers (if we need more values use list)
marks=list(map(int,input("Enter values:").split(',')))
print(marks)

#Now we wanted to accept two values from user
age,salary =map(int,input("Enter values:").split(','))
print(age)
print(salary)

#Single input --> int(input())
#two inputs --> a,b =map(int,input().split(','))
#Any number result as list --> a= list(map(int,input().split(',')))

#group of float values
age,salary =map(float,input("Enter values:").split(','))
print(age)
print(salary)

#list of float
marks=list(map(float,input("Enter values:").split(',')))
print(marks)

#Accepting input from user --> int,float --> input formatting

#Operators --> Operators perform operations between values (operands)
#7 types --> Arithmetic,Assignment,Comparison(Relationship)
#Membership,Identity,Logical,Bitwise

#Arithmetic Operators --> performs arithmetic operations
# +,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)#Float value
print(5//3) #quotient
print(5%3) #Reminder

a=12
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)#Float value
print(a//b) #quotient
print(a%b)

#Arithmetic Operators --> performs arithmetic operations
# +,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)#Float value
print(5//3) #quotient
print(5%3) #modulus --> divisible rules --?Returns Remainder
print(5**3) #Exponential


#Task --> Accept integer input as length,breadth -->find area of rectangle
#area= length * breadth

length = 16
breadth = 10
area=length * breadth
print(area)

length,breadth = 16,10
area = length * breadth
print(area)

length = int(input("Enter value:"))
breadth= int(input("Enter value:"))
area=length * breadth
print(area)             

length,breadth = map(int,input("Enter values:").split(','))
area =length * breadth
print(area)

#Assigment operators -->assign the values
# =,+=,-=
a=45
print(a)
#update the value of a
a= a+5 # a+=5
print(a)

b= 35
b +=a  #b=b+a
print(b)

b-=5
print(b)

#Task : *=,/=,//=,%=,**= 
b *=3
print(b)
b /=8
print(b)
b //=6
print(b)
b %= 12
print(b)
b **= 6
print(b)

#Comparison Operators --> we compare the values --> boolean
# == (equal to),!= (not equal to),<(less than),>(greater than)
#<=(less than or equal to),>=(greater than or equal to)

age= 25
print(age ==25) #returns boolean output
print(age !=25)
print(age<25)
print(age<=25)
print(age>25)
print(age>=25)

#Membership Operators --> in,not in(in--> True,not in --> False)
#it checks for the existance of an object in a collection

marks =[56,75,45,85]
print(35 in marks)

marks =[56,75,45,85]
print(35 not in marks)
print('code' in 'codegnan')


#Logical operators --> logical decision making --> and,or,not
#and --> all conditions to be satisfied
#or --> any one condition to be satisfied
a = (25 in [25,45,65]) and 45 < 65
print(a)
b=45 >56 or 25 <=45
print(b)
c= not True
print(c)

#Identity Operators --> check for identity of an object --> id()

a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)
'''

a=[1,3,4,5]
print(id(a))
c=a
print(id(c))
print(c is a)












