import pandas as pd
import numpy as np

data_boston = pd.read_csv('Boston.csv')

more_than_seven = data_boston[data_boston['rm'] > 7]
more_than_eight = data_boston[data_boston['rm'] > 8]

other_predictors = more_than_eight.iloc[:, :-1]



print("Number of suburbs with more than seven rooms per dwelling:", len(more_than_seven))
print("\nNumber of suburbs with more than eight rooms per dwelling:", len(more_than_eight))
print("\nValues of other predictors for the suburbs w > eight rooms :")
print(other_predictors)