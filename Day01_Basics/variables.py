#VARIABLES are containers for storing data values.
#------------------------------------------------------------

# 1, Basic Variables declaration
name = "Amit Bisht"  
age = 21
height = 5.8

print("Name:", name)
print("Age:",  age)
print("Height:",  height)


# 2. Multiple Variable in One Line
x,y,z = 10, 20, "Apple"
print("\n", x, y, z)


# 3. Same Value to Multiple Variable
a=b=c=100
print("\n",a,b,c)


# 4. f-strings
print(f"\nMy name is {name} and I am {23} years old.")


# 5. Swapping Variables
x=5
y=8
x,y=y,x
print("x: ",x, " y: ", y)


# 6. Dyanamic Typing
var = 10
print(var, type(var))
var = "Hello"
print(var, type(var))