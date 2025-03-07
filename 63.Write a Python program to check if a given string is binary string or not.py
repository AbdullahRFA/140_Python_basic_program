def is_binary_str(input_str):
# Iterate through each character in the input string
    for i in input_str:
# Check if the i is not '0' or '1'
        if i not in '01':
            return False
    return True # If any character is not '0' or '1', it's no
# If all characters are '0' or '1', it's a binary stri
# Input string to check
input_str = "1001110"
# Check if the input string is a binary string
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")