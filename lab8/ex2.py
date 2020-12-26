# Write a function def neighborAverage(values, row, column) that computes the
# average of the neighbors of a table element in the eight directions shown in Figure
# below. However, if the element is located at the boundary of the table, only include
# the neighbors that are in the table. For example, if row and column are both 0, there
# are only three neighbors. [P6.23]

def main():
    nRow = int(input("Enter n of table rows: "))
    nClmn = int(input("Enter n of table columns: "))
    table = table3X3(nRow, nClmn)
    for item in table:
        print(item)
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    print(f"The average of the neighbours of {table[row][column]} in the table is {neiAverage(table, row, column)}")

def table3X3(nRow, nClmn):
    tbl = []
    a = 0
    for i in range(nRow):
        tblRow = []
        for j in range(nClmn):
            # tblRow.append(int(input(f"Enter row {i}, column {j}: " )))
            tblRow.append(a)
            a += 1
        tbl.append(tblRow)
    return tbl




def neiAverage(value, row, column):
    sum_ = []
    directions = [[-1, -1], [-1, 0], [-1, +1],
                  [0, -1],           [0, 1],
                  [1, -1], [1, 0], [1, 1]]
    for d in directions:
        rowNei = row + d[0]
        clmnNei = column + d[1]
        if rowNei in range(len(value)) and clmnNei in range(len(value[0])):
            sum_.append(value[rowNei][clmnNei])
    average = sum(sum_) / len(sum_)
    return average



if __name__ == '__main__':
    main()















































# def neighborAverage(values, row, column):
#     nRows = len(values)
#     nColumns = len(values[0])
#     directions = [[-1, -1], [-1, 0], [-1, +1]
#                 [0, -1],         [0, +1],
#                 [+1, -1], [+1, 0], [+1, +1]]
#
#     sumNei = 0
#     nNei = 0
#     for d in directions:
#         rowNe = row + d[0]
#         colNe = col + d[1]
        # if rowNe, colNe is valid location
        #     sumNe += values[rowNe][colNe]
        #     nNei += 1
        # calculate average
        # return average

# tbl = []
# for i in range (5):
#     tblRow = []
#     for j in range(6):
#         tblRow.append(int(input("...")))
#     tblRow = [int(input(" ")) for j in range(6)] #does the same thing of the second loop but in a list comprehension
#
# tbl = [[int(input("")) for j in range(6)] for i in range(5)]
