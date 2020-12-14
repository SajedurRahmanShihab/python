# Parse JSON - Convert from JSON to Python
import json
# some JSON:
x = '{"name" : "John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
# the result is a python distionary:
print(y["age"])

# Convert from Python to JSON
# a python object (dict)
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON
y = json.dumps(x)
# the result is a JSON string:
print(y)

# Convert a Python object containing all the legal data types:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))
