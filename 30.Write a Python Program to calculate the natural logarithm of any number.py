"""
The natural logarithm, often denoted as 𝑙𝑛
, is a mathematical function that represents the
logarithm to the base 𝑒 𝑒
, where is the mathematical constant approximately equal to
2.71828 𝑥 𝑥
. In other words, for a positive number , the natural logarithm of is the exponent
𝑒𝑦
𝑦 = 𝑥
that satisfies the equation .
Mathematically, the natural logarithm is expressed as:
ln(𝑥)
It is commonly used in various branches of mathematics, specially in calculus and
mathematical analysis, as wel as in fields such as physics, economics, and engineering.
The natural logarithm has properties that make it particularly useful in situations involving
exponential growth or decay.


"""
# Enter a number: 1.4
# The natural logarithm of 1.4 is: 0.3364722366212129

import math
global result
num = float(input("Enter a number: "))
if num <= 0:
    print("Please enter a positive number.")
else:
# Calculate the natural logarithm (base e) of the number
    result = math.log(num)
print(f"The natural logarithm of {num} is: {result}")
