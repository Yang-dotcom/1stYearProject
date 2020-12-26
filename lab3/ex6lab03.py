number = [4, 3, 2, 1, 0]
decimalValues = [0.0, 0.3, 0.7, 0.9]
gradeLetter = ["A", "B", "C", "D", "F"]
gradeList = []
maxGradelist = int(input("How many grades have you got? "))
for element in range(maxGradelist):
    grade = float(input("enter your grades starting from 0.0 to 4.0: "))
    gradeList.append(grade)

gradeAverage = sum(gradeList) / maxGradelist
intGradeAverage = int(gradeAverage)
decimalGradeAverage = gradeAverage % 1
if decimalGradeAverage < (decimalValues[0]+decimalValues[1]) / 2:
  sign = ""
elif (decimalValues[0]+decimalValues[1]) / 2 < decimalGradeAverage < (decimalValues[1]+decimalValues[2]) / 2:
  sign = "+"
#is the collapse of the two intervals
# #elif  (decimalValues[0]+decimalValues[1]) / 2 < decimalGradeAverage <= decimalValues[1]:
  #sign = "+"
#elif decimalValues[1] < decimalGradeAverage < (decimalValues[1]+decimalValues[2]) / 2:
  #sign = "+"
elif (decimalValues[1]+decimalValues[2]) / 2 <= decimalGradeAverage < (decimalValues[2] + decimalValues[3]) / 2:
  sign = "-"
  intGradeAverage += 1
#is the collapse of the two intervals
# elif (decimalValues[1]+decimalValues[2]) / 2 <= decimalGradeAverage <= decimalValues[2]:
#   sign = "-"
#   intGradeAverage += 1
# elif decimalValues[2] < decimalGradeAverage < (decimalValues[2] + decimalValues[3]) / 2:
#   sign = "-"
#   intGradeAverage += 1
elif (decimalValues[2] + decimalValues[3]) / 2 <= decimalGradeAverage <= decimalValues[3]:
  intGradeAverage += 1
  sign = ""
else:
  sign = ""
indexGradeAverage = number.index(intGradeAverage)
print(gradeLetter[indexGradeAverage]+sign)
