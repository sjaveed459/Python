
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

def Choose():
    x= int (input("Enter 1 for sample if and elif example. or enter 2 for example with or"))
    if x == 1:
        Sample()
    elif x == 2:
        withOr()

Choose()




