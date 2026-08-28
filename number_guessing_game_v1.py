# Number Guessing Game using a higher or lower system

import random

num = random.randint(1,100)
guesses = 1
low_guess = 0
high_guess = 101

print(f"-------------Welcome to the Number Guessing Game-------------")

while True:
    try:
        guess = int(input("What is your initial guess, a number between 1 and 100: "))
        guesses += 1
        if guess < 1 or guess > 100:
            print("You must enter an integer between 0 and 101. ")
        else:
            break


    except ValueError:
        print(f"Please enter a valid integer.")

while guess != num:
    if guess < num and guess > low_guess:
        low_guess = guess
        print(f"Incorrect. The number is between {low_guess} and {high_guess}.")

    elif guess > num and guess < high_guess:
        high_guess = guess
        print(f"Incorrect. The number is between {low_guess} and {high_guess}.")
    else:
        print(f"Incorrect. Remember the number is between {low_guess} and {high_guess}. I wouldn't guess outside this range :).")
    while True:
        try:
            guess = int(input("What is your next guess: "))
            guesses += 1
            if guess < 1 or guess > 100:
                print("You must enter an integer between 0 and 101.")
            else:
                break

        except ValueError:
            print(f"Please enter a valid integer.")


print(f"Congratulations, you guessed the number {num} correctly in {guesses} guesses!")


