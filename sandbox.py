import numpy as np

names = np.array(['Shaun', 'Geraldo', 'Bob', 'Jim'])
ages = np.array([30, 30, 40, 40])
drinks_coffee = np.array([True, False, True, False])

ind = np.lexsort((names, ages))
# for i in ind:
#     print(f"{names[i]} + {ages[i]} + {drinks_coffee[i]}")

for name, age, coffee in zip(names[ind], ages[ind], drinks_coffee[ind]):
    print(f'{name} - {age} - {coffee}')