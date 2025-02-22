"""
A pronic number, also known as an oblong number or rectangular number, is a type of
figurate number that represents a rectangle. It is the product of two consecutive integers, n
and (n + 1). Mathematicaly, a pronic number can be expressed as:
𝑃𝑛
= 𝑛 ∗ (𝑛 + 1)
For example, the first few pronic numbers are:
𝑃1 = 1 ∗ (1 + 1) = 2
𝑃2 = 2 ∗ (2 + 1) = 6
𝑃3 = 3 ∗ (3 + 1) = 12
𝑃4 = 4 ∗ (4 + 1) = 20





"""
def is_pronic(num):
    for n in range(1,int(num**0.5)+1):
        if n*(n+1) == num:
            return True

    return False

try:
    print("Enter the range to find pronic number ")
    num1 = int(input("Lower limit : "))
    num2 = int(input("Upper limit : "))

    for num in range(num1,num2+1):
        if is_pronic(num):
            print(f"{num} is Pronic number")
except ValueError:
    print("Enter only Integer value")