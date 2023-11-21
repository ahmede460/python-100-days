import random
import blackjackart

# Cards List
cards = [11, 2, 3, 4, 5, 6, 8, 9, 10, 10, 10, 10]

# Conditions

endofgame = False
choice2 = "Y"
computer = 0
player = 0

# Welcome Message
print(blackjackart.logo)

choice1 = input("Welcome to Black Jack, type 'Y' to start :  ")

player += random.choice(cards)

computer =+ random.choice(cards)


while choice2 == "Y" and endofgame == False:

    print(f"You have {player}  \n")
    print(f"The computer has {computer} and a hidden card")
        
    choice2 = input("Type 'Y' to pull another card , type 'N' to reveal the dealer's card :   ")

    if choice2 == "Y":
        player += random.choice(cards)
        if player > 21:
            print(f"You have {player} you lose")
            endofgame = True
    elif choice2 == "N":
        while computer < 17:    
            pull = random.choice(cards)
            print(f"computer pulled {pull}")
            computer += pull
            if computer > 21:
                print(f"Computer have {computer} you win")
                endofgame = True
if endofgame == False:
    if player == computer:
        print(f"You have {player} and the dealer has {computer} it's a draw")
    elif player > computer:
        print(f"You have {player} and the dealer has {computer} you win")
    elif computer > player:
        print(f"You have {player} and the dealer has {computer} you lose")

