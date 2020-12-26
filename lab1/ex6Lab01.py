
initialBalance = int(input("Initial balance: "))
interestRate = float(input("interest rate % converted to decimals:"))
year = int(input("n of years later in which you want to check balance "))

def balanceOfAccount ():
    print("your balance years later", year, "is",initialBalance*((1+interestRate)**year))
    return
balanceOfAccount ()
