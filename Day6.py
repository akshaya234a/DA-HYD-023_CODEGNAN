'''
Control Statements --> Flow of execution of the program
                   -->Conditional statements --> if,elif,else..
                   -->Repetition statements(Loops) --> for,while(for with else)
                                                         (while with else)
                   -->Jumping Statements -->break,continue,pass
'''
#Loops --> Loops are helpful for repetition (Automative tasks)
#for keyword will hepful to iterate over a sequence / range
#Syntax for (for keyword):
'''
for <temp_var> in sequence?range:
    statement(s)...
    ....


#range(start,stop,step)
for i in range(10): #start
    print(i)
#In above case we got 10 iterations
for i in range(1,10):
    print("value of i is",i)
# (or)    print(f'value of i is -->{i}')


for i in range(1,10): #start,stop
    if i > 5 and i % 2 ==0:  #Even numbers and more than 5
        print(f'value of i is -->{i}')
        
#Range(start,stop,step)-->here step--> interval..
for i in range(1,10,4): #step means gap between the number
    print(i)
    print("Done")

for i in range(5,50,5):
    print(i)
print("These are divisible by 5")    

for i in range(1,10):
    print(i,end='')

for i in range(1,10,-1): #raises error
    print(i)  

for i in range(10,1,-1):
    print(i)

#print -10 to -1
for i in range(-10,0,1):
    print(i,end='')
    
#[]--> we generally Lists
Names = ['Akshaya','Pavan','Ranjith']
print(len(Names)) #len(object) --> returns the number of items in container
for i in Names:
    print(i)
    print(f'student Name is {i}')
#or
Names = ['Akshaya','Pavan','Ranjith']
print(len(Names)) #len(object) --> returns the number of items in container
for name in Names:
    #print(name)
    #print(f'student Name is {name}')
    if name == "Pavan":
        print(f'student name is {name}')

#Calculate the sum of first 10 numbers
#First understand your input --> range(11)-->10 numbers
#second understand your output --> sum(number)
#Third we need to to map the logic

result=0
for i in range(11):
    #print(i)
    #print(f'result is {i+1}')
    result=result + i #result +=i
    print(f'Now the result is {result}')
print(f'sum of 10 numbers is {result}')

result=0 #target variable
for i in range(21):
    if i % 2 ==0:
        result=result+i
        print(f'Now the result is {result}')
print(f'Sum of first even numbers are {result}')    
'''
#Understand the loops usage with fitness streak example
#work_out -->1,work_out_missed-->0
work_log=[0,1,1,1,0,1,0]
#result varigable -->longest_streak
longest_streak=0 #Target variable
current_streak=0
for day in work_log:
    if day == 1:
        current_streak=current_streak+1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak =0 #Streak breaks if day is zero
print(longest_streak)


