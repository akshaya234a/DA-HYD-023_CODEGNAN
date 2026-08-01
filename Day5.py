#elif keyword --> if-elif-else
'''
if <condition>:
    statement
elif <condition>:
    statement(S)...
    ....
elif <condition>:
    statement(s)...
    .....
else:
    statement(s)..
    ...


marks=int(input("Enter student marks:"))
if marks >100:
    print("Invalid marks")
elif marks >= 90:
    print("A")
elif marks >=80 and marks <=89:
    print("B")
elif marks >=70 and marks <=79:
    print("C")
elif marks >=60 and marks <=69:
    print("D")
elif marks < 60 and marks >=0:
    print("Fail")
else:
    print("No negative values")

#Task --> Same usecase try with if-elif-else usage in other way

#Voter Eligibility checkcase -->make sure to satisfy all possible conditions
#>=18 --> Access
#<18 --> no of years eligibility should tell
#negative values --> not acceptable

age=int(input("enter your age:"))
if age >=18 and age <=100:
    print("your age is",age,"you have vote eligibility")
    print("ACcess granted")
elif age < 18 and age > 0:
    print("You still need to get vote eligibility")
    print("You need to wait for more",(18-age),"year(s)")
elif age < 0:
    print("Enter only positive values")
else:
    print("less than 100 acceptable")

    

#prefer if-elif-else...
 
#output -->print --> we can pass any values also use sep and end 
#output Formatting --> old style formatting(using commas)
#% usage(%f,%d),.format() usage,fstring notation
a,b=4,5
print(a)
print(b)
print(a,b)
name="codegnan";batch="DataAnalysis"
print(name,batch) #by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='--->')
#end='\n',\t -->tab space
print(name,batch,end='\t')
print(a,b,end=',')
print("Hyd")


name="codegnan";age=21;batch="DA-023";place="hyd" 
print(batch,"is in",name) #variable and msg to be separated by comma
print(name,"is in",place,'age is',age,'years')

#old style formatting -->%d -->integer,%s-->string,%f-->float
salary = 25354.324
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.f"%(salary))
print("His salary is %.1f"%(salary))#if rounding to 1 decimal
print("His salary is %.2f"%(salary)) 
'''
#.format() usage
name="codegnan";age=21;batch="DA-023";place="hyd"
print("{} is in {}".format(name,place)) #order matters and format stores the variables we given in {}

#string usage (more recommended)
print(f'{name} is in {place}')
print(f'{'akshaya'} is in {name}')




