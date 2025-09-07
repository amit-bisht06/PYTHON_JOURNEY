# Table Program using for loop

num = int(input("Enter the number: "))

for i in range(10):
    result = num*(i+1)
    print(f"{num} * {i+1} = {result}")