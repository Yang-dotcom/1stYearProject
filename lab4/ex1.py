# Write programs that read a sequence of integer inputs and print
# a. The smallest and largest of the inputs.
# b. The number of even and odd inputs.
# c. Cumulative totals. For example, if the input is 1 7 2 9, the program should print
# 1 8 10 19.
# d. All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2, the
# program should print 3 5 6.

digit = False
number = int(input("insert an integer number, type -1 o stop: "))
listNumber = []
while not digit:
    if not number == -1:
        listNumber.append(number)
        number = int(input("insert an integer number, type -1 o stop: "))
    elif number == -1:
        digit = True

#[a]
maxInteger = max(listNumber)
minInteger = min(listNumber)
print(f"the max is {maxInteger}, the min is {minInteger}")

#[b]
even = []
odd = []
for i in listNumber:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(f"the number of even numbers is {len(even)}, and the number of odd numbers is {len(odd)}")
print()
#[c]
sum_ = 0
for i in listNumber:
    sum_ += i
    print(f"|{sum_}|", end = "")
print()
#[d]
listAdjacentDuplicates = []
for e in range (len(listNumber) - 1 , 0, -1):
    if listNumber[e] == listNumber[e - 1] and listNumber[e] not in listAdjacentDuplicates:
        listAdjacentDuplicates.append(listNumber[e])
print(listAdjacentDuplicates[::-1])




