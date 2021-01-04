# Write a program that asks a user to type in two strings and that prints:
#  The characters that occur in both strings;
#  The characters that occur in one string but not the other;
#  The letters that do not occur in either string.
# Tip: Use set to turn a string into a set of characters. [ P 8.9 ]

STR_1 = input("Enter first string: ")
STR_2 = input("Enter second string: ")
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    str1_set = set(STR_1.upper())
    str2_set = set(STR_2.upper())
    print(f"characters that occur in both strings: {str1_set.intersection(str2_set)}")
    print(f"Characters that occur in str_1 but not in str_2: {str1_set.difference(str2_set)}")
    print(f"Characters that occur in str_2 but not in str_1: {str2_set.difference(str1_set)}")
    print(f"Characters that do not occur in either string: {set(ALPHABET).difference((str1_set.union(str2_set)))}")


if __name__ == '__main__':
    main()