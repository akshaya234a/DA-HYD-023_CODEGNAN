#Sum of prices of products using for loop
'''
price=list(map(int,input("Enter prices:").split(',')))
result=0
for i in price:
    result = result +i
print(result)

#program to count uppercase,lowercase,digits,special
password=input("Enter password:")
upper_count=0
lower_count=0
digits=0
special=0
for char in password:
    if char.isupper():
        upper_count +=1
    if char.islower():
        lower_count +=1
    if char.isdigit():
        digits +=1
    if not char.isalnum():
        special +=1
print(f'upper_count are {upper_count}')
print(f'lower-count are {lower_count}')
print(f'digits are {digits}')
print(f'special characters are {special}')

#or
password=input("Enter password:")
upper=lower=digit=special=0
for ch in password:
    if 'A' <= ch <='Z':
        upper+=1
    elif 'a' <= ch <='z':
        lower+=1
    elif '0' <= ch <='9':
        digit+=1
    else:
        special += 1
print("uppercases are:",upper)
print("lowercases are:",lower)
print("Digits are:",digit)
print("special chars are:",special)

#Returns domain from the email
email=input("Enter email:")
domain=email.split('@')[1]
print(domain)
#or
email=input("Enter email").split()
for mail in email:
    print(mail.split("@")[1])
'''
#Movies should be return with index
movie=input("Enter movie names:")
position=movie.index(movie)
print(position)











