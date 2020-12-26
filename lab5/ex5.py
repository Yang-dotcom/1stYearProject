# In a predator-prey simulation, you compute the populations of predators and prey,
# using the following equations:
# preyn+1 = preyn × (1 + A – B × predn)
# predn+1 = predn × (1 – C + D × preyn)
# Here, A is the rate at which prey birth exceeds natural death, B is the rate of
# predation, C is the rate at which predator deaths exceed births without foodm and D
# represents predator increase in the presence of food. Write a program that prompts
# users for these rates, the initial population sizes, and the number of periods. Then
# print the populations for the given number of periods. As inputs, try A = 0.1, B = C =
# 0.01, and D = 0.00002 with initial prey and predator populations of 1,000 and 20.
# [P4.36]

A = float(input("Enter rate at which the prey birth exceeds natural death: "))
B = float(input("Enter rate of predation: "))
C = float(input("Enter the rate at which predator deaths exceed births without food: "))
D = float(input("Enter predator increase in the presence of food: "))
popPray = int(input("Enter population of prays: "))
popPred = int(input("Enter population of predators: "))
periods = int(input("Enter number of periods: "))

for i in range (periods):
    popPrayNext = popPray * (1 + A - B * popPred)
    popPredNext = popPred * (1 - C + D * popPray)
    popPray = popPrayNext
    popPred = popPredNext
    print(f"P{i}: preys = {int(popPray)}, predators = {int(popPred)}")
