# Created a dictionary to store information about a person
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values in the dictionary print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

# Adding a new key-value pair to the dictionary
person["occupation"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}

# Updating an existing value in the dictionary
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}

# Removing a key-value pair from the dictionary
del person["city"]
print(person)  # Output: {'name': 'Alice', 'age': 31, 'occupation': 'Engineer'}

# Methods to work with dictionaries
# Get all keys in the dictionary
keys = person.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'occupation'])

# Get all values in the dictionary
values = person.values()
print(values)  # Output: dict_values(['Alice', 31, 'Engineer'])

# Get all key-value pairs in the dictionary
items = person.items()
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 31), ('occupation', 'Engineer')])