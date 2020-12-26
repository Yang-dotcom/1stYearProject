# Write an application to pre-sell a limited number of cinema tickets. Each buyer can
# buy as many as 4 tickets. No more than 100 tickets can be sold. Implement a
# program that prompts the user for the desired number of tickets and then displays the
# number of remaining tickets. Repeat until all tickets have been sold, and then display
# the total number of buyers. [P4.33]

limit = 100
tcktBuyer = 4
i = 0
while limit > 0:
    buy = int(input("Enter how many tickets you want (the max is 4 per person): "))
    if buy <= tcktBuyer and buy <= limit:
        limit -= buy
        print(f"{limit} tickets are left.")
        i += 1
    else:
        print("You exceeded the max amount allowed or there aren't enough tickets. please choose again")
print(f"total number of buyers were {i}")


