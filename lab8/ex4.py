# Write a function def mergeSorted(a, b) that merges two sorted lists, (assume that
# they are already ordered) producing a new sorted list. Keep an index into each list,
# indicating how much of it has been processed already. Each time, append the
# smallest unprocessed element from either list, then advance the index.
# The starting lists must not be modified. For example, if a is 1 4 9 16 and b is 4 7 9 9
# 11, then mergeSorted returns a new list containing the values 1 4 4 7 9 9 9 11 16. Do
# not use the sort method or the sort function. [P6.31]

def main():
    a = [1, 4] #[1, 4, 9, 16]
    b = [2, 3] #[4, 7, 9, 9, 11]
    print(f"The merged list sorted is {mergeSorted(a, b)}")

def mergeSorted(a, b):
    """Merge two sorted lists into a new sorted list"""
    c = []
    a_i = 0
    b_i = 0
    for i in range(len(a) + len(b)):
        if b_i not in range(len(b)) or (a_i in range(len(a)) and a[a_i] < b[b_i]):
            c.append(a[a_i])
            a_i += 1
        else:
            c.append(b[b_i])
            b_i += 1
    return c




if __name__ == '__main__':
    main()
