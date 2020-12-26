
grade = input("write if you got A, B, C, D, or F as your grade (please include + or - after the Grade if there is any): ").upper()
if grade[0] == "A":
    num = 4.0
elif grade[0] == "B":
    num = 3.0
elif grade[0] == "C":
    num = 2.0
elif grade[0] == "D":
    num = 1.0
elif grade[0] == "F":
    num = 0.0
if len(grade) > 1 and grade[0] != "F":
    if grade[1] == "+" and grade[0]!= "A":
        num += 0.3
    else:
        num -= 0.3
print(num)
