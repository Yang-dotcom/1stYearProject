month = int(input("write month in number from 1 to 12: "))
day = int(input("write day in number from 1 to 31: "))

if month == 1 or month == 2 or month == 3:
    season = "Winter"
elif month == 4 or month == 5 or month == 6:
    season = "Spring"
elif month == 7 or month == 8 or month == 9:
    season = "Summer"
elif month == 10 or month == 11 or month == 12:
   season = "Fall"

if month % 3 == 0 and day >= 21:
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Fall"
    else:
        season = "Winter"
print(season)
