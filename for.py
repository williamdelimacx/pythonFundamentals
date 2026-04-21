# Example of usig for loop to iterate over a list of numbers
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Example of using for loop to iterate over a tuple
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# Example of using for loop to iterate over a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Example of using for loop with range() function
for i in range(5):
    print(i)

# Example of using for loop with len() function
for i in range(len(numbers)):
    print(numbers[i])

# Example of using for loop with enumerate() function
for index, num in enumerate(numbers):
    print(f"Index: {index}, Number: {num}")