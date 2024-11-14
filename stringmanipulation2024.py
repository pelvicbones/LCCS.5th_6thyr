#ask user for name and display the length of their name
name = input("enter your name ")
lename = len(name)
print ("the length of your name is =" , lename)

surname = input("enter your surname ")
lensur = len(surname)
print ("the length of your surname is=", lensur)

print (name , surname)

fullname = len(name + surname)
print ( fullname)

#subject
subject = input("whats your favourite subject")
for letter in subject :
    print (letter , end='-')


# Display a line of your favorite poem
poem = "he saw me crying, he crode, we both crew."
print(poem)

# Ask the user to pick two points with range checks
poem_length = len(poem)

# Input for the starting point
point = int(input(f"Pick a starting point (0 to {poem_length - 1}): "))
while point < 0 or point >= poem_length:
    print("Invalid starting point. Please choose a number within the range.")
    point = int(input(f"Pick a starting point (0 to {poem_length - 1}): "))

# Input for the ending point
point2 = int(input(f"Pick an ending point ({point} to {poem_length}): "))
while point2 <= point or point2 > poem_length:
    print("Invalid ending point. It should be greater than the starting point and within the range.")
    point2 = int(input(f"Pick an ending point ({point} to {poem_length}): "))

# Display the characters between those two points
print("Selected text:", poem[point:point2])

#asking user to type in a word in upper case
cap = input("please type a word in upper case")
if cap.isupper():
    print ("upper case")
else :
    print ("this is not upper case")


