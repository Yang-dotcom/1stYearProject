# Write a program that reads an integer and displays, using asterisks, a square and a filled diamond
# of the given side length. For example, if the side length is 4, the program should display:
# ****
# ****
# ****
# ****
#   *
#  ***
# *****
# *******
# *****
#  ***
#   *
sideLength = int(input("enter the side length: "))
#square
for i in range (sideLength):
    for j in range (sideLength):
        print("*", end = "")
    print()
#diamond
for i in range (1, sideLength + 1, 1):
    print("." * (sideLength - i) + "*" * (2 * i - 1))

for j in range (sideLength - 1, 0, -1):
    print(("." * (sideLength - j)) + ("*" * (2 * j - 1)))


