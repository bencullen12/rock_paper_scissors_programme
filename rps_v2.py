# This is an updated rock paper scissors programme

import random
options = ("rock", "paper", "scissors")

print(f"---------------------------------------------------")
print(f"Welcome to the rock paper scissors game!")
print(f"It will be a best of 5 game with sudden death at the end!")
print("----------------------------------------------------")
i = 0
# adding in a count
your_wins = 0
opponent_wins = 0
tie = 0


while i < 5:
    player_choice = input("What is your move? rock, paper, or scissors: ").lower()
    if player_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    random_choice = random.choice(options)

    if player_choice == random_choice:
        print(f"I throw {player_choice}! It's a tie!")
        tie += 1

    elif player_choice == "rock" and random_choice == "paper":
        print("I throw paper! You lose! Boo!")
        opponent_wins += 1

    elif player_choice == "rock" and random_choice == "scissors":
        print("I throw scissors. You win! Congrats!")
        your_wins += 1

    elif player_choice == "paper" and random_choice == "rock":
        print("I throw rock. You win! Congrats!")
        your_wins += 1

    elif player_choice == "paper" and random_choice == "scissors":
        print("I throw scissors! You lose! Boo!")
        opponent_wins += 1

    elif player_choice == "scissors" and random_choice == "rock":
        print("I throw rock! You lose! Boo!")
        opponent_wins += 1

    elif player_choice == "scissors" and random_choice == "paper":
        print("I throw paper. You win! Congrats!")
        your_wins += 1

    i += 1

print("-------------------------------------------------")
print(f"Your wins: {your_wins}  "
      f"My wins: {opponent_wins}  "
      f"Ties: {tie}  ")
print("-------------------------------------------------")

if your_wins > opponent_wins:
    print("Congrats! You won this best of 5 match!")
elif your_wins < opponent_wins:
    print("Unlucky! I won this time!")
else:
    print("It's a tie! Time for sudden death")

while your_wins == opponent_wins:
    player_choice = input("What is your move? rock, paper, or scissors: ").lower()
    if player_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue
    random_choice = random.choice(options)

    if player_choice == random_choice:
        print(f"I throw {player_choice}! It's a tie again! Let's run it back!")
        tie += 1

    elif player_choice == "rock" and random_choice == "paper":
        print("I throw paper! I win overall come on!")
        opponent_wins += 1

    elif player_choice == "rock" and random_choice == "scissors":
        print("I throw scissors. You win the whole game!")
        your_wins += 1

    elif player_choice == "paper" and random_choice == "rock":
        print("I throw rock. You win the whole game!")
        your_wins += 1

    elif player_choice == "paper" and random_choice == "scissors":
        print("I throw scissors! I win the whole game let's go!")
        opponent_wins += 1

    elif player_choice == "scissors" and random_choice == "rock":
        print("I throw rock! I win the whole game let's go!")
        opponent_wins += 1

    elif player_choice == "scissors" and random_choice == "paper":
        print("I throw paper. You win overall!")
        your_wins += 1

print("-----------------------------------------------------")
if your_wins > opponent_wins:
    print("Congratulations! You won the game!")
else:
    print("Unlucky! I won the game!")

