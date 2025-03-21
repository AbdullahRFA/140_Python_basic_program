"""
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""

# Accept input from the user
input_sequence = input("Enter a sequence of whitespace-separated words: ")
# Split the input into words and convert it into a set to remove duplic
words = set(input_sequence.split())
# Sort the unique words alphanumerically
sorted_words = sorted(words)
# Join the sorted words into a string with whitespace separation
result = ' '.join(sorted_words)
# Print the result
print("Result:", result)