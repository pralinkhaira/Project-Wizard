#Data Cleaning Script

import pandas as pd

# Load the CSV file
data = pd.read_csv('data.csv')

# Remove duplicates
data = data.drop_duplicates()

# Fill missing values with the mean
data.fillna(data.mean(), inplace=True)

# Save the cleaned data
data.to_csv('cleaned_data.csv', index=False)
