num = int(input("Enter the number of list : "))
my_list = list(map(int,input().split()))

# sum_of_list = 0
# for x in my_list:
#     sum_of_list += x

# print(f"Sum of given list is {sum_of_list}")
print(f"Sum of given list is {sum(my_list)}")
