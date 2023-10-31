import pandas as pd
import numpy as np

data_boston = pd.read_csv('Boston.csv')
data_suburbs = data_boston['chas']

suburbs = data_boston[data_boston['chas'] == 1]
count = len(suburbs)

print("number of suburbs near charles river", count)