# Write a program that reads each line in a file (input.txt), reverses its lines, and writes
# them to another file (output.txt). For example, if the file input.txt contains the lines:
# Mary had a little lamb
# Its fleece was white as snow
# And everywhere that Mary went
# The lamb was sure to go.
# The the file output.txt will be:
# The lamb was sure to go.
# And everywhere that Mary went
# Its fleece was white as snow
# Mary had a little lamb

def main():
    with open('input.txt', 'r') as fileI, open('output.txt', 'w') as fileO:
        for line in reversed(fileI.readlines()):
            fileO.write(line)
    with open('output.txt', 'r') as fileF:
        for line in fileF:
            print(f"{line.strip()}")

if __name__ == '__main__':
    main()
