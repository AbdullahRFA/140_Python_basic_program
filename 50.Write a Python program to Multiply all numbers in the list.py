num = int(input("Enter the number of list : "))
my_list = list(map(int,input().split()))

mul_of_list = 1
for x in my_list:
    mul_of_list *= x

print(f"Sum of given list is {mul_of_list}")

