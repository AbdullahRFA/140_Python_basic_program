"""
A monotonic array is one that is entirely non-increasing or non-decreasing.
"""

def is_monotonic(arr,n):
    increase=decrease=True
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            decrease=False
        elif arr[i]<arr[i-1]:
            increase=False
    return increase or decrease

n = int(input("Enter the number of the elements : "))

arr=list(map(int,input().split()))

print(is_monotonic(arr,n))