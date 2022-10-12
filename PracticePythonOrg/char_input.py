"""Practice python beginner exercises: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html"""

"""Exercise 1, Create a program that asks the user to enter their name and their age. Print out a message addressed to 
them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the 
previous message. (Hint: order of operations exists in Python)

Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)"""

name = input("What is your name? ")
age = int(input("What is your age rounded to the nearest whole number? "))
current_year = 2022
print_multiplier = int(input("How many times would you like the message to be printed to you? "))

year_to_100 = current_year - age + 100

print(f"Hello {name}, while you may be young now, in the year {year_to_100},"
      f" you will be 100 years old!\n" * print_multiplier)

