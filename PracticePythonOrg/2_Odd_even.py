"""The exercise comes first (with a few extras if you want the extra challenge or want to spend more time),
followed by a discussion. Enjoy!

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

num_input = int(input("Please give me a number: "))
check = int(input("Please give me a second number: "))

if num_input % check == 0:
    print("The second number divides evenly into the first number.")
elif num_input % 4 == 0:
    print("The number you have given me is divisible by 4.")
elif num_input % 2 == 0:
    print("The number you have given me is even.")
else:
    print("The first number you have given me is odd.")
