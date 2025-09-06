# String Methods

text = "    hello python world!   "

# String Length
print("Length of String: ", len(text))
# Upper Case
print(text.upper())

# Lower Case
print(text.lower())

# Remove Whitespace
print(text.strip())

# Replace String
print(text.replace("h", "J"))
print(text)

# Count a Spcific char
print("Occurence of h: ",text.count('h') )

# Find Method
print(text.find("python"))