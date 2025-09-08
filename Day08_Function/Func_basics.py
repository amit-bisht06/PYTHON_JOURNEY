# A function is a block of code which only runs when it is called.
#--------------------------------------------------------------------------------------

# CREATING A FUNCTION
# In Python a function is defined using the def keyword:
def my_function():
    print("I am inside a function.")

print("Before Function Caliing.")
my_function()   # functionCalling
print("After Fucntion Calling.")
print()
#---------------------------------------------------------------

# Function with Arguments
# Information can be passed into functions as arguments.

def arg_func(fname):    # fname will be called as Argument
    print("User name is "+fname)

name = input("Enter your name: ")
arg_func(name) # name will be called as 'parameter'
print()
#-----------------------------------------------------------------

# DEFAULT ARGUMENT
def greet(name="Guest"):
    print("Welcome "+ name)

greet("Amit")
greet()
print()
#-----------------------------------------------------------------

#Keyword Argument
def printItem(id, name, price):
    print(f"Id no is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")

printItem(101, "abc", 100)
print()
printItem(id=102, name="xyz", price=200)
print()
printItem(name="abc", id=101, price=500)
#------------------------------------------------------------------

# Returning Multiple Values in Python
def multiValue(num1, num2):
    sum = num1+num2
    mul = num1* num2
    return sum, mul

s, m = multiValue(7, 8)
print()
print("Return Multiple Values")
print("Sum= "+s, " Mul= ", m)