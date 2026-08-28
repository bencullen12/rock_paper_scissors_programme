# This is a rock paper scissors programme

import random
options = ("rock", "paper", "scissors")

print(f"---------------------------------------------------")
print(f"Welcome to the rock paper scissors game!")
i = 0

while i < 5:
    player_choice = input("What is your move? rock, paper, or scissors: ").lower()
    random_choice = random.choice(options)

    if player_choice == random_choice:
        print(f"I throw {player_choice}! It's a tie!")

    elif player_choice == "rock" and random_choice == "paper":
        print("I throw paper! You lose! Boo!")

    elif player_choice == "rock" and random_choice == "scissors":
        print("I throw scissors. You win! Congrats!")

    elif player_choice == "paper" and random_choice == "rock":
        print("I throw rock. You win! Congrats!")

    elif player_choice == "paper" and random_choice == "scissors":
        print("I throw scissors! You lose! Boo!")

    elif player_choice == "scissors" and random_choice == "rock":
        print("I throw rock! You lose! Boo!")

    elif player_choice == "scissors" and random_choice == "paper":
        print("I throw paper. You win! Congrats!")

    i += 1


