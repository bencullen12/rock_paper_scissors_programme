# version 3 of my rock paper scissors programme

import random
options = ("rock", "paper", "scissors")

print(f"---------------------------------------------------")
print(f"Welcome to the rock paper scissors game!")
print(f"It will be a best of 5 game with sudden death in the event of a tie!")
print("----------------------------------------------------")

def play_game():
    while True:
        your_choice = input("What's your move? Choose rock, paper or scissors: ").lower()
        if your_choice not in options:
            print(f"{your_choice} is an invalid input. Choose either rock, paper or scissors.")
            continue
        break
    opponent_choice = random.choice(options)

    if your_choice == opponent_choice:
        print(f"I threw {your_choice}. It's a tie!")
        return "tie"

    elif your_choice == "rock" and opponent_choice == "paper":
        print("I threw paper! You lose! Boo!")
        return "lose"

    elif your_choice == "rock" and opponent_choice == "scissors":
        print("I threw scissors. You win! Congrats!")
        return "win"

    elif your_choice == "paper" and opponent_choice == "rock":
        print("I threw rock. You win! Congrats!")
        return "win"

    elif your_choice == "paper" and opponent_choice == "scissors":
        print("I threw scissors! You lose! Boo!")
        return "lose"

    elif your_choice == "scissors" and opponent_choice == "rock":
        print("I threw rock! You lose! Boo!")
        return "lose"

    elif your_choice == "scissors" and opponent_choice == "paper":
        print("I threw paper. You win! Congrats!")
        return "win"

i = 0
your_score = 0
my_score = 0
tie = 0

while i < 5:
    outcome = play_game()

    if outcome == "lose":
        my_score += 1
    elif outcome == "win":
        your_score += 1
    else:
        tie += 1
    i += 1

print("-------------------------------------------------")
print(f"Your wins: {your_score}  "
      f"My wins: {my_score}  "
      f"Ties: {tie}  ")
print("-------------------------------------------------")

if your_score > my_score:
    print(f"Wow you beat me {your_score}:{my_score} congratulations!")
elif your_score < my_score:
    print(f"Ha I beat you {my_score}:{your_score} ")

while your_score == my_score:
    print("Sudden Death!")
    outcome = play_game()

    if outcome == "win":
        print("-------------------------------------------------")
        print("You win sudden death!!!")
        your_score += 1
    elif outcome == "lose":
        print("-------------------------------------------------")
        print("You lose sudden death! Unlucky soldier!")
        my_score += 1
    else:
        print("It's another tie! We must play again!")
        tie += 1




