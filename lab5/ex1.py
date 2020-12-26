# Write a program that reads in three strings and sorts them lexicographically.
# For instance:
# Enter a string: Charlie
# Enter a string: Able
# Enter a string: Baker
# Able
# Baker
# Charlie
strA = input("enter string: ")
strB = input("enter string: ")
strC = input("enter string: ")
## simple comparison one by one of the strings using multiple if statements and nested if statements.
# the comparison is between the ASCII values of the letters, where uppercase letters are before lowercase.
# the letters that appear first (uppercase) are lower value than those that appear later on (lowercase)
# if strC < strB:
#     if strB < strA:
#     else: #strB > strA
#         if strC > strA:
#         else: #strC < strA
# etc.etc..

## using lists
a = [strA, strB, strC]
b = sorted(a)   # creates a new list that sorts elements of list a without changing index order of a\
# if we want the reverse order (decreasing) we can do b = sorted(a, reverse = true)
# a.sort()    # using this function, the original order of elements in a is changed.
for s in b:
    print(s)
print(b)

