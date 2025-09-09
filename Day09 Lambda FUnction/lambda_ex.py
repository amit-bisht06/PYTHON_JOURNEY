# Lambda Functions in Python

# Normal function
def square(x):
    return x*x
print("Square using function is: ",square(5))

# Same using lambda
square_lambda = lambda x: x*x
print("Square using lambda: ", square_lambda(3))

# Lambda with two arguments
add = lambda x,y : x+y 
print("Sum using lambda: ", add(3,4))

# Lambda with Condition
max_num = lambda x,y: x if x>y else y
print("Maximum number: ", max_num(6,8))