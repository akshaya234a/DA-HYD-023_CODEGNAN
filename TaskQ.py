#Task Questions 2nd august
'''
#Grade Checker
marks = int(input("Enter marks:"))
if marks > 100 or marks <0:
    print("Invalid marks entered")
elif marks >=90:
    print("Grade:A")
    print("Remarks:Outstanding!")
elif marks >=80 and marks <89:
    print("Grade:B")
    print("Remarks:Excellent!")
elif marks >=70 and marks <79:
    print("Grade:C")
    print("Remarks:Good")
elif marks >=60 and marks < 69:
    print("Grade:D")
    print("Remarks:Fair,needs improvement")
elif marks >=50 and marks < 59:
    print("Grade:E")
    print("Remarks:Poor,needs serious improvement")
else:
    print("Fail,needs to reappear")


#Even odd checker(with twist)
num=int(input("Enter a number:"))
if num % 2 == 0 and num < 0:
    print("Negative Even Number")
elif num % 2 != 0 and num < 0:
    print("Negative Odd Number")
elif num % 2 == 0 and num > 0:
    print("Positive Even Number")
elif num % 2 !=0 and num > 0:
    print("Positive Odd Number")
else:
    print("Zero is neither even or odd")

'''
#Season Identifier
month=int(input("Enter month number:"))
if month >12 or month < 1:
    print("Invalid month entered")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
elif month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
else:
    print("Autumn")














