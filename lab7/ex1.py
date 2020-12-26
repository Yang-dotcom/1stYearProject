# Write a program that initializes a list of eleven random integers and then display in four
# lines the following information:
# a. All elements of even index.
# b. All items of equal value.
# c. All elements in reverse order.
# d. The first and the last element. [P6.1]

import random

def main():
    listInt = [random.randint(0, 40) for _ in range(11)]
    print(listInt)
    print("All elements with even index: ", end=" ")
    evenIndex(listInt)
    print(f"\nAll items of equal value: {equalValue(listInt)}")
    print(f"All elements in reverse order: {listInt[::-1]}")
    print(f"First element: {listInt[0]}, last element: {listInt[-1]}")


def equalValue(listInt):
    listEquals= []
    flag = False
    for i, e in enumerate(listInt):
        n = -1
        while not flag and abs(n) < len(listInt) - i:
            if e == listInt[n]:
                flag = True
            n -= 1
        if flag and e not in listEquals:
            listEquals.append(e)
        flag = False

    return listEquals


def evenIndex(listInt):
    for i in range(len(listInt)):
        if i % 2 == 0:
            print(listInt[i], end=" ")




if __name__ == '__main__':
    main()
