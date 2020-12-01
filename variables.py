x = 5
y = "John"
print(x)
print(y)

# Casting
x = str(3)
y = int(3)
z = float(3)

# Camel Case
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# Snake Case
my_variable_name = "John"

# Many values to Multiple Variables
x, y, z = "orange", "banana", "cherry"
print(x, y, z)


# One value to multiple variables
x = y = z = "Orange"
print(x, y, z)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)


# Output varables
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)


# Global Variable
x = "awesome"


def myfunc():
    print("Python is "+x)


myfunc()

x = "awesome"


def myfunc1():
    x = "fantastic"
    print("Python is " + x)


myfunc1()
print("Python is "+x)

# The global keyword


def myfunc2():
    global x
    x = "fantastic"


myfunc2()
print("Python is " + x)
