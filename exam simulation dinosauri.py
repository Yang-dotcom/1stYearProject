import random

def main():
    try:
        with open("mazzo.txt", "r") as file1:
            cards = file1.read().split()
    except OSError as error:
        print(f"Error encountered: {error}")
    index = list()
    print(cards)
    random.shuffle(cards)
    cards_shuffled = list()
    print(cards)
    x = None
    for i in range(0, 30):
        flag = False
        while not flag:
            x = None
            if x not in index:
                x = random.randint(0, 29)
                flag = True
            if i == 30:
                flag = True
        cards_shuffled.append(cards[x])
        index.append(x)
    p1_cards = create_hand(cards)
    p2_cards = create_hand(cards)

def create_hand(hands):
    """Creates a random hand of 15 cards"""


def win_cond():
    pass

if __name__ == '__main__':
    main()