#Swap of two numbers using temporary variable
print("Choose 1 for with temp swapping 2 for without temp swapping, 3 using python annotation")
choose = int(input("Choose:"))
if choose == 1:
    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))
    # taking temporary variable here
    print("value of a is:", a)
    print("value of b is:", b)
    temp = a
    a = b
    b = temp
    print("value of a is:", a)
    print("value of b is:", b)
    #Swap of two numbers without using temp variable
elif choose == 2:
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    print("value of a is:", a)
    print("value of b is:", b)
    a = a+b
    b=a-b
    a = a-b
    print("value of a is:", a)
    print("value of b is:", b)
elif choose == 3:
    a=int(input("Enter a value:"))
    b=int(input("Enter b value:"))
    a, b = b, a
    print("value of a is:", a)
    print("value of b is:", b)




