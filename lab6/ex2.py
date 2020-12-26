# Write the function:
# def countWords(string)
# which returns the number of words in the string. Words are sequences of
# characters separated by spaces. For example,
# countWords("Mary had a little lamb")
# returns 5. [P5.7]

# def main():
#     string_ = input("Enter string: ")
#     print(f"The entered string has {countWords(string_)} words")
#
# def countWords(string_):
#     listWords = string_.split()
#     return len(listWords)
#
# if __name__ == '__main__':
#     main()
# string_ = input('enter string: ')
#
# def countWords(string_):
#   parole = 1
#   for i in string_:
#     if string_.startswith(' '):
#       parole = 1
#     if string_.endswith(' '):
#       parole = 1
#     if i == ' ':
#       parole = parole + 1
#   return parole
#
# print(countWords(string_))
