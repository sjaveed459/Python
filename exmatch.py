#example of Match

x =  input("Enter Grade from A to F:")
match x:
    case "A" | "a" :
        print("Distinction")
    case "B" | "b" :
        print("First Class")
    case "C" | "c" :
        print("Second Class")
    case "D" | "d" :
        print("Third Class")
    case "F" | "f" :
        print("Fail")
    case _:
        print("No Grade")