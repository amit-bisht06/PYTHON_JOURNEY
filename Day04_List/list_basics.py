# Basic List Operations

# Creating a List
fruits = ["apple", "banana", "mango"]
print("Fruits: ", fruits)

# Accessing elements --> To add an item to the end of the list, use the append() method:
print("First fruit: ", fruits[0])
print("Second fruit: ", fruits[-1])

# Adding elements --> To add an item to the end of the list, use the append() method:
fruits.append("orange")
fruits.append("kiwi")
fruits.append("banana")
fruits.append("melon")
print("After append: ", fruits)

# Changing elements
fruits[1] = "grapes"
print("After update: ", fruits)

# Iterating through list
for fruit in fruits:
    print("Fruit: ", fruit)

# Return the third, fourth, and fifth item:
print(fruits[2:5])
# By leaving out the start value, the range will start at the first item:
print(fruits[:4])