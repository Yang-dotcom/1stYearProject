firstInteger = int(input("declare one integer:"))
secondInteger = int(input("declare a second integer"))

def resultOperations ():
    print(" The sum is ", firstInteger + secondInteger,
    "\n the difference is ", firstInteger - secondInteger,
    "\n the product is ", firstInteger * secondInteger,
    "\n the average is ", (firstInteger + secondInteger) / 2, #result of division with single / is always float points
    "\n the distance is ", abs(firstInteger - secondInteger),
    "\n the max is ", max(firstInteger,secondInteger), #doable with if else function
    "\n the min is ", (firstInteger , secondInteger))
    return



resultOperations()
