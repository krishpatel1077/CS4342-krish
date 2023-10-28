import pandas as pd
import numpy as np

data_auto = pd.read_csv("Assignment1/Auto.csv")
quant_predictors = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']

#use a dictionary to store key value pairs of predictors and the calculated range
ranges = {}
for predictor in quant_predictors:
    min_val = data_auto[predictor].min()
    max_val = data_auto[predictor].max()
    datarange = int(max_val) - int(min_val)
    ranges[predictor] = datarange

#display the data
for predictor, datarange in ranges.items():
    print(f"Range of {predictor}: {datarange:.2f}")