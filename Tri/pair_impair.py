import random
from Swap.Swap import swap
import timeit


"""Decorator to be able tu mesure the time of execution"""
def wrapper(func, *args, **kwargs):
     def wrapped():
         return func(*args, **kwargs)
     return wrapped


def pair_impair(arr):
    for i in range(1, len(arr)-1):
        #paire impaire
        for j in range(0, len(arr)-1, 2):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = swap(arr[j], arr[j+1])
        #impaire paire
        for j in range(1, len(arr)-1, 2):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = swap(arr[j], arr[j+1])
    return arr


print("\n###############\tPaire Impaire Sort\t################\n")
arr = [random.randint(0, 100) for x in range(100)]
print("Before sort :", arr)
print("After sort :", pair_impair(arr))

"""Time of execution"""
wrapped = wrapper(pair_impair, arr)
print("Time of execution : ", timeit.timeit(wrapped, number=1), "s")
