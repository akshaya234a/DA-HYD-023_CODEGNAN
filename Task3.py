#TEXT CASE COVERTER
'''
message=input("enter a text:")
cases=['upper','lower','title','capitalize','swapcase']
for case in cases:
    if case == 'upper':
        print('Upper:',message.upper())
    elif case == 'lower':
        print('lower:',message.lower())
    elif case == 'title':
        print('title:',message.title())
    elif case == 'capitalize':
        print('capitalize:',message.capitalize())
    elif case == 'swapcase':
        print('swapcase:',message.swapcase())
      
#USERNAME VALIDATOR
while True:
    username = input("Enter username: ")

    if username == "quit":
        break
    if username.isalnum():
        print("Contains only letters and numbers")
    else:
        print("Does not contain only letters and numbers")
    if username[0].isalpha():
        print("Begins with a letter")
    else:
        print("Does not begin with a letter")
    if username.isidentifier():
        print("Valid Python identifier")
    else:
        print("Not a valid Python identifier")

    if username.isascii():
        print("Contains only ASCII characters")
    else:
        print("Contains non-ASCII characters")

    print()

#FORMATTED STUDENT REPORT
students = []

for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students.append([name, marks, grade])
print("=" * 40)
print("STUDENT REPORT".center(40))
print("=" * 40)
print("Name".ljust(15) + "Marks".rjust(10) + "Grade".rjust(15))
for student in students:
    print(student[0].ljust(15) +
          str(student[1]).rjust(10) +
          student[2].rjust(15))
'''
#Character and Text Analyser
text = input("Enter a line: ")

letters = 0
digits = 0
spaces = 0
printable = 0
non_printable = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    if ch.isdigit():
        digits += 1
    if ch.isspace():
        spaces += 1
    if ch.isprintable():
        printable += 1
    else:
        non_printable += 1
print("Letters        :", letters)
print("Digits         :", digits)
print("Spaces         :", spaces)
print("Printable      :", printable)
print("Non-printable  :", non_printable)
print("Lowercase      :", text.islower())
print("Uppercase      :", text.isupper())
print("Title case     :", text.istitle())












