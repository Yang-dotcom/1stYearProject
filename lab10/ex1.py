# Write a program that reads a file containing text named input.txt. Read each line and
# send it to the output file output.txt, preceded by line numbers between characters /*
# and */.
# Mary had a little lamb
# Whose fleece was white as snow.
# And everywhere that Mary went,
# The lamb was sure to go!
# The file output.txt will be:
# /*1*/ Mary had a little lamb
# /*2*/ Whose fleece was white as snow.
# /*3*/ And everywhere that Mary went,
# /*4*/ The lamb was sure to go!

def main():
    with open('input.txt', 'r') as fileI, open('output.txt', 'w') as fileO:
            for i, j in enumerate(fileI):
                fileO.write(f"/*{i}*/ {j}")
    with open('output.txt', 'r') as fileF:
        for lines in fileF:
            print(lines)

if __name__ == '__main__':
    main()
