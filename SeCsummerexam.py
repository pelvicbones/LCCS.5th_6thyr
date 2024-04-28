#  LCCSSummer23-B 
# Name: kieva sia
# This function multiplies two numbers 
num_times = int(input("Enter the number of times you want to run the code: "))

# Loop to run the code for the specified number of times
for i in range(num_times):
    print(f"\nCalculation {i+1}:")
    
    
def multiply(x, y):
    return round(x * y ,1 )
# This function divides two numbers
def divide(x, y):
    return round (x / y , 1 )
# ADD
def add(x, y):
    return round(x + y ,1)
#SUBTRACT
def subtract(x, y):
    return round(x - y ,1 )
# Main Program
import random # To generate random numbers

print("Select operation.")
print("1.Multiply")
print("2.Divide")
print("3. Add ")
print("4. subtract")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
if choice == '1':
    print(num1,"X",num2,"=", multiply(num1,num2))
elif choice == '2':
    print(num1,"/",num2,"=", divide(num1,num2))
    
elif choice == '3' :
    print( num1 , "+" , num2 , "=" , add(num1,num2))
    
elif choice == '4' :
    print( num1 , "-" , num2 , "=" , subtract(num1,num2))
    
