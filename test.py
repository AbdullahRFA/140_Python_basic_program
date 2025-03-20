import math
def is_prime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True
my_set = set()
def print_prime_factors(n):
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                print(i)
                my_set.add(i)
                n/=i

n = 100
print(my_set)
print_prime_factors(n)