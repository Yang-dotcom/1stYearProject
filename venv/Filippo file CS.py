# Write a program that reads in a text file, converts all words to lowercase, and prints out all words in the file that contain the letter a, the letter b, and so on
# Build a dictionary whose keys are the lowercase letters, and whose values are sets of words contianing the given letter.


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
FILENAME = 'song.txt'

import sys

def new_word(word_raw):
    cooked_word = word_raw.lower().strip('",.\'\n')
    return cooked_word

def main():
    letters_dict = dict()
    for i in range(len(ALPHABET)):
        letters_dict[ALPHABET[i].lower()] = set()
    try:
        words = list()
        with open(FILENAME, 'r') as input_file:
            for line in input_file:
                for word_raw in line.split():
                    words.append(new_word(word_raw))

    except OSError as error:
        print(f"{FILENAME} not found: {error}")
        sys.exit(10)

    for name in words:
        for char    in set(name):
            if char.isalpha():
                letters_dict[char].add(name)

    for ele in letters_dict:
        print(f"{ele} -> {letters_dict[ele]}")


if __name__ == '__main__':
    main()