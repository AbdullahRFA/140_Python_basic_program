# Input two variables
# Enter the value of the first variable (a): 5
# Enter the value of the second variable (b): 9
# Original values: a = 5, b = 9
# Swapped values: a = 9, b = 5
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
# Swap the values using a temporary variable
a,b = b, a
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")
