# Write a program that displays the list of exams passed by a student, with their grades.
# There is a file, classes.txt, that contains the names of all the teachings given in the
# school (a U.S. college), whose content will be similar to this one:
# CSC1
# CSC2
# CSC46
# CSC151
# MTH121
# …
# Then, for each teaching, there is a file (whose name is equal to the teaching code
# followed by .txt) that lists the students who have passed the relevant exam and
# contains the student ID numbers and grades, like this one, which could be the
# CSC2.txt file:
# 11234 A–
# 12547 B
# 16753 B+
# 21886 C
# …
# Write a program that asks the user for a student's ID and displays the list of exams
# that that student has passed, with the relative grades obtained, as in this example:
# Student ID 16753
# CSC2 B+
# MTH121 C+
# CHN1 A
# PHY50 A–
# [P7.28]

MAIN_FILE = 'classes.txt'
STUDENT_ID = input("Enter student ID: ").strip()

def create_files(MAIN_FILE):
    files_OS = []
    files = []
    with open(MAIN_FILE, 'r') as main_file:
        for line in main_file:
            try:
                files.append(f'{line.rstrip()}.txt')
                sgl_file = open(f'{line.rstrip()}.txt', 'x' )
                files_OS.append(sgl_file)
                print(f"'{line.rstrip()}.txt' has been created")
            except FileExistsError:
                print(f"'{line.rstrip()}.txt' already exists")
        for j in files_OS:
            j.close()
    return files
def main():
    list_files = create_files(MAIN_FILE)
    temp_OS = []
    subjects_pass = []
    for i in list_files:
        temp_file = open(i, 'r')
        temp_OS.append(temp_file)
        all_students_subject = temp_file.read().splitlines()
        subjects_pass.append(find_ID(all_students_subject, i))

    print(f"Student ID {STUDENT_ID}: {[x for x in subjects_pass if x != '']}")


    for j in temp_OS:
        j.close()


def find_ID(ID_mark_list, file_name):
    passed_subject = ""
    for i in ID_mark_list:
        if STUDENT_ID in i:
            passed_subject = file_name + " with Grade: " + i.split()[1]
            return passed_subject
    return ''




if __name__ == '__main__':
    main()