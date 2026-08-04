#For with else
'''
work_log=[0,1,1,1,0,1,0]
#result varigable -->longest_streak
longest_streak=0 #Target variable
current_streak=0
for day in work_log:
    if day == 1:
        current_streak=current_streak+1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(f'longest_streak is {longest_streak}')
            break #terminates execution
    else:
        current_streak =0 #Streak breaks if day is zero
else:
    print(f'longest_streak is {longest_streak}')
print("Execution done")    
#in this case when entire loop execution is done we get result of
#else block    


#For-else with Notifications scenario

notifications=[0,1,1,1]
for notification in notifications:
    if notification == 1:
        print("Unread Notification")
        break
else:
    print("All Caught Up")

#Try to take notifications from user --> list of integers 
notifications=list(map(int,input("Enter values -->0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
        print("Unread Notification")
        break
else:
    print("All Caught Up")

#While --> it relies on condition.it'll be completely executed until the condition is satisfied

syntax while

while <condition>:
       statement(s)...
       ....
       ....
       

while True:
    print("Yes")
    
#it runs an infinite loop.we need to press control+c(keyboard interrupt) to stop the loop

i=1 #Initialised statement
while i<=10:
    i=i+1
    print(i)
 #counter -->Updating value

i=10
while i>=1:
    print(i)
    i=i-1  #decrement i-=1


i=0
while i<=10:
    print(10-i)
    i=i+1

#Banking scenario --> PIN authentication if more than 3 attempts
#Account locked

pin='1234'
max_attempts = 3
current_attempt=0
while current_attempt < max_attempts:
    entered_pin=input("Enter PIN:")
    if entered_pin == pin:
        print("Login Successful!")
    else:
        print("Entered PIN is wrong..Try again carefully")
        current_attempt=current_attempt+1
    if current_attempt>=3:
        print("account locked")
'''       
#or
pin='1234'
max_attempts = 3
current_attempt=0
while current_attempt < max_attempts:
    entered_pin=input("Enter PIN:")
    if entered_pin == pin:
        print("Login Successful!")
        break
        #continue #It holds for this condition and skips to the next part of condition
    else:
        print("Entered PIN is wrong..Try again carefully")
        current_attempt=current_attempt+1
else:
    print("account locked")

















