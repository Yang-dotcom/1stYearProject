
name = input("insert a message: ")
#stringhandling methods
if name.isalpha():
    print("the string contains only letters")
if name.isupper():
    print("the string contains only uppercase letters")
if name.islower():
    print("the string contains only lowercase letters")
if name.isdigit():
    print("the string contains only digits")
if name.isalnum():
    print("the string contains both digits and characters") #.isalnum checks if the string if all the characters in the string are alphanumeric, i.e. it contains both numbers and/or characters
if name[0] >= "A" and name[:-1] <= "Z":
    print("starts with a capital letter ")
if name.endswith("."):
    print("ends with a period")
