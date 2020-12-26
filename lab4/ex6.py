# Write a program that reads a word and prints all substrings, sorted by length. For example, if the
# user provides the input "rum", the program prints:
# r
# u
# m
# ru
# um
# rum
listName = []
name = input("insert word: ")
for i in range (0, len(name)):
    for j in range (len(name)):
        if i < len(name) and name[i:j+1] != "":
            listName.append(name[i:j+1])
listName.sort(key = len)
print(listName)
