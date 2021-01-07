# Random monoalphabet cipher. The Caesar cipher, which shifts all letters by a fixed
# amount, is far too easy to crack. Here is a better idea. As the key, don’t use numbers
# but words. Suppose the key word is FEATHER. Then first remove duplicate letters,
# yielding FEATHR, and append the other letters of the alphabet in reverse order:
# F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
# Now encrypt the letters as follows:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
# F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
# Write a program that encrypts or decrypts a file using this cipher. For example,
# crypt.py -d -kFEATHER encrypt.txt output.txt
# decrypts a file using the keyword FEATHER. It is an error not to supply a keyword.
# The first parameter (-d) determines if you have to encrypt (-e) or decrypt (-d) the
# input file (encrypt.txt in the example). [P7.20]

# KEY_WORD = input("Enter key word to use in encryption system: ")
# ENCRYPT_CHOICE = input("Enter -d to encrypt, -e to decrypt: ")

FILE_NAME = 'monoAlphabet.dsa'
WORD = input("Enter word to be used as key of encryption: ")
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    """MAIN ENTRY POINT"""
    encr_decr = input("Enter -e to encrypt, -d to decrypt: ")
    word = del_dupl(WORD).upper()
    new_alphabet = list(word) + [c for c in reversed(ALPHABET) if c not in word]
    encrypt_dict = decr2encr(new_alphabet)
    decrypt_dict = encr2decr(new_alphabet)
    list_words = list()
    print(del_dupl(WORD))
    print(new_alphabet)
    try:
        with open(FILE_NAME, 'r+') as file1:
            for line in file1:
                line.strip()
                try:
                    if encr_decr == "-e":
                        list_words.append(encrypt(line, encrypt_dict))
                    elif encr_decr == "-d":
                        list_words.append(decrypt(line, decrypt_dict))
                    else:
                        print("Invalid value")

                except ValueError as error:
                    print("invalid characters detected")

    except OSError as problem:
        print(f"Error encountered opening file: {problem}")

    print("\n".join(list_words))

def del_dupl(word):
    """REMOVE DUPLICATE LETTERS FROM KEY WORD"""
    result = "".join(dict.fromkeys(word))
    return result

def encrypt(line, encrypt_dict):
    final1 = ""
    for c in line.upper():
        final1 += encrypt_dict.get(c)
    return final1

def decrypt(line, decrypt_dict):
    final2 = ""
    for c in line.upper():
        final2 += decrypt_dict.get(c)
    return final2

def encr2decr(new_alphabet):
    encr_dict = dict()
    for i in range(len(ALPHABET)):
        encr_dict.update({ALPHABET[i]: new_alphabet[i]})
    return encr_dict

def decr2encr(new_alphabet):
    decr_dict = dict()
    for i in range(len(ALPHABET)):
        decr_dict.update({new_alphabet[i]: ALPHABET[i]})
    return decr_dict

if __name__ == '__main__':
    main()



















## CAESAR METHOD OF ENCRYPTION
# ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ROT = 13
# string = input("Enter string: ")
# def chr2num(c):
#     return ALPHABET.index(c)
#
# def num2chr(c):
#     a = (len(ALPHABET) + c) % len(ALPHABET)
#     b = ALPHABET[a]
#     return b
#
# def encrypt(string):
#     encrypted = ""
#     for c in string:
#         encrypted += num2chr(chr2num(c) + ROT)
#     print(encrypted)
#
# encrypt(string)