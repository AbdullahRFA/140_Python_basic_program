# Addition
# Enter the first number for addition: 5
# Enter the second number for addition: 6
# sum: 5.0 + 6.0 = 11.0
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

# Division
# Enter the dividend for division: 25
# Enter the divisor for division: 5
# Division: 25.0 / 5.0 = 5.0
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")
