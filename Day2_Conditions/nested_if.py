# Day 2: Nested If Example

# Check if a student passed and grade them
marks = int(input("Enter your marks: "))

if marks >= 33:
    print("You Passed!")
    
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 75:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("You Failed. Better luck next time!")
