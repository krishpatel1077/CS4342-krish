import pandas as pd
import numpy as np

data_boston = pd.read_csv('Boston.csv')
data_medv_suburbs = data_boston['medv']

# Assuming your data is stored in a DataFrame called 'df'
# Replace 'df' with the actual variable name of your DataFrame.

# Find the suburb with the lowest median value
lowest_medv_suburb = data_boston[data_boston['medv'] == data_boston['medv'].min()]

# Get the values of other predictors for that suburb
other_predictors = lowest_medv_suburb.iloc[:, :-1]

# Calculate the overall ranges for the predictors
overall_ranges = {
    column: (data_boston[column].min(), data_boston[column].max())
    for column in data_boston.columns[:-1]  # Exclude the 'medv' column
}

# Print the results
print("Suburb with the lowest median value of owner-occupied homes:")
print(lowest_medv_suburb)
print("\nValues of other predictors for that suburb:")
print(other_predictors)
print("\nOverall ranges for the predictors:")
print(overall_ranges)
