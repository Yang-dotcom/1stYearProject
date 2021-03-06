# Write a program, find.py, that looks for a given word in the content of a group of
# files. The program first asks for the list of files (to be inserted on a single line,
# separated by commas) and the word to search. The file names will be stored in a list
# (files), the word to search is stored in a variable.
# You must display all the lines containing the word, regardless of whether they are
# upper of lower case, each line preceded by the name of the file in which it is located.
# For example, if the word is “ring”, and list contains:
# book.txt, address.txt, homework.py
# Then the program might print:
# book.txt: There is only one Lord of the Ring, only one who can bend it to his will
# book.txt: The ring has awoken; it’s heard its masters call.
# address.txt: Kris Kringle, North Pole
# address.txt: Homer Simpson, Springfield
# homework.py: string = “text”

FILES = [x for x in (input("ENTER FILE NAMES SEPARATED BY COMMA ',': ").split(', '))]
WORDLOOK = input("Enter the word to search: ")
def main():
    """Main Entry Point"""
    files = list()
    instances = list()
    n = 0
    try:
        for i in FILES:
            temp = open(i, 'r')
            print(temp)
            files.append(temp)
            for line in temp:
                if WORDLOOK.upper() in line.upper():
                    instances.append(f"{FILES[n]}: {line.rstrip()}")
            n += 1
        print(' \n'.join(instances))

        for j in files:
            j.close()
    except OSError as problem:
        print(f"Error encountered: {problem}")

if __name__ == '__main__':
    main()