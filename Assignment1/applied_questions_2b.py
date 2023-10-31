import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_boston = pd.read_csv('Boston.csv')
#relevant predictors graphed with respect to the median value of the owner-occupied homes ($1000's)
predictors = ['crim', 'zn', 'indus', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'lstat']

for predictor in data_boston:
    plt.figure(figsize=(8, 6))
    plt.scatter(data_boston[predictor], data_boston['medv'], alpha=0.5)
    plt.title(f'Scatterplot of {predictor} vs. Median Values ($1000s)')
    plt.xlabel(predictor)
    plt.ylabel('Median Values ($1000s)')
    plt.grid(True)
    plt.show()

