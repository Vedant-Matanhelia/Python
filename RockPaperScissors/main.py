# This is a simple command line rock paper scissors.

import random
def game():
    choices = ['rock', 'paper', 'scissors']
    compPoints = 0
    playerPoints = 0


    while any([compPoints, playerPoints]) <= 10:
        playerChoice = input("What do u chose (rock, paper, scissors)? : ")
        compChoice = random.choice(choices)

        if playerPoints == 10:
            print("YOU WON THE GAME")
            break
        elif compPoints == 10:
            print("THE COMPUTER WINS THE GAME")
            break
        else:
            if playerChoice not in choices:
                print("Invalid Choice")
                print("Choose again")
                continue
            if (playerChoice == "rock" and compChoice == "scissors") or (playerChoice == "paper" and compChoice == "rock") or (playerChoice == "scissors" and compChoice == "paper"):
                print(f"Computer chose: {compChoice}")
                print("You win.")
                playerPoints += 1
            elif playerChoice == compChoice:
                print(f"Computer chose: {compChoice}")
                print("Draw")

            else:
                print(f"Computer chose: {compChoice}")
                print("Computer wins")
                compPoints += 1

if __name__ == "__main__":
    game()
    while input("Do you want to play again (y for yes, n for no): ").lower() == 'y':
        game()