# Write a program that counts the occurrences of each word in a text file. Next,
# improve the program so that it displays the most common 100 words. [P8.2] [P8.3]

FILE_NAME = 'ex1_sample.txt'

def main():
    dict_words = dict()
    try:
        with open(FILE_NAME, 'r') as file1:
            for line in file1:
                list_words = line.strip(",.\n").lower().replace("'", " ").replace(",", "").replace(".", "").split()
                for e in list_words:
                    if e in dict_words:
                        dict_words[e] += 1
                    else:
                        dict_words[e] = 1
            for i in dict_words.items():
                print(f"{i[0]:15} ---> {i[1]} ")
            sorted_dict = sorted(dict_words.items(), key=lambda x: x[1], reverse=True)
            # sorted(iterable, key= None, reverse=False) gives a new iterable without changing the original. list.sort(reverse=False, key=function(to be defined, default ascending)) instead only works for lists and mutates the original list.
            print(*sorted_dict[:20], sep="\n")
            # *sorted_dict unpacks all elements of the list and passes each parameter to the print function. sorted_dict[:20] returns a list up till the 20th element.
            # the sep="\n" paramenter of the print function in conjuction with the unpacking of elements, prints every single element on a new line in a clean way

    except OSError as error:
        print(f"Error encountered: {error}")

if __name__ == '__main__':
    main()