"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell
them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons
from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

random_num = random.randint(1,9)

game_on = True

while game_on:
    print("I'm thinking of a number between 1 and 9. Can you guess what it is?\n"
          "If you'd like to quit instead, you can type 'exit' at any point. ")
    guesses = 0

    while True:
        guess_num = input("")

        if guess_num == "exit":
            game_on = False
            print(f"You have chosen to quit. Good-bye.")
            break
            game_on = False

        if int(guess_num) == random_num:
            print(f"You guessed the random number. It was {random_num}. It took you {guesses} tries.\n")
            break

        elif int(guess_num) < random_num:
            print(f"My number is higher than what you guessed. Guess again.")
            guesses += 1

        else:
            print(f"My number is lower than what you guessed. Guess again.")
            guesses += 1