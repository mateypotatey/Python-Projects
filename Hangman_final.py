import random

word_list = ["Magma", "House", "School", "Parent", "Trivial", "Leopard", "Mouse", "Guess", "Immunology", "Hippopotamus", "Giraffe"]


guess_limit = 5
no_of_guesses = 0
secret_word = random.choice(word_list).lower()
hidden_word = ""
shown_word = ""
guess = ""
guess_list = []

for letter in secret_word:
    hidden_word = hidden_word + "_"

print("Your word is: " + hidden_word + ". There are " + str(len(secret_word)) + " letters in your word.")

shown_word = list(hidden_word)

while no_of_guesses != guess_limit and guess != secret_word and shown_word != secret_word:
    guess = input("Enter a letter or word: ").lower()

    position = ([pos for pos, char in enumerate(secret_word) if char == guess])  # cycles through the word and adds the position of a found letter to the list. called list comprehension method
    # print("You have chosen the letter " + guess + " which is found in position " + str(position))

    if guess in guess_list:
        print("\nYou've already guessed this letter. Try another one.")

    elif guess.isnumeric():
        print("\nThis is a number, not a letter. Try again.")

    elif guess not in secret_word:
        guess_list.append(guess)
        no_of_guesses = no_of_guesses + 1
        print("This letter was not in the word. Try another letter. ")

    else:
        guess_list.append(guess)
        if guess == secret_word:
            print("Congratulations, you guessed the secret word: " + secret_word)

        elif len(position) > 1:
            i = 0
            while i < len(position):
                shown_word = list(shown_word)
                new_position = int(position[i])  # need to have the position of the integer as 0. The problem is when there is two positions... Then I need to loop through it. Maybe an if statement?
                shown_word[new_position] = guess
                i = i + 1

        else:
            shown_word = list(shown_word)
            position = int(position[0])
            shown_word[position] = guess

    shown_word = "".join(shown_word)
    print("\n" + shown_word)

    if no_of_guesses < guess_limit and guess != secret_word and shown_word != secret_word:
        print("\nNumber of wrong guesses so far: " + str(
            no_of_guesses) + "\nYou have guessed the following letters so far: " + str(guess_list) + "\n")
    #  print(*guess_list, sep = ", ")

    elif shown_word == secret_word:
        print("Congratulations, you guessed the secret word: " + secret_word)

    elif no_of_guesses == guess_limit:
        print("\nYou have guessed the following letters: " + str(guess_list) + "\n\nBUT YOU DID NOT GUESS THE WORD AND ARE OUT OF GUESSES. YOU LOSE.")
