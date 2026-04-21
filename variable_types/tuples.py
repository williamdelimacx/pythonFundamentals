# Create a tuple
my_tuple = (1, 2, 3, "Hello", True)
print("Created tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])  # Output: 1
print("Last element:", my_tuple[-1])  # Output: True

# Slicing the tuple
print("Sliced tuple (elements 2 to 4):", my_tuple[2:5])  # Output: (3, 'Hello', True)
print("Sliced tuple (first 3 elements):", my_tuple[:3])  # Output: (1, 2, 3)
print("Sliced tuple (last 3 elements):", my_tuple[-3:])  # Output: (3, 'Hello', True)

# Tuples are immutable, so we cannot modify them directly
# However, we can create a new tuple by concatenating existing tuples
new_tuple = my_tuple + (4, 5)
print("New tuple after concatenation:", new_tuple)

# Methods for tuples
# Count occurrences of an element
print("Count of 'Hello' in the tuple:", my_tuple.count("Hello"))  # Output: 1
print("Index of 'Hello' in the tuple:", my_tuple.index("Hello"))  # Output: 3

# Length of the tuple
print("Length of the tuple:", len(my_tuple))  # Output: 5

# Unpacking a tuple
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)  # Output: 1 2 3 Hello True

