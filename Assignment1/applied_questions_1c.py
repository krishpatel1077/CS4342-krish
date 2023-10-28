import pandas as pd
import numpy as np

data_auto = pd.read_csv("Assignment1/Auto.csv")
quant_predictors = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']

#use a dictionary to store key value pairs of predictors and the calculated range
means = {}
stddevs = {}
for predictor in quant_predictors:
    mean_val = np.mean(data_auto[predictor])
    std_dev = np.std(data_auto[predictor])
    means[predictor] = mean_val
    stddevs[predictor] = std_dev

#display the data
for predictor, mean_val in means.items():
    print(f"Mean of {predictor}: {mean_val:.2f}")

for predictor, std_dev in stddevs.items():
    print(f"Std Dev of {predictor}: {std_dev:.2f}")