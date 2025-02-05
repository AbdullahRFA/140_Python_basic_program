"""
Fibonacci sequence:
The Fibonacci sequence is a series of numbers where each number is the sum of the two
preceding ones, typicaly starting with 0 and 1. So, the sequence begins with 0 and 1, and
the next number is obtained by adding the previous two numbers. This pattern continues
indefinitely, generating a sequence that looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
Mathematicaly, the Fibonacci sequence can be defined using the folowing recurrence
relation:
𝐹(0
) = 0 𝐹(1) = 1 𝐹(𝑛) = 𝐹(𝑛 − 1) + 𝐹(𝑛 − 2)𝑓𝑜𝑟𝑛 > 1

"""


# Initialize the Fibonacci sequence
fib = [0, 1]

# Get user input for nth Fibonacci number
nth = int(input("Enter which (nth) Fibonacci number you want: "))

# Generate Fibonacci sequence up to nth number
for i in range(2, nth):
    fib.append(fib[i-1] + fib[i-2])

# Print the nth Fibonacci number
print(f'The {nth}th Fibonacci number is: {fib[-1]}')

for i in range(0,len(fib)):
    print(f'{i+1}th fibonacci number = {fib[i]}')