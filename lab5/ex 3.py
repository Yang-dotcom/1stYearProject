# Factoring of integers. Write a program that asks the user for an integer and then
# prints out all its factors. For example, when the user enters 150, the program should
# print:
# 2
# 3
# 5
# 5
# [P4.16]
number =  int(input("Enter integer: "))

# for n in range (2, number, 1):
#     if number != 1:
#         while number % n == 0:
#            print(n)
#            number = number // n   #we use // instead of / bc with / we would get a float number x.0, which occupies more memory than an integer number

## with while loops: [it is more optimized because it has less checks to do]
factor = 2
while factor <= number:
    if number % factor == 0:
        print(factor)
        number //= factor
    else:
        factor += 1
 
