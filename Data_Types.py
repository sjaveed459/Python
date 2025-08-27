import random
print(random.randrange(1,100))
print(random.random())
print(random.randint(2,10))

x = 1    # int
y = 2.8  # float
z = 3+1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
# you can not convert complex number to any other format
#d = int(z)
#print(d)

print(type(a))
print(type(b))
print(type(c))