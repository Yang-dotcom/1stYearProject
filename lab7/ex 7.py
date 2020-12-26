# Write the sumWithoutSmallest function that calculates, with a single loop, the
# sum of all the values of a list, excluding the minimum value. In the loop, update the sum
# and the minimum value; at the end, print the difference between these two values on the
# terminal. [P6.6]

def main():
    listA = [2, 3, 4, 5, 6, 1]
    print(f"The sum of the elements {listA} is {sumWithoutSmallest(listA)}")

def sumWithoutSmallest(listA):
    smallest = listA[0]
    sum_ = 0
    for i, e in enumerate(listA):
        sum_ += e
        if e < smallest:
            smallest = e
    sum_ -= smallest
    return sum_

if __name__ == '__main__':
    main()
