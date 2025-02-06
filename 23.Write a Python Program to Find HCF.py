"""
Highest Common Factor(HCF):
HCF, or Highest Common Factor, is the largest positive integer that divides two or more
numbers without leaving a remainder.
Formula:

For two numbers a and b, the HCF can be found using the formula:
HCF(𝑎, 𝑏) = GCD(𝑎, 𝑏)
For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers at
a time until you reach the last pair.
Note: GCD stands for Greatest Common Divisor.


"""


# Python program to find H.C.F of two numbers
# define a function
def compute_hcf(x, y):
    # choose the smaller number

    global hcf
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The H.C.F. is", compute_hcf(num1, num2))
# Enter the number: 54
# Enter the number: 24
# The H.C.F. is 6
