# Write a function that calculates the balance of a bank account after a given
# number of years have elapsed, starting with a given initial balance and a
# given annual interest rate, crediting the interest annually. [P5.22

def main():
    inIncome = int(input("Enter intiial balance: "))
    rate = float(input("Enter interest rate in decimals: "))
    year = int(input("Enter elapsed years after which you want to check the total balance: "))
    print(f"your balance after{year} is {calculator(inIncome, rate, year)} \u20ac")

def calculator(inIncome, rate, year):
    for i in range (year):
        inIncome = inIncome * (1. + rate)
    return round(inIncome, 2)

if __name__ == '__main__':
    main()
