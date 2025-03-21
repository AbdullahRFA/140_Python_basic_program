"""
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""

# Accept input from the user
input_sequence = input("Enter a comma-separated sequence of words: ")
# Split the input into a list of words
words = input_sequence.split(',')
# Sort the words alphabetically
sorted_words = sorted(words)
# Join the sorted words into a comma-separated sequence
sorted_sequence = ','.join(sorted_words)
# Print the sorted sequence
print("Sorted words:", sorted_sequence)