import random


# Create a list of 100
listof100 = []
for num in range (1,101):
    listof100.append(num)

# Conditions
endofgame = False
lives = 0

#Function to check the random number
def checkrandomnumber(guess):
    global randomnumber
    global endofgame
    global lives
    if guess == randomnumber:
        print(f"You Win, the correct number is {guess}")
        endofgame = True
    elif guess > randomnumber:
        print("Too High!")
        lives -=1
    elif guess < randomnumber:
        print("Too Low!")
        lives -=1


# Select a random number
randomnumber = random.choice(listof100)


gamelevel = input("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100 \n Choose a difficulty. Type 'easy' or 'hard' : ").lower()


if gamelevel == "easy":
    lives = 10
elif gamelevel == "hard":
    lives = 5

print(f"You chose {gamelevel}, you have {lives} lives")

while endofgame == False:
    userguess = int(input("Make a guess : "))
    checkrandomnumber(userguess)
    if lives == 0:
        print(f"You lost the correct number was {randomnumber}")
        endofgame = True

    elif lives > 0 and endofgame == False:
        print(f"You have {lives} remaining")

playagain = input("if you want to play again type 'Y' : ").lowerl

#if playagain == "y"