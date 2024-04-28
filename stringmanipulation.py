name = input ("Enter your first name ")
surname = input ("Enter your surname ")
print ( "Hello" , name , surname )

subject = input (" What is your favourite subject ")
for letter in subject :
    print ( letter, end= "-")
    
poem = (" Functional hospital wards ") 
starting = input(" Pick an starting point")
ending = input (" Pick an ending point")
print ( starting , poem , ending )

while True:
    upper = input("TYPE SOMETHING IN UPPERCASE: ")
    if upper.isupper():
        print("Uppercase")
        break
    else:
        print("This is not uppercase, try again.")
    
code = input (" Enter your postcode")
print ( code[:2])




