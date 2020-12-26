#numberRandom = str(input("declare a 5-digit integer number:"))

# print(numberRandom[0],
#       numberRandom[1],
#       numberRandom[2],
#       numberRandom[3],
#       numberRandom[4],
#       )

# for x in numberRandom:
#     print(x)
# the code above is not relevant to the exercise because it specifies integer, thus you can't convert it to string and print
# the characters
numberRandom = int(input("declare a 5-digit integer number:"))
numberRandomStr = str(numberRandom)
check1 = 0
list = []
while check1 < (len(numberRandomStr)):
    reminder = numberRandom % 10
    numberRandom = numberRandom // 10
    list.append(reminder)
    check1 = check1 + 1
print(list[::-1])
