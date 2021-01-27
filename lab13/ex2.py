# Exercise 2. Propose three different functions (programs) that find all numbers which are
# divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). For each
# proposed function, the numbers obtained should be stored in a text file printed in a commaseparated sequence on a single line. Create a Python function that compares the three
# generated files and prints if all were equal or not.



def main():
    numbers = [m for m in range(2000, 3201)]
    txt1 = check1(numbers)
    txt2 = check2(numbers)
    txt3 = check3(numbers)
    print(f"The three fucntions produce the same numbers: {func_check(txt1, txt2, txt3)}")
    try:
        with open('file-1.txt', 'w') as file1, open('file-2.txt','w') as file2, open('file-3.txt', 'w') as file3:
            file1.write(",".join(str(e) for e in txt1))
            file2.write(",".join(str(k) for k in txt2))
            file3.write(",".join(str(l) for l in txt3))

    except OSError as error:
        print(f'{error} error.')


def check1(numbers):
    txt1 = list()
    for i in numbers:
        if i % 7 == 0 and i % 5 != 0:
            txt1.append(i)
    return txt1


def check2(numbers):
    txt2 = list()
    for i in reversed(numbers):
        if i % 7 == 0 and i % 5 != 0:
            txt2.append(i)
    return txt2


def check3(numbers):
    txt3 = list()
    flag = False
    i = 0
    while not flag:
        if numbers[i] % 7 == 0 and numbers[i] % 5 != 0:
            txt3.append(numbers[i])
        i += 1
        if i == len(numbers):
            flag = True
    return txt3


def func_check(txt1, txt2, txt3):
    if set(txt1).intersection(txt2).intersection(txt3) == set(txt3):
        return True
    return False


if __name__ == "__main__":
    main()