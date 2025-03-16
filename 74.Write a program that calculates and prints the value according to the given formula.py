"""
𝑄 = Squ
are root of 2𝐶𝐷
𝐻
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-
separated sequence.
Example
Let us assume the following comma separated input sequence is given to the
program:
100,150,180
The output of the program should be:
18,22,24
"""

import math
# Fixed values
C = 50
H = 30
# Function to calculate Q
def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))
# Input comma-separated sequence of D values
input_sequence = input("Enter comma-separated values of D: ")
D_values = input_sequence.split(',')
# Calculate and print Q for each D value
result = [calculate_Q(int(D)) for D in D_values]
print(','.join(map(str, result)))