# Write a function removeMin that removes the minimum value from a list without
# using the min function or remove method. [P6.7]

def main():
    a = [3, 4, 5, 1, 2]
    print(f"The list with the min removed is {removeMin(a)}")

def removeMin(a):
    smallest = a[0]
    for e in a:
        if e < smallest:
            smallest = e
    b = [x for x in a if x != smallest]
    return b


if __name__ == '__main__':
    main()
