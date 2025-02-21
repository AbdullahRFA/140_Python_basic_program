"""
Happy Number: A Happy Number is a positive integer that, when you repeatedly replace
the number by the sum of the squares of its digits and continue the process, eventualy
reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number
is not a Happy Number.
For example:
19 is a Happy Number because:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

The process reaches 1, so 19 is a Happy Number.

"""
def is_happy(number):
    seen = set()
    while number!=1 and number not in seen:
        seen.add(number)
        number = sum([int(x)**2 for x in str(number)])
    seen.clear()
    return number == 1
try:
    print("Enter the range to check if it is happy number or not ")
    num1 = int(input("Lower limit : "))
    num2 = int(input("Upper limit : "))

    for num in range(num1,num2+1):
        if is_happy(num):
            print(f"{num} is a happy number ")
        # else:
        #     print(f"{num} is not a happy number ")

except ValueError:
    print("Enter only Integer number")