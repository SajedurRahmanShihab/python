thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)
print(thisdict["brand"])

# Unordered
# Changeable
# Duplicates Not Allowed

print(len(thisdict))
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# Access Dictionaries items
# Accessing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
x = thisdict["model"]
print(x)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# Get Keys
x = car.keys()
print("before the changes")
print(x)
car["color"] = "white"
print("after the changes")
print(x)

# Get values
x = car.values()
print("values")
print(x)


# Get Items
x = car.items()
print(x)

# Check if key Exists
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# Update Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# Removing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# clear()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop Dictionaries
# Loop through a dictionay
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])

# values()
for x in thisdict.values():
    print(x)

# keys()
for x in thisdict.keys():
    print(x)

# Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
    print(x, y)


# Copy Dictionaries
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict()
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": "2004"
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

# Or, add three dictionaries into a new dictionary
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
