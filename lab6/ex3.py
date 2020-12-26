# Write a function:
# def find(string , match)
# that checks whether the match string is contained in the string:
# b = find("Mississippi", "sip") # Assigns true to b [P5.17]
# Hint: try to write the code to search in the string by
# yourself.

def main():
    string_ = input("Enter string: ")
    match = input("Enter match string: ")
    print(findSub(string_, match))

# def findSub(string_, match):
#     b = string_.lower().find(match.lower())
#     if b != -1:
#         return True
#     return False
def findSub(string_, match):
    for i in range(len(string_)):
        if string_[i:i+len(match)] == match: # here we discovered that we can slice out of the max index of the string
            return True
    return False

if __name__ == '__main__':
    main()
