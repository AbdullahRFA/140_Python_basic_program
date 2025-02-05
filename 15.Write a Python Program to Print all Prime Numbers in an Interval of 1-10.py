# Python program to display all the prime numbers within an interval

lower = int (input("Enter lower interval : "))
upper = int (input("Enter lower interval : "))
prime =[]
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    flag = False
    if num <= 1:
        print(f"{num}, is not a prime number\n")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} can divide by {i}")
                flag = True  # break out of loop
                break
                # if factor is found, set flag to True
                # check if flag is True
        if flag:
            print(f"{num}, is not a prime number\n")
        else:
            print(f"{num}, is a prime number\n")
            prime.append(num)

print(f"prime numbers in the interval of {lower} and {upper}: ",prime)