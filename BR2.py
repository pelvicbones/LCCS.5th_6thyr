import os
import pandas as pd
import matplotlib.pyplot as plt

# Use raw strings for file paths to avoid unicodeescape errors
input_file = r'C:\Users\kieva\Downloads\coursework\cleaned_coursework.csv'

# Check if the file exists
if not os.path.exists(input_file):
    print(f"File not found: {input_file}")
else:
    # Read the cleaned dataset
    data = pd.read_csv(input_file, dtype={
        'Life Expectancy': float,
        'weight of the animal  (kg) ': float,
        'weight that differ for female ': float
    })

    # Print the first few rows of the dataset to ensure it's loaded correctly
    print("Data Loaded Successfully")
    print(data.head())

    # Print the entire dataset
    print("\nComplete Data:")
    print(data.to_string())

    # Data Analytics

    # Ensure necessary columns are present
    required_columns = ['Species', 'Population Estimate ', 'Conservation Status', 'Life Expectancy', 'weight of the animal  (kg) ']
    if not all(col in data.columns for col in required_columns):
        print("One or more required columns are missing from the dataset.")
    else:
        # Handle Population Data
        def parse_population(estimate):
            try:
                if estimate == 'unknown' or 'less than' in estimate.lower():
                    return None
                elif 'million' in estimate.lower():
                    return float(estimate.split()[0]) * 1_000_000
                elif 'thousand' in estimate.lower():
                    return float(estimate.split()[0]) * 1_000
                else:
                    return float(estimate.replace(',', ''))
            except:
                return None

        data['Parsed Population'] = data['Population Estimate '].apply(parse_population)

        # Scatter Plot: Population vs Species
        plt.figure(figsize=(12, 8))
        species_with_population = data.dropna(subset=['Parsed Population', 'Species'])
        plt.scatter(species_with_population['Species'], species_with_population['Parsed Population'], alpha=0.7, color='blue')
        plt.title('Population of Species')
        plt.xlabel('Species')
        plt.ylabel('Population')
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()

        # Scatter Plot: Weight by Life Expectancy
        plt.figure(figsize=(12, 8))
        weight_life_data = data.dropna(subset=['weight of the animal  (kg) ', 'Life Expectancy'])
        plt.scatter(weight_life_data['weight of the animal  (kg) '], weight_life_data['Life Expectancy'], alpha=0.7, color='green')
        plt.title('Weight vs Life Expectancy')
        plt.xlabel('Weight of the Animal (kg)')
        plt.ylabel('Life Expectancy (years)')
        plt.grid()
        plt.tight_layout()
        plt.show()

        # Bar Chart: Conservation Status by Population with Species Name
        conservation_population = data.dropna(subset=['Parsed Population', 'Conservation Status', 'Species'])
        conservation_population['Species (Population)'] = conservation_population.apply(
            lambda row: f"{row['Species']} ({int(row['Parsed Population'])})", axis=1
        )
        grouped_data = conservation_population.groupby('Conservation Status')['Species (Population)'].apply(lambda x: ', '.join(x))

        print("\nConservation Status with Species and Population")
        print(grouped_data)

        # Bar Chart Visualization
        plt.figure(figsize=(12, 8))
        conservation_population_grouped = conservation_population.groupby('Conservation Status')['Parsed Population'].sum()
        conservation_population_grouped.plot(kind='bar', color='orange')
        plt.title('Conservation Status vs Population')
        plt.xlabel('Conservation Status')
        plt.ylabel('Total Population')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.tight_layout()
        plt.show()
