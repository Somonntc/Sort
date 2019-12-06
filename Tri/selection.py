import random
from Swap.Swap import swap
import timeit


"""Decorator to be able tu mesure the time of execution"""
def wrapper(func, *args, **kwargs):
     def wrapped():
         return func(*args, **kwargs)
     return wrapped


def selection(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = swap(arr[i], arr[min_index])
    return arr


print("\n###############\tSelection Sort\t################\n")
arr = [random.randint(0, 100) for i in range(100)]
print("Before sort : ", arr)
print("After sort : ", selection(arr))

"""Time Execution"""
wrapped = wrapper(selection, arr)
print("Time of execution : ", timeit.timeit(wrapped, number=1), "s")
