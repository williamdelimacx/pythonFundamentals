# Declaration of string variables
full_name = "John Doe"

full_name_quotation_marks = """John
Doe"""

full_name_single_quotation_marks = 'John Doe'

full_name_broke = "John \
  Doe"

name = "John"
surname = "Doe"

# Format
print("Full name (1° type):", full_name)
print("Full name (2° type):" + full_name)
print("Full name (3° type):" + "John" + "Doe")
print("Full name (4° type):" + "John", "Doe")
print("Full name (5° type):", full_name_quotation_marks)
print("Full name (6° type):", full_name_broke)
print("Full name (7° type): %s" % full_name)
print("Full name (8° type): %s %s" % (name, surname))
print(f"Full name (9° type): {name} {surname}")
print("Full name (10° type): {} {}".format(name, surname)) 

# Methods
print(name.upper()) # Converts all characters to uppercase
print(name.lower()) # Converts all characters to lowercase
print(name[0]) # Accessing the first character of the string (index starts at 0)
print(full_name.count("o")) # Counts the number of occurrences of the substring "o" in the full_name string
print(name.find("o")) # Finds the index of the first occurrence of the substring "o" in the name string.
print(name.encode()) #  Encodes the name string into bytes using the default encoding (usually UTF-8).
print(name.encode().decode()) # Decodes the previously encoded bytes back into a string using the default encoding (usually UTF-8).
print(full_name.replace("o", "a")) # Replaces all occurrences of the substring "o" with "a" in the full_name string and returns the modified string.
print("-".join(name)) # Joins the characters of the name string into a single string, with a hyphen ("-") between each character.
print(name.split("o")) # Splits the name string into a list of substrings using "o" as the delimiter. The resulting list will contain the parts of the name string that were separated by "o".

namex = "xJohn Doex" 
print(namex.strip("x")) # Removes the specified characters from both ends of the string
print(namex.lstrip("x")) # Removes the specified characters from the left end of the string
print(namex.rstrip("x")) # Removes the specified characters from the right end of the string

print(name.startswith("J")) # Checks if the string starts with the specified substring
print(name.endswith("n")) # Checks if the string ends with the specified substring

print("hn" in name) # Checks if the substring "hn" is present in the name string
print("hn" not in name) # Checks if the substring "hn" is not present in the name string