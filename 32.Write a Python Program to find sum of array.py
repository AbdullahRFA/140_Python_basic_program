"""
In Python, an array is a data structure used to store a collection of elements, each identified
by an index or a key. Unlike some other programming languages, Python does not have a
built-in array type. Instead, the most commonly used array-like data structure is the list.
A list in Python is a dynamic array, meaning it can change in size during runtime. Elements
in a list can be of different data types, and you can perform various operations such as
adding, removing, or modifying elements. Lists are defined using square brackets [] and
can be indexed and sliced to access specific elements or sublist.
Example of a simple list in Python:
my_list = [1, 2, 3, 4, 5]
This list can be accessed and manipulated using various built-in functions and methods in
Python.

"""

# Finding Sum of Array Using sum()
num = int(input("Enter the number of elements: "))
arr = []
for i in range(num):
    arr.append(int(input(f"Enter number {i + 1}: ")))
ans = sum(arr)
print('Sum of the array is', ans)
# Sum of the array is 6

"""


# Function to find the sum of elements in an array
def sum_of_array(arr):
    total = 0 # Initialize a variable to store the sum
    for element in arr:
        total += element # Add each element to the total
    return total
# Example usage:
array = [1, 2, 3]
result = sum_of_array(array)
print("Sum of the array:", result)

"""
