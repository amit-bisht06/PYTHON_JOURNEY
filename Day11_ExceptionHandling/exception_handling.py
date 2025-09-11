# Basic try-except
try: 
    num= int(input("Enter a number: "))
    print("You Entered: ", num)
except ValueError:
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
