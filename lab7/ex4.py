# Write the function def sameSet(a,b) that checks if two lists contain the same
# elements, regardless of the order and ignoring the presence of duplicates. For example,
# the two lists 1 4 9 16 9 7 4 9 11 and 11 11 7 9 16 4 1 must be
# considered equal. You will probably find it useful to design auxiliary functions.
# [P6. 12]

def main():
    listA = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    listB = [11, 11, 7, 9, 16, 4, 1]
    print(f"the statement 'listA has the same elements as listB' is {sameSet(listA, listB)}")

def sameSet(listA, listB):
    listA = delDupl(listA)
    listB = delDupl(listB)
    if len(listA) != len(listB):
        return False
    for i, e in enumerate(listA):
        if e not in listB:
            return False
    else:
        return True

def delDupl(lists):
    list_ = []
    for i, e in enumerate(lists):
        if e not in list_:
            list_.append(e)
    return list_



if __name__ == '__main__':
    main()
