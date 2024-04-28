import random

num = random.randint (1, 100)
print ( num)
fruit = random.choice (["bananna" , "strawberry" , "mango" , "lychee" , "starfruit"])
print ( fruit)

ht = random.choice ([ "t" , "h" ])
user = input(" heads (h) or tails (t) ? ")

if user == ht:
    print("you win")
elif user != ht :
    print ("you lose")
    
print ( " the answer was" , ht)
###
num1 = random.randint (1,5)
user1 = int(input("Pick a number between 1-5 "))
if num1 == user1 :
    print ("well done !")
    
elif num1 < user1:
    print ("number too high, Try again : ")
    chance1 =input("enter a second number ")
    if chance1 == num1 :
        print("you win")
    else:
        print ("you lose")
    
elif num1 > user1 :
    print ("number too low , Try again : ")
    chance2 = input("enter a second number ")
    if chance2 == num1 :
        print ("you win")
    else :
        print ("you lose")
    
    
###

while True:
    num2 = random.randint(1, 10)
    user2 = int(input("Enter a number between 1 to 10: "))

    if num2 == user2:
        print("You win!")
        break
    elif num2 > user2 :
        print ("number too low ")
        
    elif num2 < user2 :
        print ("number too high ")

    