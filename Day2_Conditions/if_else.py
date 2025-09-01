# Day 2: If-Else Conditions

# Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")

# Check if the person is eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
