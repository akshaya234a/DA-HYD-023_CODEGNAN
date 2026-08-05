#Task
#Observe +ve+ve,-ve-ve, & +ve-ve all possibilities
'''
#Slicing
name="Hyderabad"
print(name)
#+ve+ve
print(name[:])
print(name[:9])
print(name[0:6])
print(name[6:9])
print(name[2:6])
print(name[3:8])
#+ve-ve
print(name[2:-2])
print(name[:-4])
print(name[4:-4])
#-ve-ve
print(name[-9:-1])
print(name[-9:])
print(name[-6:])
print(name[-8:-4])


#Striding
month='October'
print(month)
print(month[1:4:1])
print(month[2:7:2])
print(month[:7:3])
print(month[4::2])
print(month[::-1])
print(month[::-3])

#Task:A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Use loops and strings to return A-Z

for i in range(65,91):
    print(chr(i),end='')
 #or
'''
text="abcdefghijklmnopqrstuvwxyz"
for i in text:
    print(i.upper(),end='')












