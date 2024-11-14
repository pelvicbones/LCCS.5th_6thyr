
# ask user for name and number , displaying their name for x num 
name = input("what is your name?")
num = int(input("enter a number"))
for i in range (num):
    print (name)
    
#ask user for name and display each letter on a seperate line and then ask the user to input a value , the value inputed is the number of time this process repeats

name2 = input ("enter second name")
num2 = int(input("enter a number "))

for _ in range(num2):  # Outer loop repeats the entire process
    for letter in name2:  # Inner loop goes through each letter of the name
        print(letter)
    print()  # Print a blank line between repetitions for clarity
    

