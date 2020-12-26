# Write a function def merge(a, b) that merges two lists, alternating elements from both
# lists. If one list is shorter than the other, then alternate as long as you can and then
# append the remaining elements from the longer list. For example, if a is 1 4 9 16 and
# b is 9 7 4 9 11 then merge returns a new list containing the values 1 9 4 7 9 4 16 9 11

def main():
    a = [1, 4, 9, 16]
    b = [9, 7, 4, 9, 11]
    print(f"The list of alternating elements from {a} and {b} is the new list {merge(a, b)}")


def merge(a,b):
    c = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            c.append(a[i])
        if i < len(b):
            c.append(b[i])
    return c


if __name__ == '__main__':
    main()
