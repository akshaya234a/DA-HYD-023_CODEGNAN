'''
Tokens --> variables,Punctuators

Variables --> Named memory location,it's a placeholder for data

#rules to be followed


#multiAssignment of variables

name,age,place = 'Codegnan',7,'HYD'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='-->')

#a,b=2,3,4 #valueError as too many values to unpack
#reassigning variables

name="codegnan"
a,b=45,1.5
print(a,b)
a,b=b,a
print(a,b,sep=',')

#sa,b=b,c #nameError
#print(a,b)

#deleting the variables -->del
#del a
#print(a)
#del a,b
#print(a,b)

#Punctuators --> [],(),{} --they represent the notations in python.. [](list),()(tuples),{}(dict,sets)
name = "codegnan";age = 7;course='DA'
print(name,age,course)

#Datatypes --> Numeric (int,float,complex,boolean,None)
        # --> Sequences -->Lists.Tuples,Sets,Strings,Frozensets,mappings(dict)

#Numeric type --> int,float,complex

#int datatype --> quantity,age..
age=7
print(age)
print(type(age))

print(type(234))

#quantity =03 #Zero not allowed
#print(quantity)

#float datatype --> temp,salary,price
price= 750.24;discount=2.5
print(price,discount)
print(type(price))

#complex --> combination of real and imaginary
#data=5+2i #syntaxError
#print(type(data))

i2=4
data = 5 +i2
print(data)

data =5+2j  # j is imaginary representation
print(data)
print(type(data))

#Boolean --> True/False

valid = True
print(type(valid))

error= False
print(type(error))

#TypeCasting -->Converting one type to another type
#python by default follows Implicit Type (we need not mention the datatype)

#we will go for Explicit Conversion
#Every built-in dataype is a built-in function
#int,float,complex,bool

#TypeCasting --> int -->float,complex,bool

age=35
print(type(age))
a=float(age)
print(b)
b=complex(age)
print(b)
d=bool(age) #returns True for existing data
print(d)
e= bool(0)
print(e)

# coverting float into int,complex,bool 
price=125.10
print(type(price))
b=int(price)
print(b)
print(type(b))
c=complex(price)
print(c)
print(type(c))      
d=bool(price)
print(d)
e = bool(0)
print(e)
'''

'''
#converting complex into int 
data =2+5j
print(type(data))
#b=int(data)
#print(b)
#c=float(data)
#print(c)
d= bool(data)
print(d)
print(type(d))
'''

'''
e=int(float(bool(45)))
print(e)
e=bool(int(float(25)))
print(e)
'''

f=45+2.5 +2 +3j +False
print(f)
