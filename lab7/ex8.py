# Often the values collected during an experiment need to be corrected to remove part of
# the measurement noise. A simple approach to this problem is to replace, in a list, each
# value with the average between the same value and the two adjacent values (or a single
# adjacent one if the value under consideration is at one end of the list). Build a program
# that does this, without creating another list. [P6. 36]

def main():
    listA = [1, 2, 3, 4, 5, 6]
    print(f"Original list: {listA}, corrected list is {correction(listA)}")

def correction(listA):
    x = listA.index(listA[-1])
    for i, e in enumerate(listA):
        if i == 0:
            listA[i] = round((e + listA[1]) / 2, 3)
        elif i == x:
            listA[i] = round((e + listA[-2]) / 2, 3)
        else:
            listA[i] = round((listA[i - 1] + e + listA[i + 1]) / 3, 3)
    return listA



if __name__ == '__main__':
    main()
