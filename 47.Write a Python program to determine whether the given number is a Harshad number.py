"""
A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
In other words, a number is considered a Harshad number if it can be evenly divided by the
sum of its own digits.
For example:
18 is a Harshad number because 42 is not a Harshad number because 1 + 8 = 9
, and 18 is divisible by 9
4 + 2 = 6
, and 42 is not divisible by 6.
"""

def is_harshad_number(num):
    # Calculate the sum of the digits of the number
    digit_sum = sum(int(i) for i in str(num))
    # Check if the number is divisible by the sum of its digits
    return num % digit_sum == 0
    # Input a number
num = int(input("Enter a number: "))
# Check if it's a Harshad Number
if is_harshad_number(num):
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is not a Harshad Number.")