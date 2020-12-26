# A supermarket wants to reward its best customer of each day, showing the
# customer’s name on a screen in the supermarket. For that purpose, the customer’s
# purchase amount is stored in a list and the customer’s name is stored in a
# corresponding list. Implement a function nameOfBestCustomer(sales, customers)
# that returns the name of the customer with the largest sale. Write a program that
# prompts the cashier to enter all prices and names, adds them to two lists, calls the
# function that you implemented, and displays the result. Use a price of 0 as a sentinel.

def main():
    customers = []
    sales = []
    flag = False
    while not flag:
        c = input("Enter customer name (0 to end): ")
        b = int(input("Enter purchase amount of customer (0 to end): \u20ac "))
        if b != 0:
            sales.append(b)
            customers.append(c)
        else:
            flag = True
    print(f"the customer that spent the most is {nameOfBestCustomer(sales, customers)[0][0]} with this amount: {nameOfBestCustomer(sales, customers)[0][1]}")


def nameOfBestCustomer(sales, customers):
    tubList = sorted(zip(customers, sales), key= lambda tup: tup[1], reverse= True)
    print(tubList)
    return tubList

if __name__ == '__main__':
    main()



