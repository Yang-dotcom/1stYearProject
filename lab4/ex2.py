# Write programs that read a line of input as a string and print
# a. Only the uppercase letters in the string.
# b. Every second letter of the string.
# c. The string, with all vowels replaced by an underscore.
# d. The number of digits in the string.
# e. The positions of all vowels in the string

#input
line = input("please enter the line: ")
#algorithms a, b, c, d, e
#[a]
element = 0
while element < len(line):
    if line[element].isupper():
        print(line[element], end = "")
    element += 1

print()
#it is also possible to do this w/out the python function .upper(); one such example would be uscing Lexicographic order;
#another way would be comparing the ASCII value of the letters.

# while element <= len(line)
#     hex_value = ord(line[element]) #the function ord converts element to its equivalent ASCII code #0x before the number is for hexadecimal base (base 16) instead of decimal
#     if hex_value >= 0x41 and hex_value <= 0x5A: #it's preferable not to use y<x<z notation, but instead x>y and x<z
#         print(line[element], end = "_")
#     element += 1

#it's also possible to solve it using a for function e.g.:
#for element in range (0, len(line), 1):
#   if line[element].isupper():
#       print(line[element], end = "") #it's not necessary to use the pointer element anymore since the for function reiterates over the next element in list range() by itself

#[b]
secondLetter = []
for element in range (0,len(line), 1):
    if line[element].isalpha():
        secondLetter.append(line[element])
for i in range (1, len(secondLetter), 2):
    print(secondLetter[i])


#the following solutions would've been doable if the exercise asked for every second character, but since it specified every second *letter*, they don't work.
# for element in range (0, len(line), 1): #EVERY second character means every alternate character
#     if element % 2 == 1:
#         print(line[element], end = "")
#another way to solve the ex. would be to take advantage of the range() which allows us to define the steps.s
#for element in range (1, len(line), 2):    #it starts with the second letter (1) and jumps to the next second letter (1+2 =3)
#   print(line[element], end= "")
print()
#[c]
# for element in range (0, len(line), 1): #this solution is fully explicit and very labour intensive.
#    if line[element].lower() == "a" or line[element].lower() == "e" or line[element].lower() == "i" or line[element].lower() == "o" or line[element].lower() == "u":
newLine = []
for element in range (0, len(line), 1):
    if line[element] in "aeiouAEIOU": #we check if the element exists in the universe which contains aeiouAEIOU
        newLine.append("_")             #we append the value "_" instead of the line[element] value, in the same index as line[element]
    else:
        newLine.append(line[element])   #we append the line[element] value in the list in the original index position
print(newLine, end = "")
print()
#[e] it's enough to insert into the if block in line 46 the subsequent code: ##print(line.index(line[element]), end = "")
#[d]
listDigits = []
for element in range (0, len(line), 1):
    if line[element].isdigit():     #it's also possible to do it in the same way as in ex 2a using ASCII comparison.
        listDigits.append(line[element])
print(len(listDigits))
