# Playfair cipher. Another way of thwarting a simple letter frequency analysis of an
# encrypted text is to encrypt pairs of letters together. A simple scheme to do this is the
# Playfair cipher. You pick a keyword and remove duplicate letters from it. Then you
# fill the keyword, and the remaining letters of the alphabet, into a 5 × 5 square.
# (Because there are only 25 squares, I and J are considered the same letter.). Here is
# such an arrangement with the keyword PLAYFAIR.
# P L A Y F
# I R B C D
# E G H K M
# N O Q S T
# U V W X Z
# To encrypt a letter pair, say AM, look at the rectangle with corners A and M:
# P L A Y F
# I R B C D
# E G H K M
# N O Q S T
# U V W X Z
# The encoding of this pair is formed by looking at the other two corners of the
# rectangle, in this case, FH. If both letters happen to be in the same row or column,
# such as GO, simply swap the two letters. Decryption is done in the same way. Write
# a program that encrypts or decrypts an input text according to this cipher. [P7.23]

FILE_NAME = 'playFairCypherTest.txt'
KEYWORD = input("Enter key word in the cypher: ")
ALPHABET = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def del_dupl(word):
    no_dupl = "".join(dict.fromkeys(word)).upper()
    if "J" in no_dupl:
        no_dupl = no_dupl.replace("J", "I")
    return no_dupl

def main():
    """MAIN ENTRY POINT"""
    tbl = tbl5X5(KEYWORD)
    print(del_dupl(KEYWORD))
    display_matrix(tbl)

    try:
        with open('playFairCypherTest.txt') as cypher_test:
            for line in cypher_test:
                try:
                    x = []
                    x = plain_text(line)
                    print(f"Original: {x}")
                    print(cypher(x, tbl))
                except ValueError as error:
                    print(f"Unexpected value entered: {error}")

    except OSError as problem:
        print(f"Error encountered: {problem}")

def tbl5X5(word):
    full_string = ''.join(list(del_dupl(word)) + [c for c in ALPHABET if c not in del_dupl(word)])
    tbl = [["" for _ in range(5)] for _ in range(5)]
    print(f"{full_string}")
    for i in range(5):
        for j in range(5):
            tbl[i][j] = full_string[i * 5 + j]
    return tbl

def cypher(plain_text, tbl):
    # check row
    list_temp = []
    for i in range(len(plain_text)):
        first_chr = plain_text[i][0]
        second_chr = plain_text[i][1]
        index_first = [(i, el.index(first_chr)) for i, el in enumerate(tbl) if first_chr in el]
        index_second =[(i, el.index(second_chr)) for i, el in enumerate(tbl) if second_chr in el]
        list_temp.append(index_first)
        list_temp.append(index_second)
        # print(first_chr, second_chr)
        # print(type(index_first[0][0]), type(index_second[0][1]))
        # print(tbl[index_first[0][0], index_second[0][1]])
        if index_first[0][0] == index_second[0][0] or index_first[0][1] == index_second[0][1]:
            # print(f"OK for {first_chr} and {second_chr}")
            plain_text[i][0], plain_text[i][1] = plain_text[i][1], plain_text[i][0]
            # print(f"Switched 1: {plain_text[i][0]}, {plain_text[i][1]}")
        else:
            plain_text[i][0] = tbl[index_first[0][0]][index_second[0][1]]
            plain_text[i][1] = tbl[index_second[0][0]][index_first[0][1]]
            # print(f"Switched 2: {plain_text[i][0]}, {plain_text[i][1]}")

    return plain_text



def plain_text(user_line):
    user_line = ''.join(user_line.split()).replace(".", "").upper()
    if len(user_line) % 2 != 0:
        user_line += "Z"
    list_line = [["" for x in range(2)] for c in range(len(user_line) // 2)]
    for i in range(len(user_line) // 2):
        for j in range(2):
            list_line[i][j] = user_line[2 * i + j]
    return list_line



def display_matrix(tbl):
    for x in tbl:
        print(x)

if __name__ == '__main__':
    main()
