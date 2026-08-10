"""
strings -->CaseConversion,Searching & Finding,String testing methods,
Replace space removal

#Searching,Finding,Replacing,Joining...
a="Codegnan"

print(len(a))
print(min(a))
print(max(a))

b=a.index('d') #it returns the index position
print(b)
c=a.index('n') #it returns only the first occurance
print(c)
d=a.index('n',6) #it returns the next occurance
print(d) 
#e=a.index('n',8) #valueError
#print(e)
#f=a.index('t') #ValueError
#print(f)
#g=a.index('n',1,4)#ValueError
#print(g)
h=a.index('n',1,7)
print(h)

#rindex()--> returns last occurance
b=a.rindex('g')
print(b)
c=a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d=a.rindex('n',8) #it returns ValueError
#print(d)

#Count() -->returns the number of items object is repeating

print('Codegnan'.count('n'))
print('Code'.count('w')) #it returns 0 as we don't have 'w' in 'Code'
print('Cakshjasaksajs'.count('a'))

#Find() --> gives first occurance but avoid error and returns -1 if substring is
#not found
print('codegnan'.find('r'))
print('codegnan'.find('n'))
print('codegnan'.rfind('n'))

a="DataAnalysis"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))

#Replacing,Splitting,Joining
#Strings are immutable
a='Codegnan'
#a[4]='s'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
print('khusju#jdfh#djfbj'.replace('#',' '))
print('fhusju#jdfh#djfbj'.replace('#',','))
print(a.replace('x','Akshaya')) #prints codesnan
print('jshsud@fjho#fjh@fs'.replace('#',' ^ '))

a='Akshaya is a good girl'
b=a.split()
print(b)
print(len(b))
c='Askhaya,is,a,good,girl'
d=c.split()
print(d)
e=c.split(',')
print(e)


#join()

a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('Akshaya'))
print(' '.join('Akshaya'))

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),isupper(),isslower()...

a='Akshaya23'
print(a.isalnum())
b='akshaya'
print(b.isalnum())
print(b.isalpha()) #Returns true only for the alphabets
print(b.isdigit())
print('3378365428'.isdigit())
print('2345'.isnumeric())
print('akshaya'.startswith('a'))
print('akshaya'.startswith('a',4))
print('codegnan'.endswith('f'))

print('codegnan'.islower()) #True --> returns true for all lowercase
print('codegnan'.isupper()) #False -->returns true for all uppercases
print('codegnan python'.istitle())#False


#Space removal--> strip() (removes leading and trailing spaces)

a='codegnan'
print(a.strip())
b=input("Enter the string:").strip().lower()
print(b)
"""
#Zfill() filling with zeroes as per the given numeric string
print('124'.zfill(4))
print('124'.zfill(7))
#Center(),ljust(),rjust() --> Alignment of strings (check length and then
#modify the width accordingly)
print('hai'.center(6))
print('hai'.center(6,'#'))
print('hai'.center(4))
print('hai'.center(5))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))


