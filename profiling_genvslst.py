#profiling generator vs list performance for huge series
import sys
nums_squared_lc = [num**2 for num in range(5)]
print(nums_squared_lc)
print("Size of List for squaring range(5) ",sys.getsizeof(nums_squared_lc))

nums_squared_gc =(num**2 for num in range(5))
print(type(nums_squared_gc))
print("Size of Generator for squaring range(5) ",sys.getsizeof(nums_squared_gc))

for i in nums_squared_gc:
    print(i)