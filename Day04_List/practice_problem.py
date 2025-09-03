# Practice Questions:
"""
1. Create a list of 5 friend's names and print each using a loop.
2. Take 5 numbers from the user and store them in a list, then print the sum.
3. Create a list of fruits and replace the second element with "kiwi".
4. Sort a list of numbers in descending order.
5. Count how many times "apple" occurs in a list. 
"""

# Solution 1
friends = ["A", "C", "D", "H", "T"]
for individual in friends:
    print("Friend: ", individual)

#Solution 2
numbers = []
print("\n")
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total_sum = sum(numbers)
print("The sum of the numbers is:", total_sum)

#Solution 3
fruits = ["Apple", "Banana", "Grapes", "Guava", "Apple"]
print("\nFruits: ",fruits)
fruits[1] = "Kiwi"
print("After replace: ", fruits)


#Solution 4
numbers = [5,2,7,8,9,10]
print("\nNumbers: ", numbers)
numbers.sort(reverse=True)
print("After sorting: ",numbers)

# Solution 5
count = fruits.count("Apple")
print("\nApple Count: ",count)