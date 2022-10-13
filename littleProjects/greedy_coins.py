"""Writing a coding solution for greedy coins like on CS50 problem in C.
For a given input of cents, print out the least number of change you will get (in number of coins)
1c = pennies, 5c = nickels, 10c = dimes, 25c = quarters."""

cents = int(input("Enter the number of cents to return to customer: "))

quarters = 0
dimes = 0
nickels = 0
pennies = 0

while cents >= 25:
    cents = cents - 25
    quarters += 1

while cents >= 10:
    cents = cents - 10
    dimes += 1

while cents >= 5:
    cents = cents - 5
    nickels += 1

while cents >= 1:
    cents = cents - 1
    pennies += 1

print(quarters + dimes + nickels + pennies)

