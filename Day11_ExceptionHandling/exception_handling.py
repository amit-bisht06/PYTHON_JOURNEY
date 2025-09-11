# Basic try-except
try: 
    num= int(input("Enter a number: "))
    print("You Entered: ", num)
except ValueError:
    print("Invalid Input! Please enter a number")

    