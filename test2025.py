import pandas as pd
import numpy as np

# Input and output file paths
input_file = r'C:/Users/ksia/python programme/courseworkproject.csv'
output_file = r'C:/Users/ksia/python programme/cleaned_coursework.csv'

# Step 1: Read the dataset
data = pd.read_csv(input_file, dtype=str)

# Step 2: Clean column names by removing leading/trailing spaces
data.columns = data.columns.str.strip()

# Step 3: Check if 'Population estimate' exists in the data and print raw values for inspection
print("Raw Population Estimate Values:")
print(data['Population estimate'].head())  # Displaying first few rows for inspection

# Step 4: Clean and convert the 'Population estimate' column
def clean_population_estimate(value):
    if isinstance(value, str):
        # Remove unwanted characters like '~' and '*'
        value = value.replace('~', '').replace('*', '').strip()

        # If value is in a range format (e.g., "10,000-25,000"), split it and average the range
        if '-' in value:
            try:
                parts = value.split('-')
                min_val = float(parts[0].replace(',', ''))
                max_val = float(parts[1].replace(',', ''))
                return (min_val + max_val) / 2
            except ValueError:
                # If there's an issue with parsing, return NaN
                return np.nan
        
        # If the value is a single number, remove commas and return as float
        try:
            return float(value.replace(',', ''))
        except ValueError:
            # If not a valid number, return NaN
            return np.nan
    return np.nan

# Apply cleaning function to the 'Population estimate' column
data['Population estimate'] = data['Population estimate'].apply(clean_population_estimate)

# Step 5: Check if the population column is now populated
print("Cleaned Population Estimate Values:")
print(data['Population estimate'].head())  # Displaying first few rows after cleaning

# Step 6: Save the cleaned data to the output file
data.to_csv(output_file, index=False)

# Step 7: Display cleaned data (Optional)
print("Cleaned Data:")
print(data.head())  # Displaying first few rows of cleaned data
