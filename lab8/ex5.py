# Write a program that plays tic-tac-toe. The tic-tac-toe game is played on a 3 × 3 grid
# as in the figure below. The game is played by two players, who take turns. The first
# player marks moves with a circle, the second with a cross. The player who has
# formed a horizontal, vertical, or diagonal sequence of three marks wins. Your
# program should draw the game board, ask the user for the coordinates of the next
# mark, change the players after every successful move, and pronounce the winner.

def main():
    tbl = table()
    for x in tbl:
        print(x)
    lost = False
    rounds = 0
    while not lost:
        rounds += 1
        playerTurn1(tbl)
        for j in tbl:
            print(j)
        if winCond(tbl) and rounds >= 5:
            return print("Player 1 won")
        playerTurn2(tbl)
        for j in tbl and rounds >= 5:
            print(j)
        if winCond(tbl):
            return print("Player 2 won")
        if rounds == 9:
            return print("No one one, you guys both suck dick")



def playerTurn1(tbl):
    row1, clmn1 = int(input("Enter P1 row value:")), int(input("Enter P1 column value:"))
    tbl[row1].pop(clmn1)
    tbl[row1].insert(clmn1, "O")
    return tbl

def playerTurn2(tbl):
    row2, clmn2 = int(input("Enter P2 row value:")), int(input("Enter P2 column value:"))
    tbl[row2].pop(clmn2)
    tbl[row2].insert(clmn2, "X")
    return tbl


def winCond(tbl):
    diag1Check = []
    diag2Check = []
    for i in range(3):
        clmnCheck = []
        rowCheck = []
        diag1Check.append(tbl[i][i])
        diag2Check.append(tbl[i][2-i])
        boolDiag1 = diag1Check.count("O") == 3 or diag1Check.count("X") == 3
        boolDiag2 = diag2Check.count("O") == 3 or diag2Check.count("X") == 3
        if boolDiag1 or boolDiag2:
            return True
        for j in range(3):
            clmnCheck.append(tbl[j][i])
            rowCheck.append(tbl[i][j])
        boolVer = clmnCheck.count("O") == 3 or clmnCheck.count("X") == 3
        boolHor = rowCheck.count("O") == 3 or rowCheck.count("X") == 3
        if boolVer or boolHor:
            return True
    return False


def table():
    """Creates a 3X3 table"""
    tbl = []
    for i in range(3):
        tblrow = []
        for j in range(3):
            tblrow.append(" ")
        tbl.append(tblrow)
    return tbl


if __name__ == '__main__':
    main()
