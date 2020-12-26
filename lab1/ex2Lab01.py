def receipt ():
    print("what's the bill?")
    bill = int(input())
    print("how many of you ate?")
    nFriends = int(input())
    tipTotal = 0.15*bill
    tipSingle = tipTotal/nFriends
    totalCost = tipTotal + bill
    singleCost = totalCost / nFriends
    print("the bill is:", bill)
    print("the tip for the meal is:", tipTotal)
    print("the tip for a single person is:", tipSingle)
    print("the amount each has to pay is:", singleCost)
    return
receipt()
