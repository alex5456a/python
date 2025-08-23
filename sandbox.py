import numpy as np

arr_1d = np.array([67, 23, 10, -100, 234, 5])
#arr_1d.sort()
arr_1d_sorted = np.sort(arr_1d)

str_arr_1d = np.array(['cherry', 'banana', 'data', 'apple', 'eggplant'])
sorted_str_arr_1d = np.sort(str_arr_1d)

sorted_indiced = np.argsort(arr_1d)

print(str_arr_1d)
print(arr_1d)
print(arr_1d_sorted)
print(sorted_indiced)

for i in sorted_indiced:
    print(arr_1d[i])