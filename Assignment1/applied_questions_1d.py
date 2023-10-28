import pandas as pd
import numpy as np

data_auto = pd.read_csv("Assignment1/Auto.csv")
data_auto = data_auto.drop(range(10, 86))
quant_predictors = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']

ranges = {}
means = {}
stddevs = {}

for predictor in quant_predictors:
    min_val = data_auto[predictor].min()
    max_val = data_auto[predictor].max()
    datarange = int(max_val) - int(min_val)
    ranges[predictor] = datarange
    mean_val = np.mean(data_auto[predictor])
    std_dev = np.std(data_auto[predictor])
    means[predictor] = mean_val
    stddevs[predictor] = std_dev

#display the data
for predictor, datarange in ranges.items():
    print(f"Range of {predictor}: {datarange:.2f}")

for predictor, mean_val in means.items():
    print(f"Mean of {predictor}: {mean_val:.2f}")

for predictor, std_dev in stddevs.items():
    print(f"Std Dev of {predictor}: {std_dev:.2f}")