# the code till line 31 is not correct for this exercise. it is because of a misinterpretation of the request.
# status = input("enter your marital status as either married or unmarried: ").lower()
# taxableIncome = int(input("enter your taxable income: "))
# unmarriedTaxableIncome = [[m for m in range(8001)], [m for m in range(8001, 32001)], [m for m in range(32001, 100000)]]
# unmarriedTax = [[0.1, 1], [800, 0.15], [4400, 0.25]]
# marriedTaxableIncome = [[m for m in range(0, 16001)], [m for m in range(16001, 64001)], [m for m in range(64001, 100000)]]
# marriedTax = [[0, 0.1], [1600, 0.15], [8800, 0.25]]
#
#
# def calculator():
#     if status == "married":
#         for list in marriedTaxableIncome:
#             if taxableIncome in list:
#                 indexTax = marriedTaxableIncome.index(list)
#         if taxableIncome > 100000:
#                 indexTax = 2
#         tax = marriedTax[indexTax][0] + taxableIncome * marriedTax[indexTax][1]
#     elif status == "unmarried":
#         if taxableIncome > 100000:
#             indexTax = 2
#         for list in unmarriedTaxableIncome:
#             if taxableIncome in list:
#                 indexTax = unmarriedTaxableIncome.index(list)
#         tax = unmarriedTax[indexTax][0] + taxableIncome * unmarriedTax[indexTax][1]
#     elif status != "married" or status != "unmarried":
#         retry = input("invalid status. do you wish to retry? press y/n").upper()
#         if retry == "Y":
#             calculator()
#     print("your tax is : \u20ac", tax)
#
# calculator()


taxableIncome = int(input("insert taxable income: "))
maritalStatus = input("are you married? (y/n)").lower()
statusBoolean = maritalStatus == "y"
umThreshold1 = 8e3
umThreshold2 = 32e3
mThreshold1 = 16e3
mThreshold2 = 64e3
tax = 0

if not statusBoolean:
    if taxableIncome <= umThreshold1:
        tax = 0.1 * taxableIncome
    elif taxableIncome <= umThreshold2:
        tax = 8e2 + 0.15 * (taxableIncome - umThreshold1)
    elif taxableIncome > umThreshold2:
        tax = 44e2 + 0.25 * (taxableIncome - umThreshold2)

if statusBoolean:
    if taxableIncome <= mThreshold1:
        tax = 0.1 * taxableIncome
    elif taxableIncome <= mThreshold2:
        tax = 16e2 + 0.15 * (taxableIncome - mThreshold1)
    elif taxableIncome > mThreshold2:
        tax = 88e2 + 0.25 * (taxableIncome - mThreshold2)

print(f"your tax is {tax}")
