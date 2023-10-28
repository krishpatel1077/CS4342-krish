import pandas as pd
import matplotlib.pyplot as plt

data_auto = pd.read_csv("Assignment1/Auto.csv")
quant_predictors = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']

for predictor in quant_predictors:
    plt.figure(figsize=(8, 6))
    plt.scatter(data_auto[predictor], data_auto['mpg'], alpha=0.5)
    plt.title(f'Scatterplot of {predictor} vs. MPG')
    plt.xlabel(predictor)
    plt.ylabel('MPG')
    plt.grid(True)
    plt.show()