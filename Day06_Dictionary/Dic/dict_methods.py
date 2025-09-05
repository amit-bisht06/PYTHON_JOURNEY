#Dictionary Methods

student = {
    "name": "Amit",
    "age": 21,
    "course": "CSE"
}

# Keys
print("Keys:", student.keys())

# Values
print("Values: ", student.values)

# Items
print("Items: ", student.items())

# Pop
student.pop("age")
print("After pop: ", student)

# Update
student.update({"course":"ML/Python"})
print("After Update: ", student)