'''
Functions --> Variable length arguments(*args)
        --> Keyword variable length arguments (**kwargs)

variable length arguments --> The number of positional arguments are not limit
we can pass any number of arguments,but we need to use the * representataion,data is stored in tuple


def sample(*args):
    """simple demo for *args"""
    print(args)
    print(type(args))
sample() #no arguments
sample(1,3,4,6) #any number
sample('codegnan','akshaya',23)
details=[24,45,36,65]
sample(details) #passing a collection
sample(*details) #unpacking values from collection

#* is used for unpacking the values into a collection
a,b,c=13,4,'da'
print(a,b,c)
a,*b,c='codegnan','python',23,45.6,7,'data'
print(a,*b,c)
print(*b) #returns python 23 45.6,7
a,b,*c=34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)


#Task --> we wanted to calculate the sum of given objects using function
def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #Take output variable as a result
    result = 0
    for i in a:
        #print(i)
        if type(i) == int or type(i) == float:
            result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4.5))
#print(add(3,4,5,'poll','dear',4.5))
#print(add(23,4,5.5,2+4j,56,'code',23))
b=list(map(int,input("enter values:").split(',')))
print(b)
#print(*b) #returns each value side by side
#print(add(*b)) #unpacks the values from collection
print(*b)
for i in b:
    print(i,end='')
    
#Keyword variable length arguments --> we can pass any number of keyword
arguments we use ** representation,data is stored in dictionary

def details(**kwargs):
    """usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details() #returns empty dictionary    
#details(2,3,4,6) #raises TypeError
details(batch='DA',place='hyderabad',name='codegnan')
batch = {'number':'da23','place':'hyd'}
print(**batch)
'''
#Now let us include both of the item into a function
def sample(*a,**b):
    """Usage of both variable length and keyword variable length args"""
    result =0
    for i in a :
        if type(i) in (int,float,complex):
            result = result +i
    #print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
    return result    
print(sample(2,4,5,'police','codegnan',3.5,
       name='codegnan',
       place='hyd',
       batch='da23'))
#sample(name='codegnan',23,ids=23445) #positional args follows keyword args