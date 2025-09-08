# Find First Digit 
def find_First(num):
    while num>=10:
        num= num // 10
    return num

number = int(input("Enter a number: "))
first_digit = find_First(number)
print("First Digit of a number: ", first_digit)