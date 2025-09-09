# Lambda Functions in Python
#A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.
#-------------------------------------------------------------------------------------------------------

# Normal function
def square(x):
    return x*x
print("Square using function is: ",square(5))
print()
#------------------------------------------------------------------------------

# Same using lambda
square_lambda = lambda x: x*x
print("Square using lambda: ", square_lambda(3))
print()
#------------------------------------------------------------------------------

# Lambda with two arguments
add = lambda x,y : x+y 
print("Sum using lambda: ", add(3,4))
print()
#------------------------------------------------------------------------------

# Lambda with Condition
max_num = lambda x,y: x if x>y else y
print("Maximum number: ", max_num(6,8))
print()
#------------------------------------------------------------------------------

# Using map with lambda ->> map(function, iterable)
nums = [1, 2, 3, 4, 5]
square_list = list(map(lambda x : x**2, nums))
print("Square of list: ", square_list)
print()
#------------------------------------------------------------------------------

# Using filter with lambda --> filter (function, iterable)
even_num = list(filter(lambda x : x%2==0, nums))
print("Even Number List: ", even_num)
print()
#-------------------------------------------------------------------------------

# Using Lambda with sorted
students = [("Amit",21), ("Chirag", 20), ("Rahul", 22)]
students_sorted = sorted(students, key =lambda x: x[1])
print("Students sorted by age: ", students_sorted)