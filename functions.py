# Python function
# Creating a Function

def my_function():
    print("Hello from a function")


my_function()


# Arguments
def my_function1(fname):
    print(fname + " Rahman")


my_function1("Sajedur")


# Number of Arguments
def my_function2(fname, lname):
    print(fname + " " + lname)


my_function2("Sajedur", "Rahman")


# Arbitrary Arguments, *args
# This way the function will receive a tuple of arguments, and can access the items accordingly
def my_function3(*kids):
    print("The youngest child is " + kids[2])


my_function3("Galib", "Raiyan", "Khadija")


# Keyword Arguments
# send arguments with the key = value syntax
# This way the order of the arguments does not matter.
def my_function4(child3, child2, child1):
    print("The youngest child is " + child3)


my_function4(child1="Alif", child2="Galib", child3="Raiyan")


# Arbitrary Keyword Arguments, **kwargs
# If we do not know how many keyword arguments that will be passed into our function
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def my_function5(**kid):
    print("His last name is " + kid["lname"])


my_function5(fname="Sajedur", lname="Rahman")


# Default Parameter Value
def my_function6(country="Norway"):
    print("I am from " + country)


my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")

# Passing a List as an Argument


def my_function7(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function7(fruits)

# Return Values


def my_function8(x):
    return 5 * x


print(my_function8(3))
print(my_function8(5))
print(my_function8(9))
