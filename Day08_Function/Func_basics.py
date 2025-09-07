# A function is a block of code which only runs when it is called.

# CREATING A FUNCTION
# In Python a function is defined using the def keyword:
def my_function():
    print("I am inside a function.")

print("Before Function Caliing.")
my_function()   # functionCalling
print("After Fucntion Calling.")

# Function with Arguments
# Information can be passed into functions as arguments.

def arg_func(fname):    # fname will be called as Argument
    print("User name is "+fname)

name = input("Enter your name: ")
arg_func(name) # name will be called as 'parameter'