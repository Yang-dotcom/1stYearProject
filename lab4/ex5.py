# Prime numbers. Write a program that prompts the user for an integer and then prints
# out all prime numbers up to that integer. For example, when the user enters 20, the
# program should print
# 2
# 5
# 7
# 11
# 13
# 17
# 19
# Recall that a number is a prime number if it is not divisible by any number except 1 and itself.

number = int(input("enter an integer: "))
notPrime = False
n = 2
for i in range (2, number):
    n = 2
    while not notPrime and n < i:
        if i % n == 0:
            notPrime = True
        n += 1
    else:
        if not notPrime:
            print(i, end=" ")
    notPrime = False








