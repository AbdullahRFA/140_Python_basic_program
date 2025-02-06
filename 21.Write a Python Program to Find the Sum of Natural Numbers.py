"""
Natural numbers are a set of positive integers that are used to count and order objects.
They are the numbers that typicaly start from 1 and continue indefinitely, including al the
whole numbers greater than 0. In mathematical notation, the set of natural numbers is often
denoted as "N" and can be expressed as:
𝑁 = 1, 2, 3, 4, 5, 6, 7, 8,
. . .

"""
# Enter the limit: 10
# The sum of natural numbers up to 10 is: 55
limit = int(input("Enter the limit: "))
# Initialize the sum
sum = 0
# Use a for loop to calculate the sum of natural numbers
for i in range(1, limit + 1):
    sum += i
# Print the sum
print("The sum of natural numbers up to", limit, "is:", sum)
