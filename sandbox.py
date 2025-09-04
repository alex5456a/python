import pandas as pd
import numpy as np

user_data = {
    'id': { 'a': 123, 'b': '234', 'c': 345 },
    'name': { 'a': 'Bob', 'b': 'Sue', 'c': 'Dean' },
    'age': { 'a': 30, 'b': 40, 'c': 50 },
}

index = np.array(['a', 'b', 'c'])

user_data_s = {
    'id': pd.Series([123, 345, 456], index=index),
    'name': pd.Series(['Bob', 'Sue', 'Dean'], index=index),
    'age': pd.Series([30, 40, 50], index=index),
}

print(pd.DataFrame(user_data))
print(pd.DataFrame(user_data_s))