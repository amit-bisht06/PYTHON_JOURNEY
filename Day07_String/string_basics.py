# String is the collection Words....
# STRINGS in python are surrounded by either single quotation marks, or double quotation marks. e.g.('hello' is the same as "hello".)

# Creating a String
name = "Amit Bisht"
print("Name: ", name)

# Indexing 
print("First Character: ", name[0])
print("Last Character: ", name[-1])

# Slicing
print("First 4 letters: ", name[:4])
print("Last 4 characters: ", name[-4:])

#Looping through a String
for c in name:
    print(c, end="")

# String Length
print(len(name))

# Check String 
print("Bisht" in name)
if("it" in name):
    print("Yes, 'it' is Present.")

# String Concatenation -> Adding two String together by operator "+"
a = "Hello"
b = "World"
c = a +" "+ b
print(c)