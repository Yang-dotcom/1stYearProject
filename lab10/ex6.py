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

def del_dupl(word):
    no_dupl = "".join(dict.fromkeys(word))
    return no_dupl

def main():
    tbl = tbl5X5()
    print(del_dupl(KEYWORD), tbl)

def tbl5X5():
    tbl = [[" " for _ in range(5)] for _ in range(5)]
    return tbl

def cypher():
    pass

if __name__ == '__main__':
    main()