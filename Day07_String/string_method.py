# String Methods

text = "    hello python world!   "

# Length() --> return Length of a string
print("Length of String: ", len(text))

# Upper Case --> Converts a string into upper case
print(text.upper())

# Lower Case --> Converts a string into lower case
print(text.lower())

# Strip() --> Returns a trimmed version of the string(Remove extra whitespaces)
print(text.strip())

# Replace() --> Returns a string where a specified value is replaced with a specified value.
print(text.replace("h", "J"))
print(text)

# Count() method --> Returns the number of times a specified value occurs in a string.
print("Occurence of h: ",text.count('h') )

# Find Method --> Searches the string for a specified value and returns the position of where it was found
print(text.find("python"))