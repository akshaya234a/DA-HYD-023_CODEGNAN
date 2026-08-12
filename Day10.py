'''
Sequences --> Strings,Lists,Tuples,Sets
Mapping --> Dictionary

#Lists --> Collection of heterogenous(it can be same kind or diffirent) elements
#List --> Indexed,Ordered,Mutable,Heterogenous,we use [] to store data

marks =[35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)

#Operations : Indexing,sliscing,striding,Membership,Merging,Repetition
#Nested list--> A list inside another list

names=['codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4]) #it returns code
print(names[0][4:]) #it returns gnan

print(names[0][0:8:2]) #returns cdga
names[0]=names[0][::-1]
print(names)
names[3]=names[3][::-1]
print(names)
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,Slicing -->Mutable
names[2] ='python'
print(names)
#By indexing if we change the elements,length of collection will remain same
names[4]=['codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[3][1:3])
print(names[4][1:4])
print(names[4][0])
print(names[4][0][4:])
names[2:4]='Akshaya','Pavan','Ranjith','Kid'
print(names)
print(len(names))
#In slicing whatever u pass as per the logic length keeps on increasing

#o/p as follows:
#['Codegnan',25,'Akshaya','Python','Ranjith','Java','DA23',34]
names[3:6:2]='python','Java'
print(names)

#Create a nested list and work on indexing,striding,slicing
#added advantage if u could add string functions also to it
#Lists Functions --> append(),insert(),extend(),pop(),remove(),clear()
#index(),count(),copy(),sort(),reverse()

names=['codegnan','Akshaya']
#append()--> inserts single element to the end of the list
names.append('data')
print(names)
#names.append('analysis','data') #TypeError
names.append(['analysis','agents'],)
print(names)
#append() will always increment the length of list by 1
print(names[3])
names[3].append('Chatgpt')
print(names)
print(names[3].append('chatgpt')) #It returns None as append is applicable on list
#not on print
print(names[3])

#extend()--> inserts multiple elements to the end of list

names.extend('analysis')#String willbe splitted
print(names)
names.extend(['analysis'])#Kalpadaniki 
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(20,34) #TypeError -->Extend takes only one argument
#print(names)

#Insert(index,object)-->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b']) #Syntax Error
#print(names)
names.insert(-1,'AAA')
print(names)

#Pop(),remove(),clear()
#pop() by default last,else given index
names.pop()
print(names)
names.pop(2)
print(names)

#remove() we can remove a specific value 
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
#names.remove(14) #ValueError
#print(names)
del names[1:3] #del keyword will apply permanent changes
print(names)
names.clear() #clear removes all elements and returns empty list
print(names)
'''
#Task
#Data = ['codegnan','saketh','python','java'] #input
#output as follows

0:codegnan
1:saketh
2:python
3:java


Data = ['codegnan', 'saketh', 'python', 'java']
for i in range(len(Data)):
    print(i, ":", Data[i])

#OR

Data = ['codegnan', 'saketh', 'python', 'java']
for i in range(len(Data)):
    print(str(i) + ":" + Data[i])








