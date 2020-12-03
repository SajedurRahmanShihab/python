fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping through a String
for x in "banana":
    print(x)

# The break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
