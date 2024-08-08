import random
import os

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = False

    while player not in choices:
        player=input("rock,paper or scissors:").lower()

    print("Computer\'s choice:",computer)
    print("Your choice:",player)

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!")
        if computer == "scissors":
            print("You won!!")
    elif player == "scissors":
        if computer == "rock":
            print("You lose!")
        if computer== "paper":
            print("You won!!")
    elif player == "paper":
        if computer == "scissors":
            print("You lose!")
        if computer == "rock":
            print("You won!!")

    play_again=input("Play again(yes/no):").lower()
    if play_again != "yes":
        break
    else:
        os.system("cls")

print("BYE!!!")
