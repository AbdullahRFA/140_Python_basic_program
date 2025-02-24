"""
A Disarium number is a number that is equal to the sum of its digits each raised to the
power of its respective position. For example, 89 is a Disarium number because
8^1 9^2 = 8 + 81 = 89
"""
def is_disarium(num):
    str_num = str(num)
    result=0
    length = len(str_num)
    for i in range(length):
        result+= int(str_num[i])**(i+1)

    return result == num
try:
    print("Enter the range to find disarium number")
    num1 = int(input("lower limit : "))
    num2 = int(input("Upper limit : "))
    for num in range(num1,num2+1):
        if is_disarium(num):
            print(f"{num} is Disarium")
        # else:
        #     print(f"{num} is not Disarium")
except ValueError:
    print("Enter the Integer value")

"""
2 3
4 6


"""