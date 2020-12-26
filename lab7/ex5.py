# Write a program that generates a sequence of 20 random values between 0 and 99, then
# displays the generated sequence, orders it, and displays it again, sorted. Use the sort
# method. [P6.17]
import random

def main():
    listA = [random.randint(0, 99) for _ in range(20)]
    print(f"Original list {listA}. Ordered list: {sorted(listA)}")

if __name__ == '__main__':
    main()
