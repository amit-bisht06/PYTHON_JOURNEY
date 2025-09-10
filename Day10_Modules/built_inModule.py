"""
* Using Python's built-in math MODULE
"""
import math
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("Pi value:", math.pi)
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print()
#---------------------------------------------------------------------------
"""
* random MODULE
"""
import random
print("random MODULE")
print("Enter number between 1-10: ", random.randint(1,10))
print("Enter float between 0-1: ", random.random())
print("Random choice: ", random.choice(["apple", "banana", "grapes", "mango"]))

num = [1,2,3,4,5,6]
random.shuffle(num)
print("math MODULE")
print(num)
print()
#----------------------------------------------------------
"""
* datetime MODULE
"""
import datetime

today = datetime.date.today()
print("datetime MODULE")
print("Today's Date: ",today)

now = datetime.datetime.now()
print("Current time: ", now)

yesterday= now - datetime.timedelta(days=1)
print("1 days ago: ", yesterday)

future = now + datetime.timedelta(days=10)
print("10 days later: ", future)