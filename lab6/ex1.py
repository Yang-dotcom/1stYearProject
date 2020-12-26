# Write the function:
# def countVowels(string)
# which returns the number of vowels in the string string . The vowels are the
# letters a, e, i, o and u, in addition to their respective capital versions. [P5.6]

def main ():
    string_ = input("Enter string here: ").lower()
    print(f"the number of vowels in the entered string is {countVowels(string_)}")



def countVowels(string_):
    numVowels = 0
    for i in string_:
        if i in "aoeiu":
            numVowels += 1
    return numVowels


if __name__ == '__main__':
    main()
