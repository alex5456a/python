import numpy as np

arr_1 = np.array([67, 23, 10, -100, 234, 5])
arr_2 = np.array([1, 2, 3, 4, 5])
arr_3 = np.array([1, 2, 3, 4, 5])

both = np.concatenate((arr_1, arr_2, arr_3))
print(both)

arr_1_extended = np.append(arr_1, 1000)
print(arr_1_extended)

arr_1_deleted = np.delete(arr_1, 3)
print(arr_1_deleted)