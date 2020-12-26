# Write a program that converts a Roman numeral, such as MCMLXXVIII,
# into its decimal representation. Tip: First, write a function that returns the
# numerical value of each single letter, then use the following algorithm:
# total = 0
# As long as the string s containing the Roman numeral is not empty
# If value(first character of s) is at least equal to value(second
# character of s) or s has length 1
# Add value( first character of s) to total.
# Delete the first character of s.
# Otherwise
# Add the difference value(second character of s) - value(first
# character of s) to the total
# Delete the first and second characters of s.
# [P5.27]

def main():
    romaLetters = input("Enter a Roman numeral: ").upper()
    print(f"the total is: {algRoma(romaLetters)}")

def converter(romaLetters):
    dictRoma = {"M" :1e3, "D" :5e2, "C" :1e2, "L" :50, "X" :10, "V": 5, "I" :1}
    return dictRoma[romaLetters]

def algRoma(romaLetters):
    total = 0
    listRoma = list(romaLetters)
    if romaLetters.isalpha():
        for c in range(len(listRoma)):
            if len(listRoma) == 1 or converter(romaLetters[c:c+1]) >= converter(romaLetters[c+1:c+2]):
                total += converter(listRoma[0])
                listRoma.remove(listRoma[0])
            else:
                total += converter(romaLetters[1]) - converter(romaLetters[0])
                del listRoma[0:2]
    return total


if __name__ == '__main__':
    main()

