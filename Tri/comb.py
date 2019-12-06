import random
from Swap.Swap import swap
import timeit


"""Decorator to be able tu mesure the time of execution"""
def wrapper(func, *args, **kwargs):
     def wrapped():
         return func(*args, **kwargs)
     return wrapped


def comb(arr):
    interval = len(arr)-1
    sp = True
    while interval > 1 and sp is True:
        interval = int(interval/1.3)
        if interval < 1:
            interval = 1
        i = 0
        sp = False
        while i <= (len(arr) - 1) - interval:
            if arr[i] > arr[i + interval]:
                arr[i], arr[i + interval] = swap(arr[i], arr[i+interval])
                sp = True
            i += 1
    return arr


print("\n###############\tComb Sort\t################\n")
arr = [random.randint(0, 100) for i in range(100000)]
print("Before sort : ", arr)
print("After sort : ", comb(arr))

"""Time of execution"""
wrapped = wrapper(comb, arr)
print("Time of execution : ", timeit.timeit(wrapped, number=1), "s")
