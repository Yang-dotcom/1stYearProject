# Write functions that carry out the following tasks for a list of integers. For each
# function, provide a test program.
# a. Swap the first and last elements in the list.
# b. Shift all elements by one to the right and move the last element into the first
# position. For example, 1 4 9 16 25 would be transformed into 25 1 4 9 16.
# c. Replace all even elements with 0.
# d. Replace each element except the first and last by the larger of its two neighbors.
# e. Remove the middle element if the list length is odd, or the middle two elements if
# the length is even.
# f. Move all even elements to the front, otherwise preserving the order of the elements.
# g. Return the second-largest element in the list.
# h. Return true if the list is currently sorted in increasing order.
# i. Return true if the list contains two adjacent duplicate elements.
# j. Return true if the list contains duplicate elements (which need not be adjacent).

def main():
    a = [1, 4, 2, 16, 25]
    swapFL(a)
    print(a)
    print(f"Swapped first and last element {swapFL(a)}")
    print(f"Shifted right and last item in first position: {shiftRight(a)}")
    print(f"Replaced even values with 0: {replEven(a)}")
    print((f"Replace each element except the first and last by the larger of its two neighbors: {largNei(a)}"))
    print(f"Remove the middle element if the list length is odd, or the middle two elements if the length is even: {rmvMiddle(a)}")
    print(f"Move all even elements to the front, otherwise preserving the order of the elements: {evenFront(a)}")
    print(f"Return second largest element in list: {secondMax(a)}")
    print(f"Return true if the list contains two adjacent duplicate elements: {adjNeiDupl(a)}")
    print(f"Return true if the list is currently sorted in increasing order: {incrOrder(a)}")
    print(f"Return true if the list contains duplicate elements (which need not be adjacent): {dupl(a)}")


def swapFL(a):
    """Swap first and last elements in a list"""
    b = a[:]
    b[0], b[-1] = b[-1], b[0]
    return b

def shiftRight(a):
    """Shifts all elements to the right by 1 and places the last element at the beginning"""
    b = a[:]
    b.insert(0, b.pop(-1))
    return b

def replEven(a):
    b = a[:]
    for i, e in enumerate(b):
        if e % 2 == 0:
            b[i] = 0
    return b

def largNei(a):
    """Replace each element except first and last by the larger of its two neighbors."""
    b = []
    b.append(a[0])
    for i in range (1, len(a) - 1):
        b.append(max(a[i-1], a[i+1]))
    b.append(a[-1])
    return b

def rmvMiddle(a):
    """Remove the middle element if the list length is odd, or the middle two elements if
    the length is even."""
    b = a[:]
    if len(b) % 2 == 0:
        b.pop(len(b) // 2)
        b.pop(len(b) // 2)
    else:
        b.pop(len(b) // 2)
    return b

def evenFront(a):
    """Move all even elements to the front, otherwise preserving the order of the elements."""
    b = a[:]
    for i, e in enumerate(b):
        if e % 2 == 0:
            b.insert(0, b.pop(i))
    return b

def secondMax(a):
    """Return second largest element in list"""
    a.remove(max(a))
    b = max(a)
    return b

def adjNeiDupl(a):
    """Return True if list contains two adjacent duplicate elements"""
    for i in range(len(sorted(a)) - 1):
        if a[i] == a[i+1]:
            return True
    return False

def incrOrder(a):
    """Return True if list is in increasing order"""
    b = a[:]
    if a == sorted(b):
        return True
    return False

def dupl(a):
    for e in a:
        if a.count(e) > 1:
            return True
    return False


if __name__ == '__main__':
    main()
