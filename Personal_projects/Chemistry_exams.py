def main():
    dict_marks = dict()
    try:
        with open('marks.txt', 'r') as file:
            for line in file:
                b = line.split()[1]
                if int(b) >= 18:
                    if b in dict_marks:
                        dict_marks[b] += 1
                    else:
                       dict_marks[b] = 1
    except OSError:
        print('Error encountered')

    tot_students_passed = 0
    tot_marks = 0
    for key in sorted(dict_marks):
        tot_students_passed += int(dict_marks[key])
        tot_marks += int(key) * int(dict_marks[key])
        print(f'Number of students: {dict_marks[key]}, Mark: {key: ^{10 }}')
    print(f'Average is {tot_marks / tot_students_passed:.2f}')

if __name__ == '__main__':
    main()