# Lo schema dei posti a teatro è una tabella con i prezzi dei biglietti per ciascun posto,
# come questa. [P6.27]
# 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10
# 10 10 10 10 10 10 10 10 10 10
# 10 10 20 20 20 20 20 20 10 10
# 10 10 20 20 20 20 20 20 10 10
# 10 10 20 20 20 20 20 20 10 10
# 20 20 30 30 40 40 30 30 20 20
# 20 30 30 40 50 50 40 30 30 20
# 30 40 50 50 50 50 50 50 40 30
# Scrivete un programma che chieda all’utente di scegliere un posto o un prezzo.
# Contrassegnate con un prezzo uguale a 0 i posti già venduti. Quando l’utente
# specifica un posto, accertatevi che sia libero. Quando, invece, specifica un prezzo,
# assegnategli un posto qualsiasi tra quelli disponibili a quel prezzo.

def main():
    a = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
         [10, 10, 20, 20, 20, 20, 20, 20, 10, 10], [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
         [20, 20, 30, 30, 40, 40, 30, 30, 20, 20], [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
         [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]
    for e in a:
        print(e)
    autSeatPrice(a)



def autSeatPrice(a):
    sentinel = False
    while not sentinel:
        question = input("Press Y to choose seat based on position. Press N to choose seat based on price. Press Z to stop: ").upper()
        if question == "Z":
            break
        flag = False
        if question.upper() == "Y":
            while not flag:
                row, clmn = map(int, input("Choose row and column of the seat you want: ").split())
                if a[row][clmn] != 0:
                    a[row][clmn] = 0
                    for e in a:
                        print(e)
                    flag = True
                else:
                    print("The selected seat is not available. Please choose another one")
        if question.upper() == "N":
            priceEqual = int(input("Enter a price: "))
            for i, o in enumerate(a):
                    for j, k in enumerate(o):
                        if k == priceEqual and k != 0 and not flag:
                            a[i][j] = 0
                            flag = True
            for u in a:
                print(u)
    return a



if __name__ == '__main__':
    main()
