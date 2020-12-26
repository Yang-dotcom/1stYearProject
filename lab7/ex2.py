# Write a program that calculates the alternating sum of the elements of a list. For
# example, if the program reads the data 1 4 9 16 9 7 4 9 11, it must calculate
# and display 1 - 4 + 9 - 16 + 9 - 7 + 4 - 9 + 11 = –2 . [P6. 8]
import random

def main():
    """Main entry point"""
    values = [random.randint(0,10) for _ in range(10)]
    print(f"the alternating sum of the list {values} is: ")
    alterSum(values)


def alterSum(values):
    """Calculate alternating sum of elements of a list"""
    sum_ = 0
    operations = []
    for i, e in enumerate(values):
        if i % 2 == 0:
            sum_ += e
            operations.append(f"+{e}")
        else:
            sum_ -= e
            operations.append(f"-{e}")
    return print(f"{' '.join(operations)} = {sum_}")

if __name__ == '__main__':
    main()
