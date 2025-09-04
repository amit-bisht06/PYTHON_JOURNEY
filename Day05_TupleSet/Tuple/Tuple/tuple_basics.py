"""
A tuple is a collection which is ORDERED and UNCHANGEABLE. Allows duplicate members.
Tuples are written with round brackets () .
"""
 
# Creating a TUPLE
thisTuple = ("apple", "banana", "cherry")
print("Fruits Tuple: ", thisTuple)

# Accessing elements
print("Frist fruit: ", thisTuple[0])
print("Last fruit: ", thisTuple[-1])

#Tuple is immutable so we can't change its item
#fruits[1] = "Grapes"   # ❌ This will give an error  

# Iterating through tuple
for fruit in thisTuple:
    print("Fruits: ", fruit)


#Tuples allow duplicate values:
thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thisTuple)

# Range of Indexes
print("thistuple[2:5]: ", thisTuple[1:4])
print("thistuple[:6]: ", thisTuple[:3])