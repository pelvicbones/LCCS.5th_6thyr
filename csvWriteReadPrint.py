import csv
import pandas
import statistics

csvfile = open("myfile3.csv", "x",newline = "")
print("File Created")
# Create column headers
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Temp', 'Noise'])
print("Columns Created")

# Create 2 rows of data 
csvwriter.writerow([25, 27])
csvwriter.writerow([23, 24])

print("Data Created")
# Close the file
csvfile.close()
print("closed after created rows")

# Open the file read it and print the first 2 rows
csvfile = open("myfile3.csv","r", newline = "")
line = csvfile.readline()
print(line, "readline1")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline3")
line = csvfile.readline()
print(line, "readline4")
line = csvfile.readline()
print(line, "readline5")

csvfile.close()
print("closed after printing rows")

# Open the file to append to it
csvfile = open('myfile3.csv',"a", newline = "")
csvwriter = csv.writer(csvfile)
csvwriter.writerow([20, 28])
csvwriter.writerow([19, 10])
csvfile.close()
print("closed append")
