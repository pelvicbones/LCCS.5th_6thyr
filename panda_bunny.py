import statistics
import pandas


# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('bunny.csv')

# Filter out the column, value_eur

bunny_values = df['bunnys']
print ("BUNNY")
print(bunny_values)
print ("")

eggyolk_values = df["egg_yolk"]
print("EGG YOLK")
print ( eggyolk_values)
print ("")

expiredmilk_values = df["expired_milk"]
print ("EXPIRED MILK")
print (expiredmilk_values)
print ("")

mean_value_in_bunny = round(statistics.mean(bunny_values), 2 )
print("average value of bunnys= " , mean_value_in_bunny)

mean_value_in_eggyolk = round(statistics.mean(eggyolk_values), 2 )
print("average value of egg yolk= " , mean_value_in_eggyolk)

mean_value_in_expiredmilk = round(statistics.mean(expiredmilk_values), 2 )
print("average value of expired milk= " , mean_value_in_expiredmilk)