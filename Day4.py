'''
Identity Operators --> checks the identity of an object --> id()
id() is an built in function which returns the memory location

a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(5 == 5)

a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#As we have lists (mutable collection --> can modify),both c and a lists will have different
#ids whereas values are same
print( Bitwise operators --> we perform bitwise operations over operands
# &(and) ,| (or), ^(XOR),shifting operators(<<,>>)
#number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3)#bitwise OR

print(5^3) #Bitwise XOR

print(5 and 3) #Where and is logical operator checks for both existances
#returns 5 in above case
print(5 or 3) # returns 3 in this case

#Leftshift Operator <<,Right Shift Operator >>

print(5 < 1) #False Comparison
print(5 << 1) #Left shift operation by 1 position
print(5 >> 1) #Right shift operation

print(15 << 2) #convert 15 to binary and perform 2 times left shifting
print(15 >> 2) # same 2 times right shifting]

#Input Formatting --> input(),int(input()),float(input())
#You Know --> single input
#2 or 3 inputs -->map()
#group of integers --> list(map(int,input(),split(','))

names = input("Enter the names:").split(',')
print(names)

name1,name2 =map(str,input("Enter the Friends names:").split(','))
print(name1,name2)

#Tokens -->Numeric Datatypes --> Operators --> flow of the program
#control Block Statements --> they control the flow of program
#when to execute ,how to execute
#Conditional Statements --> if,else,elif,(rely on condition to be executed)
#Repetition statements(Loops) --> for,while

Syntax :
    
if <condition>:
    statement(s)...
    ...

age=int(input("Enter age:"))
if age >= 18:
    print("Your Age is:",age)

age=int(input("Enter the age:"))
if age>=18 and age in[19,21,20]:
    print("your age is:",age)
print(age)


#else keyword --> if-else
else:
    statement(S)..

if-else usage as below:

if<condition>:
    statement(S)...
    ...
else:
    statements(S)...
    ....
 

#vote Eligibility --> To check his/her voter eligibility and give access...

age=int(input("Enter the age:"))

if age>=18:
    print("You have Voter eligibility and age is",age)
    print("Access Granted")
else:
    age=18-age
    print("you don't have eligibility as your age is",age,"years less")
    print("you need to wait for more",age,"years")

#same case let's use only nested --> if,else
age=int(input("Enter the age:"))
if age>0:
    if age>=18:
        print("You have Voter eligibility and age is",age)
        print("Access Granted")
    else:
        age=18-age
        print("you don't have eligibility as your age is",age,"years less")
        print("you need to wait for more",age,"years")
else:
    print("you have entered -ve values/zero enter only +ve")

task:  student marks and grade analyzer
90-100 --> 'A'
80-89 --> 'B'
70-79 --> 'C'
60-69 --> 'D'
<60 --> Fail
#also -ve cases should not be allowed and marks shouldn't be greater than 100


marks = int(input("Enter marks:"))
if marks < 0:
    print("-ve cases should not be allowed and marks shouldn't be greater than 100")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("B")
elif marks >=60:
    print("D")
else:
    print("Fail")                


marks = int(input("Enter marks:"))
if marks < 0:
    print("-ve cases should not be allowed and marks shouldn't be greater than 100")
if marks >= 90:
    print("A")
if marks >= 80:
    print("B")
if marks >= 70:
    print("B")
if marks >=60:
    print("D")
else:
    print("Fail")
'''               


marks = int(input("Enter marks:"))
if marks > 0 and marks <=100:
    if marks >= 90:
        print("A")
    if marks >= 80 and marks <=89:
        print("B")
    if marks >= 70 and marks <=79:
        print("C")
    if marks >=60 and marks <=69:
        print("D")
    if marks < 60: 
        print("Fail")
else:
    print("Enter only +ve values greater than 0 and less than 100")





