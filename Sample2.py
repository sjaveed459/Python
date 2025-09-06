x = float(input("enter a number:"))
y = float(input("enter another number:"))
z= round(x+y,2)
z1= x+y
print(f"Addition of two numbers is {z}")

# we can use another method for rounding as well, by using f-string

print(f"z value after addition is {z:.2f}")