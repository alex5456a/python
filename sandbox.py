import numpy as np

numbers = np.arange(0, 25)
[print(num) for num in numbers[[0, 1, -2, -1]] if (num > 5)]
[print(num) for num in numbers[:(len(numbers)//2)] if (num > 5)]

numbers_2d = numbers.reshape(5, 5)
print(numbers_2d)
summary = np.sum(numbers_2d, axis=1).tolist()
for s in summary:
    if s > 50:
        [print(num) for num in numbers_2d[summary.index(s),[0, -1]]]

#[print(x) for x in numbers if x % 2 == 0]
# print(numbers[numbers % 2 == 0])