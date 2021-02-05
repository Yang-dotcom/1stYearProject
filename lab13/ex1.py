def main():
    p_lists = list()
    try:
        with open("input.txt", "r") as file1:
            for line in file1:
                p_lists.append(dict_player(line))
    except OSError as error:
        print(f"{error}")

    print(p_lists)


def dict_player(line):
    p_dict = dict()
    scores_list = line.strip().split("  ")
    print(scores_list)
    for i in range(0, 10):
        p_dict[i+1] = scores_list[i].split(" ")
    if len(scores_list) == 11:
        p_dict[11] = scores_list[10].split(" ")
    if len(scores_list) == 12:
        p_dict[11] = scores_list[10].split(" ")
        p_dict[12] = scores_list[11].split(" ")
    return p_dict


if __name__ == "__main__":
    main()
