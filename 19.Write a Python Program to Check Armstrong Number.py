"""
Armstrong Number:
It is a number that is equal to the sum of its own digits, each raised to a power equal to the
number of digits in the number.
For example, let's consider the number 153:
It has three digits (1, 5, and 3).
If we calculate + , we get , which is equal to .
13 +
53 33 1 + 125 + 27 153
So, 153 is an Armstrong number because it equals the sum of its digits raised to the power
of the number of digits in the number.


"""
num = int(input("Enter a number: "))
# Calculate the number of digits in num
num_str = str(num)
num_digits = len(num_str)
# Initialize variables
sum_of_powers = 0
temp_num = num
# Calculate the sum of digits raised to the power of num_digits
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10
# Check if it's an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
# Enter a number: 9474
# 9474 is an Armstrong number.