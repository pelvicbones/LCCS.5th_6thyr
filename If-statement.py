num1 = input("Enter the first number ")
num2 = input("Enter the second number ")

if int(num1 > num2) :
    print ( num1 , num2 )
    
elif num1 < num2 or num1 == num2 :
    print ( num2, num1 )
    
twenty= int(input("Enter the number 20 "))

if twenty != 20 :
    print ("Incorrect answer ")
    
elif twenty == 20 :
    print ("Thank you")
    
#range
while True:
    number = int(input("Enter a number between 10 and 20: "))
    if 10 <= number <= 20:
        print("Thank you!")
        break
    else:
        print("Incorrect. Please enter a number between 10 and 20.")
        
#colour
#colour = input("What is your favourite colour? ")
 #   if colour == "red" :
 #   print ( "i like red too" )
        


