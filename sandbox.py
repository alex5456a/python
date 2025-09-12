import numpy as np
import pandas as pd

ev_data = pd.read_csv('ev_data.csv')
ev_data.head(3)
ev_data.tail(3)
ev_data.info()
ev_data.describe()
ev_data[['Postal Code', 'Model Year', 'Base MSRP']].head()
ev_data.nunique()
years = ev_data['Postal Code'].unique()
years.sort()
original_col_names = ev_data.columns
ev_data.columns ['vin', 'county', 'city', 'state', 'postal_code', 'model_year', 'make', 'model', 'ev_type', 'cafv', 'range', 'base_msrp', 'district', 'dol_id', 'location']
names_map = { key: value for key, value in zip(ev_data.colums, original_col_names)}
ev_data.rename(columns=names_map)