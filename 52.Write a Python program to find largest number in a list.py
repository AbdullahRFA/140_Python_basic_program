# Sample list of numbers
numbers = [30, 10, -45, 5, 20]
# Initialize a variable to store the maximum value, initially set to th
maximum = numbers[0]
# Iterate through the list and update the minimum value if a smaller nu
for i in numbers:
    if i > maximum:
        maximum = i
# Print the minimum value
print("The largest number in the list is:", maximum)
# print("The largest number in the list is:", max(numbers))