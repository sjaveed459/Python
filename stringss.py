#strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
b = 'Hello Javeed'
print(b)

print("Hello World!")

name = input("What is your name? ")
name = name.strip()
#only capitalize first letter of whole name
name = name.capitalize()

# capitalize all the words starting
name = name.title()

name = name.strip().title()

# we can include all these in sigle line code
enter_name = input("What is your name? ").strip().title()

print("Hello",enter_name)
