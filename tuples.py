mytuple = ("apple", "banana", "cherry")
thistuple = mytuple
print(thistuple)

# Tuple Items
# Ordered
# Unchangeable
# Allow Duplicates
# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple with One item
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple with strings, integers, boolean
tuple1 = ("abc", 34, True, 40, "male")


# The tuple() Constructor
# note the double round-bracket
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Access Tuple Items
print(thistuple[1])

# Check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Tuples are unchangeable, or immutable
thistuple = ("appple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green, yellow, red)

# Using Asterix*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Join Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
