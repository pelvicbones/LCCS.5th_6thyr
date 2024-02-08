import csv

csvfile = open("myfile3.csv", "r", newline='')
csvreader = csv.reader(csvfile)

# Read and print the header
header = next(csvreader, None)
print("Header:", header)

# Read and print the first row
row = next(csvreader, None)
print("Row 1:")
print(row[0])  # Access the first column
print(row[1])  # Access the second column
#add code to accum average here
#add code to count the records here
row = next(csvreader, None)
print("Row 2:")
print(row[0])  # Access the first column
print(row[1])  # Access the second column
#add code to accum average here
#add code to count the records here


# Close the file
csvfile.close()
#print the average(s) here


########################Loop thru file###################################
#No need to close the file when using this "with open .....as csv file etc"
"""
#alternative way of looping thru file
#dont have to know what length or number of records
dont have to close the file

with open("myfile3.csv", "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader, None)
    print("Header with:", header)
    for row in csvreader:
        print(row[0])
        print(row[1])
        #add code to accum average here
        #add code to count the records here

################## PANDAS ########################
# open the file and read it all into one variable
# Read the entire CSV file into a pandas DataFrame
# Calculate the Mean of each searate column by referring to the Column Heading
#DOES FILE NEED TO BE OPENED FIRTS???
df = pandas.read_csv('myfile3.csv')
print(df.to_string())
# Filter out the column, value_eur
temp_values = df['Temp']
mean_value_temp = round(statistics.mean(temp_values), 2)
print("Mean Value Temp:", mean_value_temp)
noise_values = df['Noise']
mean_value_noise = round(statistics.mean(noise_values), 2)
print("Mean Value Noise:", mean_value_noise)
"""


