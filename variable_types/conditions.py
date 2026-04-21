# Conditions
# A condition is a function that takes in a variable and returns a boolean value.
# Conditions are used to check if a variable meets certain criteria.

# Example of using conditions in an if statement
age = 18
if age < 18:
    print("You are a minor.")

if age > 18:
    print("You are an adult.")

if age == 19:
    print("You are an adult.")

if age >= 18:
    print("You are an adult.")

if age <= 18:
    print("You are an adult.")

if age != 10:
    print("You don't have the required age.")

# Example of using conditions in an elif statement
if age < 18:
    print("You are a minor.")
elif age >= 18:
    print("You are an adult.")

# Example of using conditions in an else statement
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

# Example of using conditions in a elif and else statement
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Example of using input to get user input and check conditions
user_age = int(input("Enter your age: "))
if user_age < 18:
    print("You are a minor.")
elif user_age >= 18 and user_age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
