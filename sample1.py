import  sys
import math

print (sys.version)

print (sys.version_info)

print("Hello World")
# simple if example and intendation example
if(5>2):
    print("Five is Greater than 2")
else:
    print("Five is less than 2")
"""
This is multiple line comment Example
"""
x= "My Name "
y = "is "
z="Javeed"
print(x,y,z)
print(x+y+z)


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)