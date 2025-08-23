import numpy as np

arr = np.arange(0, 21, 2)
indices = np.array([0, 1, -2, -1])
even_indices = np.arange(0, arr.size, 2)
odd_indices = np.arange(1, arr.size, 2)

# print(indices)
# print(arr[even_indices])
# print(arr[odd_indices])

arr_2d = np.arange(0, 25).reshape(5, 5)
print(arr_2d)
print()
print(arr_2d[[0, 2, 4], -3:])