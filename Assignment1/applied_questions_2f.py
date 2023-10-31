import pandas as pd
import numpy as np

data_boston = pd.read_csv('Boston.csv')
data_suburbs = data_boston['ptratio']

print(f"Median of Pupil-teacher ratio: ", data_suburbs.median())