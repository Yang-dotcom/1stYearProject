year = int(input("enter year: "))
if year > 1582 and year % 4 ==0 and year % 100 != 0 or year % 400 == 0 and year > 1582:
    print("it's a leap year, i.e. a day with 366 days")
else:
    print("not leap year")
