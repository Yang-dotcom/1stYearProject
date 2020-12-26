# Write a unit conversion program that asks the user from which unit (choosing
# from: ml, l, g, kg, mm, cm, m, km ) and to which unit (choosing
# from: fl . oz , gal , oz , lb, in, ft , mi ) wants to make a conversion, rejecting
# incompatible conversions (such as, for example, gal → km ). Then ask the value to
# be converted and finally visualize the result [P3.26]:
# Convert from? gal
# Convert to? ml
# Value? 2.5
# 2.5 gal = 9463.5 ml
unit1 = input("insert unit to convert from: ").lower()
unit2 = input("insert unit to convert to: ").lower()
value = float(input("insert value to be converted: "))
#we express each unit in relation to a fundamental unit that we choose arbitrary. for example, if we choose m as the fund. unit for length, then every value shall be converted into 1 unit of m. (e.g: 1 m = 1e-3 mm = 1e-2 cm.
#to convert from mm to cm then we simply need to divide the unit you convert from by the unit you convert to.
#e.g: 1 mm = 0.1 cm, result of 1e-3 / 1e-2. (which is equal to saying what's the value X expressed in 1e-3 meters when I want it expressed in 1e-2 meters: to do so I multiply by 1e1 the unit 1e-3 to get unit 1e-2, and divide value by 1e1 according to basic a[gebra rules.
listCapacity = ["ml", "l", "fl . oz", "gal"]
capacityConvert = [1e3, 1, 33.814, 0.264172]    # expressed in relation to 1 l  # NB: we need 1000 ml to get 1 l, not 1e-3 ml
listWeigth = ["g", "kg", "oz", "lb"]
weightConvert = [1e3, 1, 35.274, 2.20462 ]  #expressed in relation to 1 kg
listLength = ["mm", "cm", "m", "km", "in", "ft", "mi" ]
lengthConvert = [1e3, 1e-2, 1, 1e3,39.3701, 3.28084, 0.000621371] #expressed in relation to 1 m

if unit1 and unit2 in listCapacity:
    value = ((capacityConvert[listCapacity.index(unit2)]) / capacityConvert[listCapacity.index(unit1)]) * value
    print(value)

if unit1 and unit2 in listWeigth:
    value = ((weightConvert[listWeigth.index(unit2)]) / weightConvert[listWeigth.index(unit1)]) * value
    print(value)

if unit1 and unit2 in listLength:
    value = ((lengthConvert[listLength.index(unit2)]) / lengthConvert[listLength.index(unit1)]) * value
    print(value)
















































#The code till line 48 is not ideal for this problem.
# listMetricName = [["ml", "l"], ["g", "kg"], ["mm", cm", "m", "km"]]
# listImperialName = [["fl . oz", "gal"], ["oz", "lb"], ["in", "ft", "mi"]]
# imperialToMetric = [[29.574, 3.785], [28.35, 0.4536], [2.54, 0.3048, 1.6093]]
# metricToImperial = [[0.033814, 0.264172], [28.3495, 0.453592], [2.54, 0.3048, 0.621371]]
# invertedValues = [[0.000264172, 33.814],[0.00220462,35.274], []
# unit1 = input("which unit do you want to you want to convert from? ")
# unit2 = input("which unit do you want to convert to? ")
# userValue = float(input("insert value to be converted "))
# def typeunit1():
#     for list1 in listMetricName:
#         if unit1 in list1:
#             indexUnit1 = listMetricName.index(list1)
#             unit1Boolean = 1
#             convertIndex1 = list1.index(unit1)
#     for list2 in listImperialName:
#          if unit1 in list2:
#             indexUnit1 = listImperialName.index(list2)
#             unit1Boolean = 0
#             convertIndex1 = list2.index(unit1)
#     return indexUnit1, unit1Boolean, convertIndex1
# def typeunit2():
#     for list3 in listMetricName:
#         if unit2 in list3:
#             indexUnit2 = listMetricName.index(list3)
#             convertIndex2 = list3.index(unit2)
#             unit2Boolean = 1
#     for list4 in listImperialName:
#         if unit2 in list4:
#             indexUnit2 = listImperialName.index(list4)
#             convertIndex2 = list4.index(unit2)
#             unit2Boolean = 0
#     return indexUnit2, convertIndex2, unit2Boolean
# indexUnit1, convertIndex1, unit1Boolean = typeunit1()
# indexUnit2, convertIndex2, unit2Boolean = typeunit2()
#
# if indexUnit1 == indexUnit2:
#     if unit1Boolean > unit2Boolean and convertIndex1 == convertIndex2:
#          convertedValue = userValue * metricToImperial[indexUnit1][convertIndex1]
#     elif indexUnit1 == indexUnit2 and unit2Boolean > unit1Boolean and convertIndex1 == convertIndex2:
#         convertedValue = userValue * imperialToMetric[indexUnit2][convertIndex2]
#     elif:
#     elif:
#     print(f"the converted value is: {convertedValue:.3f} {unit2}")
# else:
#     print("invalid pair of units")
# print(indexUnit1, convertIndex1, convertedValue)
# print(f"the converted value is: {convertedValue:.3f} {unit2}")





