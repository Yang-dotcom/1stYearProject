# A non-governmental organization needs a program to calculate the share of
# financial aid to be allocated to each family in need of assistance. The
# formula is as follows:
# ● If the family's annual income is between $30,000 and $40,000 and the
# family has at least three children, the benefit is $1,000 for each child.
# ● If the family's annual income is between $20,000 and $30,000 and the
# family has at least two children, the benefit is $1500 for each child.
# ● If the family's annual income is less than $ 20,000, the benefit is
# $2,000 for each child.
# Write a function that does these calculations, then write a program that asks
# the user to provide the annual income and number of children of each
# family, displaying the corresponding value returned by the function. Use -1
# as the sentinel value to end data entry. [P5.28]

def main():
    flag = False
    while not flag:
        annInc = int(input("Enter annual income (enter -1 to end): "))
        if annInc != -1:
            child = int(indput("Enter number of children: "))
            print(f"the benefit you receive is {calcBen(annInc, child)} \u20ac")
        else:
            flag = True



def calcBen(annInc, child):
    condRich = 3e4 < annInc <= 4e4 and child >= 3
    condMiddle = 2e4 < annInc <= 3e4 and child >= 2
    condPoor = annInc <= 2e4
    benefit = 0

    if condRich:
        benefit = child * 1e3
    elif condMiddle:
        benefit = child * 15e2
    elif condPoor:
        benefit = child * 2e3
    return benefit


if __name__ == '__main__':
    main()
