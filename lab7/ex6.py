# Write a function which reverses the sequence of the elements of a list. For example, if
# the function is invoked with the list 1 4 9 16 9 7 4 9 11 , it must modify its
# content so that it becomes 11 9 4 7 9 16 9 4 1 . [P6. 9]

import random

def main():
    listA = [random.randint(0, 10) for _ in range(5)]
    print(f"Original list {listA}, reversed list {reverseList(listA)}")

def reverseList(listA):
    for i in range(len(listA) // 2):
        listA[-i - 1], listA[i] = listA[i], listA[-i - 1]
    return listA


if __name__ == '__main__':
    main()
