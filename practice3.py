#For loop
#Write a python program to calculate  the innings of a batman,boundaries,
#dot balls and total score
'''
score=[4,6,1,0,4,0,6] #or list(map(int,input().split()))
dotball=0
boundaries=0
total_score=0
for i in score:
    total_score = total_score+i
    if i == 0:
        dotball=dotball+1
    elif i ==4 or i ==6 :
        boundaries=boundaries+1
print("The total_score is:",total_score)        
print("The dot balls are:",dotball)
print("The boundaries are:",boundaries)

#While loop

pin='1234'
max_attempt=5
current_attempt=0
while current_attempt < max_attempt:
    entered_pin=input("enter a pin:")
    if entered_pin == pin:
        print("Unlocked successfully")
        break
    else:
        print("Entered wrong pin")
        current_attempt=current_attempt+1
else:
    print("phone locked!")
'''
#write a python program for ATM lock 
pin='2331'
max_attempt=3
current_attempt=0
while current_attempt < max_attempt:
    entered_pin=input("enter a pin:")
    if entered_pin == pin:
        print("Login successful")
        break
    else:
        print("Entered wrong pin")
        current_attempt=current_attempt+1
else:
    print("Account locked!")      

#Movies should return with index
movies=input().split()
i=1
for movie in movies:
    print(i,".",movie,sep="")
    i=i+1
    
