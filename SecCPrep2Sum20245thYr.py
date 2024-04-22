# user enters two numbers 
num1 = int(input ("Enter a number : "))
num2 = int(input ("Enter a second number : "))
choice = input( " If you want to add enter 'A' , To subtract enter 'S'")
A = ( num1 + num2 )
a = ( num1 + num2 )

if choice == 'A' :
    print( "By adding" , num1, "and" , num2 , "=", A )
    
if choice == 'a' :
    print( "By adding" , num1, "and" , num2 , "=", A )
    
s = ( num1 - num2 )
S = ( num1 - num2 )

if choice == 's':
    print("By subtracting" , num1, "and" , num2 , "=", s )
    
if choice == 'S':
    print("By subtracting" , num1, "and" , num2 , "=", S )
   
if choice == 'W' or choice == 'w' :
    print ("INVALID OPTION")



