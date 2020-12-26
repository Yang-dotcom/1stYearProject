TOTALPRICE = float(input("enter total book price in euro:"))
NUMBERBOOKS = int(input("enter number of books:"))

tax = 0.075 * TOTALPRICE

shippingCharge = 2 * NUMBERBOOKS

priceOfOrder = TOTALPRICE + tax + shippingCharge
print ("the price of the order is:", priceOfOrder)
