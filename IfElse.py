a = 33
b = 200
if b > a:
    print("b is greater than a")

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is grater than b")

# Shorthand example
if a > b:
    print("a is greater")

# Shorthand If Else
a = 2
b = 330
print("A") if a > b else print("B")

# And
a = 220
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# OR
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
