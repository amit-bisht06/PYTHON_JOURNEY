# Dictionaries are used to store data values in { key:value } pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Creaeting a Dictionary
student = {
    "name": "Amit",
    "age": 21,
    "course": "Btech"
}
print("Student Dictionary: ", student)

# Accessing values
print('student["name"]: ', student["name"])
print('student["age"]: ', student.get("age"))

# Updating Values
student["age"] = 23
print("Updated Age: ", student["age"])

# Adding new Key-value pair
student["hobby"] = "Reading, Yoga, Content Creation"
print("After adding hobby: ", student)