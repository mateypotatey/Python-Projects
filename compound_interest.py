# Compound interest calculator where you can see how much your investment grows, given a certain starting balance

def compound_interest_calculator():
    while True: 
        try:
            principal = int(input("Enter the balance of your principal amount, rounded to the nearest dollar: "))
            break
        except ValueError:
            print("This is not a valid number. Please enter a valid starting amount, rounded to the nearest dollar.\n")

    while True:
        try:
            interest_rate = float(input("Enter the interest rate for your balance: "))
            break
        except ValueError:
            print("This is not a valid number. Please enter a valid interest rate.\n")

    while True:
        try:
            years_invested = int(input("Enter the number of years you'd like to invest your balance (in whole years): "))
            break
        except ValueError:
            print("This is not a valid number. Please enter a valid number of years, rounded to a full year.\n")

    while True:
        try:
            annual_contribution = int(input("Enter a number if you will be making an additional annual contribution: "))
            break
        except ValueError:
            print("This is not a valid number. Please enter a valid number, rounded to the nearest dollar.\n")

    balance = principal

    i = 0
    while i < years_invested:
        if annual_contribution == 0:
            balance = balance * (1 + interest_rate / 100)
            balance = float("{:.2f}".format(balance))
            i += 1
        else:
            balance = (balance + annual_contribution) * (1 + interest_rate / 100)
            balance = float("{:.2f}".format(balance))
            i += 1

    print(f"\nThe balance after {years_invested} year(s) will be {balance}.")

compound_interest_calculator()
