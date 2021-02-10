## compact style code for homework about scores, assigned on 18/11/2020
# import random
#
# def main():
#   """Main Entry Point"""
#   scores = [random.randint(0, 30) for i in range(int(input("Enter number of scores: ")))]
#   return print(f"Initial scores: {scores}. Scores after removing lowest score {scores.pop(scores.index(min(scores)))}: {scores}. Average of new scores is {sum(scores)/len(scores)}")
#
# if __name__ == '__main__':
#   main()
#
#
# import random
# def main():
#   """Main Entry Point"""
#   numScores = int(input("Enter number of scores: "))
#   scores = getScores(numScores)
#   lowestRemList = getNewScores(scores)
#   average = getAverage(lowestRemList)
#   print(f"Initial scores: {scores}. Scores after removing lowest score: {lowestRemList}. Average of new scores {average}")
#   return
#
#
# def getScores(number):
#   """Return a list of random integers"""
#   listScores = []
#   for i in range(number):
#     listScores.append(random.randint(0, 30))
#   return listScores
#
#
# def getNewScores(listScores):
#   """Return a list without the lowest value"""
#   lowest = listScores[0]
#   for e in listScores:
#     if e < lowest:
#       lowest = e
#   newListScores = list(listScores)
#   newListScores.remove(lowest)
#   return newListScores
#
#
# def getAverage(listNewScores):
#   """Return the rounded average of a list"""
#   sum_ = 0
#   for i, e in enumerate(listNewScores):
#     sum_ += e
#   newNumScores = len(listNewScores)
#   average = sum_ / newNumScores
#   return round(average, 2)
#
# if __name__ == '__main__':
#     main()

# compute and print frequency of each die value.

#
# NUM_VALUES = 50000
# import random
# def main():
#     """Main entry point"""
#     dieValues = list()
#     for i in range(NUM_VALUES):
#         dieValues.append(random.randint(1,6))
#     leastCriticalValue = check(dieValues)
#     converter = {9.236: "90%", 11.070: "95%", 12.833: "97.5%", 15.086: "99%", 20.515: "99.9%"}
#     print(f"The dice is unbiased at {converter[leastCriticalValue]} significance level")
#
#
# def check(values):
#     """Check whether the dice is fair"""
#     # frequency = [0, 0, 0, 0, 0, 0]
#     #step 1: count results
#     # for r in values:
#     #     frequency[r-1] = frequency[r-1] + 1
#     ## start with pearson chi fairness test
#     frequency = []
#     for r in range(6):
#         frequency.append(((values.count(r+1) - NUM_VALUES / 6)**2) / NUM_VALUES / 6)
#     print(frequency)
#     b = sum(frequency) # sum of Pearson's cumulative test statistic
#     criticalValues = [9.236, 11.07, 12.833, 15.886, 20.515]
#     for i in criticalValues:
#       if b <= i:
#         return i
#
#     ## end pearson chi fairness test
#
#     #normalize:
#     # for f in range(len(frequency)):
#     #     frequency[f] = frequency[f] / len(values)
#     # check them
#     # expectedFrequency = 1/6
#     # acceptableError = 0.01
#     # allCorrect = True
#     # for f in frequency:
#     #     if abs(f - expectedFrequency) > acceptableError:
#     #         allCorrect = False
#     # return allCorrect
#
# if __name__ == '__main__':
#     main()

# def descending_order(num):
#     string_ = str(num)
#     lis1 = [int(x) for x in string_]
#     lis1.sort(reverse = True)
#     lis2 = [str(j) for j in lis1]
#     lis2_string = "".join(lis2)
#     lis2_integer = int(lis2_string)
#     return lis2_integer
#
# num = 3241513234
# print(descending_order(num))

##
# def filter_list(l):
#     lis = [x for x in l if isinstance(x, int)]
#     return lis
# l = [1,2,'a','b']
#
# print(filter_list(l))

# ##
# def to_camel_case(text):
#     lis = list(text)
#     for i, e in enumerate(lis):
#         if e == "-" or e == "_":
#             lis.remove(e)
#             lis[i] = lis[i].upper()
#     return "".join(lis)
# text = "the-stealth-warrior"
# print(to_camel_case(text))


