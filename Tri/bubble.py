from Swap.Swap import swap
import random
import timeit

"""Decorator to be able tu mesure the time of execution"""
def wrapper(func, *args, **kwargs):
     def wrapped():
         return func(*args, **kwargs)
     return wrapped


"""bubble sort"""
def bubble(T):
    for i in reversed(range(len(T))):
        for j in range(i):
            if T[j] >= T[j+1]:
                T[j], T[j+1] = swap(T[j], T[j+1])
    return T

print("\n###############\tBubble Sort\t################\n")
arr = [random.randint(0, 200) for x in range(100)]
print("Before sort : ", arr)
print("After sort : ", bubble(arr))

"""Time of execution"""
wrapped = wrapper(bubble, arr)
print("Time of execution : ", timeit.timeit(wrapped, number=1), "s")
