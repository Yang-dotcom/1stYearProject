def main():
    list_lines = list()
    try:
        with open("strawberry.txt", "r") as file1:
            for line in file1:
                line_words = clean_line(line)
                list_lines.append(line_words)

    except OSError as error:
        print(f"File error: {error}")
    for i, e in enumerate(list_lines):
        j = 0
        for l, k in enumerate(list_lines[i]):
            if j < len(list_lines[i]) - 2 and len(list_lines[i][l]) == len(list_lines[i][l + 1]) == len(list_lines[i][l + 2]):
                print(list_lines[i][l], list_lines[i][l + 1], list_lines[i][l + 2])
            elif len(list_lines[i]) - j == 2 and i < len(list_lines) and len(list_lines[i][l]) == len(list_lines[i][l + 1]) == len(list_lines[i + 1][0]):
                print(list_lines[i][l], list_lines[i][l + 1], list_lines[i + 1][0])
            j += 1
    for p in list_lines:
        print(p)

def clean_line(line):
    cleaned = line.strip("\n',\".!?-").split(" ")
    for i, e in enumerate(cleaned):
        cleaned[i] = cleaned[i].replace(",", "").replace(".", "").replace("!", "").replace("\"", "").replace("?", "").upper()
    return cleaned


if __name__ == "__main__":
    main()