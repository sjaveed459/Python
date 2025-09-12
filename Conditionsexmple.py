
def Sample():
    firstint = input("Enter a number:")
    secondint = input("Enter another number:")
    if firstint > secondint:
        print("First number is greater than second number")
    elif firstint < secondint:
        print("Second number is greater than first number")
    else:
        print("first and second numbers are equal")

def withOr():
    firstint = input("Enter a number:")
    secondint = input("Enter another number:")
    if firstint > secondint or firstint > secondint:
        print("First number is not equal to second number")
    else:
        print("First number is equal to Second number")

def withOrr():
    firstint = input("Enter a number:")
    secondint = input("Enter another number:")
    if firstint == secondint:
        print("First number is equal to Second number")
    else:
        print("Second number is equal to First number")
def withnotor():
    x= int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    if x!=y:
        print("The numbers are not equal")
    else:
        print("The numbers are equal")
def withand():
    x = int (input("Enter Marks:"))
    if x >=90 and x<=100:
        print("Grade: A")
    else :
        print("No Grade")
def Choose():
    x= int (input("Enter 1 for sample if and elif example. or enter 2 for example with or"))
    if x == 1:
        Sample()
    elif x == 2:
        withOr()
    elif x == 3:
        withOrr()
    elif x == 4:
        withnotor()

Choose()




