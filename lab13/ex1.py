<<<<<<< HEAD
=======

>>>>>>> origin/master
def main():
    p_lists = list()
    try:
        with open("input.txt", "r") as file1:
            for line in file1:
                p_lists.append(dict_player(line))
<<<<<<< HEAD
    except OSError as error:
        print(f"{error}")

    print(p_lists)
=======

    except OSError as error:
        print(f"{error}")
    list_scores = list()
    for i in range(len(p_lists)):
        list_scores.append(sum_scores(p_lists[i]))
    for k in range(len(list_scores)):
        print(f"\nPlayer {k+1}")
        print(f"Frame       Score")
        print("-----        -----")
        for i in range(0, len(list_scores[k])):
            print(f"{i+1}{list_scores[k][i]:15d}")
>>>>>>> origin/master


def dict_player(line):
    p_dict = dict()
    scores_list = line.strip().split("  ")
<<<<<<< HEAD
    print(scores_list)
=======
>>>>>>> origin/master
    for i in range(0, 10):
        p_dict[i+1] = scores_list[i].split(" ")
    if len(scores_list) == 11:
        p_dict[11] = scores_list[10].split(" ")
    if len(scores_list) == 12:
        p_dict[11] = scores_list[10].split(" ")
        p_dict[12] = scores_list[11].split(" ")
    return p_dict

<<<<<<< HEAD

if __name__ == "__main__":
    main()
=======
def sum_scores(p_scores):
    sum = 0
    sum_frames = list()
    for i in range(1, 11):
        if len(p_scores[i]) == 2:
            if int(p_scores[i][0]) + int(p_scores[i][1]) == 10:
                sum += int(p_scores[i][0]) + int(p_scores[i][1]) + int(p_scores[i+1][0])
            elif int(p_scores[i][0]) + int(p_scores[i][1]) < 10:
                sum += int(p_scores[i][0]) + int(p_scores[i][1])
        elif len(p_scores[i]) == 1:
            if len(p_scores[i +1]) == 2:
                sum += int(p_scores[i][0]) + int(p_scores[i+1][0]) + int(p_scores[i+1][1])
            elif len(p_scores[i+1]) == 1:
                sum += int(p_scores[i][0]) + int(p_scores[i+1][0]) + int(p_scores[i+2][0])
        sum_frames.append(sum)
    return sum_frames

if __name__ == '__main__':
    main()
>>>>>>> origin/master
