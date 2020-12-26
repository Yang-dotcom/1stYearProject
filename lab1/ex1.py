def personalUseCar ():
    print("insert your starting mileage:")
    startMileage = int(input())
    print("insert your ending mileage:")
    endMileage = int(input())
    print("insert your distance in miles from home to work:")
    homeWorkDistance = int(input())
    print("insert your workdays:")
    workDays = int(input())
    personalUseFraction = ((endMileage-startMileage) - homeWorkDistance*workDays)*100/(endMileage-startMileage)
    print("The % of car used for personal use is", personalUseFraction)
    return
personalUseCar()
