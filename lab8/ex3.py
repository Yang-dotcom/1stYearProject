# Magic squares. An n × n matrix that is filled with the numbers 1, 2, 3, ..., n2 is a
# magic square if the sum of the elements in each row, in each column, and in the two
# diagonals is the same value. For instance, this is a magic square with size 4:
#Write a program that reads in 16 values from the keyboard and tests
# whether they form a magic square when put into a 4 × 4 table. You
# need to test two features:
# 1. Does each of the numbers 1, 2, …, 16 occur in the user input?
# 2. When the numbers are put into a square, are the sums of the rows, columns,
# and diagonals equal to each other?

def main():
    length = int(input("Enter size of n x n matrix: "))
    table = tableNXN(length)
    for item in table:
        print(item)
    print(f"the table is a magic square: {magicSquare(length, table)}")

def tableNXN(length):
    """Creates a matrix n x n and user inputs values into the matrix"""
    tbl = []
    noDupl = []
    flag = False
    for i in range(length):
        tblRow = []
        for j in range(length):
            a = int(input(f"Enter value from 1 to {length*length}: "))
            if a not in noDupl:
                tblRow.append(a)
                noDupl.append(a)
            else:
                while not flag:
                    a = int(input(f"Enter again a value from 1 to {length*length}: "))
                    if a not in noDupl:
                        tblRow.append(a)
                        noDupl.append(a)
                        flag = True
        flag = False
        tbl.append(tblRow)
    return tbl

def magicSquare(length, table):
    """Check if matrix is magic square"""
    sumCheck = sum(table[0]) # (1 + length * length) * length // 2
    for i in range(length):
        if sum(table[i]) != sumCheck:
            return False
    for j in range(length):
        clmnSum = 0
        for k in range(length):
            clmnSum += table[k][j]
        if clmnSum != sumCheck:
            return False
    diagSum1 = 0
    for x in range(length):
        diagSum1 += table[x][x]
    if diagSum1 != sumCheck:
        return False
    diagSum2 = 0
    for l in range(length):
        diagSum2 += table[l][length - l]
    if diagSum2 != sumCheck:
        return False
    return True


if __name__ == '__main__':
    main()
