"""
Least Common Multiple (LCM):
LCM, or Least Common Multiple, is the smalest multiple that is exactly divisible by two or
more numbers.
Formula:
For two numbers a and b, the LCM can be found using the formula:
LCM(𝑎, 𝑏) =|𝑎 ⋅ 𝑏|
GCD(𝑎, 𝑏)
For more than two numbers, you can find the LCM step by step, taking the LCM of pairs of
numbers at a time until you reach the last pair.
Note: GCD stands for Greatest Common Divisor.

"""
# Python Program to find the L.C.M. of two input number
# Enter the number: 54
# Enter the number: 24
# The L.C.M. is 216
def compute_lcm(x, y):
    if x > y:
        greater = x
# choose the greater number
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The L.C.M. is", compute_lcm(num1, num2))
