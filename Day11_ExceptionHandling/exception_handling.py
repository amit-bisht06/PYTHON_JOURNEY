# Basic try-except
try:    # --> Block of code where you put the statements that might cause an error. 
         # --> If an error occurs → Python jumps to the  except block.
    num= int(input("Enter a number: "))
    print("You Entered: ", num)
except ValueError:
    # Handles the error that occurs inside try.
    # Can specify the error type (ValueError, ZeroDivisionError) or leave it general.
    print("Invalid Input! Please enter a number") 

# * Multiple exceptions
try:
    a = 10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Divison by zero is not allowed")        
except Exception as e:  
    print("Some other error occured: ",e)  

# * Using else  --> Runs only if no error occurs in the try block.
try:
    x = int("5")
except ValueError:
    print("Invalid Conversion")
else: 
    print("Conversion successful: ",x)

# * Using finally --> This block always executes (whether an error happened or not), --> Used for cleanup tasks like closing files, releasing resources.
try:
    f = open("text.txt","w")
    f.write("Hello")
finally:
    f.close()
    print("File closed (finally block executed)")

# * Using raise --> Used to manually throw an exception.
                    # *--> Helpful when you want to enforce rules in your code.
age = 16
if age < 18:
    raise ValueError("Age must be at least 18.")                    