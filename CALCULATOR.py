# TO OPERATE ON TWO NUMBERS

a= int(input("enter the first number"))
b= int(input("enter the second number"))

# ADDITION
def add(a,b):
    s=a+b
    print("the sum of two number is : ",s)
# SUBSTRACTION
def minus(a,b):
    s=a-b
    print("the substraction of two number is : ", s)
# MULTIPLICATION
def multiply(a,b):
    s=a*b
    print("the product of two number is : ", s)
# DIVISION
def division(a,b):
    s=a-b
    print("the product of two number is : ", s)
# interaction loop
while True:
    print("""hi!
              addition = 1
              substraction = 2
              multiplication = 3
              division = 4 
              finish = 5
              reassign = 6 """)
    x=int(input("enter the operation's corresponding value"))
# input cases
    if x == 1:
        add(a,b)
    elif x == 2:
        minus(a, b)
    elif x == 3:
        multiply(a, b)
    elif x == 4:
        division(a,b)
    elif x == 5:
        break
    # reassigning the two values
    elif x == 6:
        a = int(input("enter the first number"))
        b = int(input("enter the second number"))
    else :
        print(" invalid input !")
