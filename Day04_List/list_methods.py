# Common List Methods

numbers = [5, 2, 9, 1, 5, 6]

# 1. Length
print("Length: ", len(numbers))


# 2. Sorting
numbers.sort()
print("Sorted: ", numbers)


# 3. Reversing
numbers.reverse()
print("Reversed: ", numbers)


# 4. Count
print("Count of 5: ", numbers.count(5))         #count the ffrequency of that number


# 5. Copy
copy_numbers = numbers.copy()
print("Copied List: ", copy_numbers)


# 6. Insert  --> The insert() method inserts an item at the specified index:
numbers.insert(2, "7")
print("After insert(): ",numbers)


# 7. Remove and Pop & del
#Remove --> The remove() method removes the specified item.
numbers.remove(9)
print("After remove: ", numbers)

# Pop ---> The pop() method removes the specified index. & If you do not specify the index, the pop() method removes the last item.
popped = numbers.pop()
print("Popper Element: ", popped)
print("After pop: ", numbers)

#del --> The del keyword also removes the specified index:
del numbers[1]
print("After del operation: ", numbers)


# 8. Extend List --> To append elements from another list to the current list, use the extend() method.
two_digits = [99, 88, 77, 66, 55, 44, 33, 22,11 ]
numbers.extend(two_digits)
print("After Extending the list: ",numbers)


#  Clear
numbers.clear()
print("After clear: ",numbers)