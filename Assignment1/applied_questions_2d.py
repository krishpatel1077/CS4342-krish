import pandas as pd
import numpy as np

data_boston = pd.read_csv('Boston.csv')
predictors = ['crim', 'tax', 'ptratio']

ranges = {}
for predictor in predictors:
    min_val = data_boston[predictor].min()
    max_val = data_boston[predictor].max()
    datarange = int(max_val) - int(min_val)
    ranges[predictor] = datarange

for predictor, datarange in ranges.items():
    print(f"Range of {predictor}: {datarange:.2f}")