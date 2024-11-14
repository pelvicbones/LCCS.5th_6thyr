import random

# Generate a random number between 0 and 100 and print it
num = random.randint(0, 100)
print(num)

# Randomly select a fruit and print it
fruit = random.choice(["banana", "apple", "strawberry", "grapes", "blueberries"])
print(fruit)

# Coin toss game
h_t = random.choice(["h", "t"])
user = input("heads or tails? (enter 'h' or 't'): ")
if user == h_t:
    print("You win!")
else:
    print("Bad luck")
print("The answer was:", h_t)

# Number guessing game
num1 = random.randint(1, 5)
user1 = int(input("Pick a number between 1 and 5: "))

if user1 == num1:
    print("Well done!")
elif user1 > num1:
    print("Your number is too high")
elif user1 < num1:
    print("Your number is too low")

# Optionally, allow the user to enter a second number if they guessed wrong
if user1 != num1:
    user2 = int(input("Enter a second number: "))
    if user2 == num1:
        print("Well done!")
    else:
        print("Sorry, the correct number was:", num1)
        
# entering number until its right
pick= random.randint (1,10)
pickuser = int(input("enter a number between 1 and 10 "))

while pickuser != pick:
    if pickuser > pick:
        print("Your number is too high")
    else:
        print("Your number is too low")
    
    # Prompt for a new guess after feedback
    pickuser = int(input("Try again: "))

# When the correct guess is made, exit the loop
print("You win!")

#math quizz
count = 0
print ("MATH QUIZ 1")
math1 = random.randint (1,10)
math2 = random.randint (1,10)
add = math1 + math2
print (math1 , "+", math2 , "=")
ask = int(input())

if ask == add :
    count += 1
    
print ("QUESTION 2 ")
mult= math1*math2
print(math1, "x", math2 , "=")
ask2 = int(input())

if ask2 == mult:
    count += 1
    
print("QUESTION 3 ")
div= math1 / math2
print(math1, "div", math2 , "=")
ask4 = int(input())

if ask4 == div:
    count +=1
    
print ("QUESTION 4 ")
sub = math1 - math2
print (math1 , "-", math2, "=")
ask5= int(input())

if ask5== sub :
    count += 1
    
print ("QUESTION 5")
add1= math1 + math2
print(math1, "+", math2, "=")
ask6= int(input())

if ask6==add1:
    count +=1

    
print("RESULTS =")
print (count ,"/5")

#colour picking
colour = random.choice(["blue", "green", "red"])
guess= input("pick a colour")

while guess != colour :
    if guess == 'blue' :
        print ("well arent ya feelin blue")
        
    elif guess == 'green' :
            print ("green for broccoli")
            
    elif guess == 'red' :
            print ("red for apple")
            
else :
    print (" sorry thats not an option ")
    
guess2= input(" guess again")
print ("horray")
        
        



