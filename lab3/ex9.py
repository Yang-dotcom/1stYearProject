# A supermarket rewards its customers with shopping vouchers whose amount depends
# on the amount of money spent on groceries . For example, if you spend $50, you get
# a shopping voucher equal to eight percent of that amount. The following table shows
# the percentage used to calculate the voucher for different amounts. Write a program
# that calculates and displays the value of the shopping voucher delivered to the
# customer, based on the amount of money they spent on the purchase of food
# products. [P3.40]
# Money spent Percentage of the voucher
# Less than $10 |No coupons
# From $10 to $ 60 |8%
# More than $60 to $150 |10%
# More than $150 to $210 |12%
# More than $210 |14%

expense = int(input("Enter amount spent: "))
listBrackets = [[x for x in range(10)], [x for x in range(10, 61)], [x for x in range(61, 151)], [x for x in range(151, 211)], [x for x in range(211, 1001)]]
listCoupon = ["", 0.08, 0.1, 0.12, 0.14]
expIndx = 0
tax = 0

if expense > 1000:
    expIndx = 4

for i in listBrackets:
    if expense in i:
       expIndx = listBrackets.index(i)
print(f"Your expense is {expense}\u20ac, therefore you get a {listCoupon[expIndx] * expense}\u20ac discount, bringing the total to {expense - listCoupon[expIndx] * expense }\u20ac")
