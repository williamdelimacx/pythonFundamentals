# Declaration
my_list = [1, 2, 3, 4, 5, "John Doe", True, False]
print("My list:", my_list)

# Accessing elements
print("First element:", my_list[0])  # Output: 1
print("Last element:", my_list[-1])  # Output: False

# Slicing the list
print("Sliced list (elements 2 to 4):", my_list[2:5])  # Output: ['Inserted Element', 20, 4]
print("Sliced list (first 3 elements):", my_list[:3])
print("Sliced list (last 3 elements):", my_list[-3:])

# Modifying elements
my_list[1] = 20
print("Modified list:", my_list)

# Methods for lists

# Adding elements
my_list.append("New Element")
print("List after appending:", my_list)

my_list.insert(2, "Inserted Element")
print("List after inserting:", my_list)

# Removing elements
my_list.remove(3)
print("List after removing 3:", my_list)

popped_element = my_list.pop(0)
print("Popped element:", popped_element) 
print("List after popping:", my_list)

# Indexing and counting
print("Index of 'John Doe':", my_list.index("John Doe"))

print("Count of True in the list:", my_list.count(True))

# Sorting the list (only works with comparable types)
numeric_list = [5, 2, 9, 1, 5, 6]
numeric_list.sort()
print("Sorted numeric list:", numeric_list)

# Length of the list
print("Length of the list:", len(my_list))

