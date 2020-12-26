# Write the function def equals(a, b) that checks whether two lists a and b
# contain the same elements in the same order. [P6. 11]
import random

def main():
    """Main entry point"""
    listA = [random.randint(0,10) for _ in range(10)]
    listB = [random.randint(0,10) for _ in range(10)]
    print(f"the statement 'two lists {listA} and {listB} are equal.' is {checkEqual(listA, listB)}")

def checkEqual(listA, listB):
    if len(listA) != len(listB):
        return False
    for i, e in enumerate(listA):
        if listA[i] != listB[i]:
            return False
    else:
        return True


if __name__ == '__main__':
    main()
