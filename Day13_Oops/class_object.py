# OOP Basics: Class and Object

#Defining a class
class Student:
    # Class attribute
    college = "BTKIT Dwarahat"

    # Constructor (__init__ method)
    def __init__(self, name, age):
        self.name = name   #instance variable
        self.age= age

    # Method
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, College: {Student.college}")

# CREATING OBJECTS
s1 = Student("Amit", 22)
s2 = Student("Chirag", 23)

# ACCESSING METHODS
s1.show_info()
s2.show_info()

#Accesssing attributes directly
print(s1.name, s1.age)