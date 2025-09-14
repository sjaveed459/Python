#example of loops
import math

choose = int(input("Choose:"))
if choose == 1:
    #example of while loop
    i =3

    while i!=0:
        print("Meow")
        i =i-1
#example to add numbers of given number
elif choose == 2:
    n = int (input("Enter a number:"))
    sumofints =0
    while n!=0:
        x=n%10
        sumofints+=x
        n=n//10
        #n=math.floor(n/10)
        # or we can use this one also n=n//10
    print ("The sum of the numbers is",sumofints)