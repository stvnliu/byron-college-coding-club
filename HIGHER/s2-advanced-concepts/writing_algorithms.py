from random import randint
from time import sleep

# Generating some random data for testing.
def generate_random_data(lower: int, upper: int, length: int):
    data = []
    for _ in range(length):
        data.append(randint(lower, upper))
    return data

# This is an example of Bubble Sort, one of the most basic examples of an algorithm
# It functions by selecting 2 items each time, compares if they are in the correct position
# If they are not, they are swapped. If they are, continue to the next position (indicated by i)
def bubble_sort(arr: list):
    checks = 0
    while checks < len(arr):
        print(f"Checks={checks}")
        i = 0
        while i < len(arr) - 1:
            # sleep(1)
            if arr[i] < arr[i+1]: 
                checks += 1
            else: 
                tmp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = tmp
                print(arr)
            i += 1
    return arr
narr = generate_random_data(0, 100, 10)
narr = [i for i in range(100, 0)]
print(narr)
print(bubble_sort(narr))