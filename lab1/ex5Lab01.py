def sumNumbersMe ():
    endNumber = 10
    print("The sum of the first", endNumber, "from 1 is", (endNumber*(endNumber+1))/2)
    return

def sumNumberNech ():
    num = int(input("Up to what number do you want to sum ?"))
    summation = sum(x for x in range(0, num+1))
    print("the sum is:",summation)
    return
sumNumberNech()


print(int("32"))
