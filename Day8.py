'''
Sequences -->strings,lists,sets,tuples,mapping(dict)

#strings --> group of characters we use single or double or triple quotes
#for representation of strings...
#strings are immutable,ordered,indexed collection
#In Python space is also an character
name='codegnan'
print(name)
print(type(name))
print(len(name)) #len-->returns the number of items in container

#Index() is used to fetch the object(position) starts at 0 and ends at len(obj)
print(name[0])
print(name[5])
#print(name[25]) #IndexError --> as its out of range

#Negative Indexing --> -1 to len(obj)
print(name[-1])
print(name[-3])
#print(name[-33]) index error
print(name[-1:-4])

#Slicing --> we can access group of characters(objects)
#we use [start:end] #start default -->0 start is included,end is excluded
name='codegnan'
print(name)
print(name[:]) #we get entire string
print(name[0:]) #it returns entire string
print(name[:4]) #starts at 0th index before 4th index
print(name[1:5]) #prints odeg
print(name[0:5]) #prints codeg
'''
'''
#Example
course="Data Analytics"
print(course)
print(course[0:4])
print(course[5:14])
print(course[5:11])
print(course[2:8])

name="python"
print(name)
print(name[3:7]) 
#print(name[7:3]) #returns empty string bcz slicing is applicable from lower index to higher index
# returns empty as strings are immutable
print(name[:45]) #returns till end of the string
#print(name[45:]) #returns empty

name="Akshaya"
print(name)
#print(name[-1:-5])#returns empty string
print(name[-5:-1]) #starts at -5 and ends at -2
print(name[-2:])
print(name[-7:])
print(name[1:-2])

#Task
#Observe +ve+ve,-ve-ve, & +ve-ve all possibilities
#Striding -->[start:end:step]

course='DataAnalysis'
print(len(course)) #prints 12
print(course[:4]) # returns Data
print(course[4:]) #returns Analysis
print(course[-3:]) #returns sis

print(course[::1])#returns all characters
print(course[::2]) #includes start to end skipping 1 character
print(course[1:6:3]) #aA
print(course[2::3])#tnys
print(course[2:13:3]) #tnys
print(course[::-1]) #returns string in reverse
print(course[::-2]) # returns sslna

#Task:Workout with all possibilities of slicing and striding on a example

name="codegnan"
#name[3]='w' #returns type error bcz strings are immutable

#Operations on strings -->Indexing,Conacatenation,Repetition
print(name * 3)
print('*' *25) #Repetition

#Concatenation --> Combining strings

data='saketh'+'python'+''+'database'
print(data)     
print('123' * 4) #Numerical string
print('code' in 'codegnan')

for i in 'codegnan':
    print(i,':')
#In above case we get every character line by linefor i in 'codegnan'

for i in 'codegnan':
    print(i,end='')

name="datACodegnan"
#Built-in functions -->len(),min(),max(),sorted()
print(len(name))
print(min(name)) #Alphabetical order ASCII ordering
print(ord('A')) #returns ASCII value
print(ord('T'))
print(chr(97))
print(chr(98))
print(max(name))
print(sorted(name)) #returns a list by sorting all elements
'''
#Methods on strings --> Case-Conversions,Finding/Searching...
name='Codegnan Data'
#Case-conversions --> upper(),lower,title(),capitalize()
print(name.upper()) #converts total string into upper case letters
#or
a=name.upper()
print(a)
b=name.lower()
print(b)

#Capitalize()--> converts first letter to uppercase
c=name.capitalize()
print(c)
#Title()--> converts every word first letter into upper case
d=name.title()
print(d)

#Task:A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Use loops and strings to return A-Z

