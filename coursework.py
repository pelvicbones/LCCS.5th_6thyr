import pandas as pd
import csv

input_file = 'courseworkproject.csv'
output_file = 'cleaned.csv'

data = pd.read_csv('courseworkproject.csv')
print(data.head())
#print(data.info())

# Function to check if a row contains spaces or asterisks
def contains_invalid_characters(row):
    for cell in row:
        if ' ' in cell or '*' in cell:
            return True
    return False

print(data.describe())   # Get summary statistics for numerical columns

#cleaning the data , check if there are any missing data
no_data = data.isnull().sum()
print(no_data)

'''
# if there are any missing values set as 'NA'
data['weight_that_differ_for_female'] = data['weight_that_differ_for_female'].fillna(value='NA')

'''

# Process each row
for row in data :
    if not contains_invalid_characters(row):
        data.writerow(row) 

print(f"Cleaned data has been written to {output_file}")
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
print(data.columns)

data.to_csv('cleaned_coursework.csv', index=False)
print(f"Cleaned data has been written to {output_file}")

