import numpy as np
import pandas as pd

my_series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
my_series_d = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'c': 5})
my_series_np = pd.Series(np.array([1, 2, 3, 4, 5]), index=np.array(['a', 'b', 'c', 'd', 'e']))

print(my_series)
print(my_series_d)
print(my_series_np)