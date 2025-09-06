def main ():
    global name
    name = input("Enter your name:")
    hello(name)

def hello(to = "World"):
    print("Hello", to)

main()
hello()

def Greet():
    print("This is a greeting message to the user")
    print("Hello",name,"How are you?",name)

Greet()