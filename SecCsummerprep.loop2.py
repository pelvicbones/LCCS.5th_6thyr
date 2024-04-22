#fName = input("Enter a name")
#sName = input ("Enter a surname")

while True :
    print ("running while loop...")
    check = input ("Do you want to continue the loop? ")
    if check in ("Y" , "y"):
        fName = input("Enter a name ")
        sName = input ("Enter a surname ")
        print ("continuing loop" , fName , sName )
    else:
        break 