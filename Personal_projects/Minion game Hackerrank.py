# def minion_game(string):
#     stuart = []
#     kevin = []
#     vowels = {'U', 'O', 'E', 'A', 'I'}
#     consonants = {'M', 'K', 'X', 'W', 'G', 'Q', 'R', 'P', 'J', 'B', 'H', 'C', 'V', 'D', 'F', 'S', 'N', 'L', 'Y', 'T', 'Z'}
#     for i in range(0, len(string)):
#         for j in range(i + 1, len(string) + 1):
#             if string[i] in consonants and string[i:j] not in stuart:
#                 stuart.append(string[i:j])
#             elif string[i] in vowels and string[i:j] not in kevin:
#                 kevin.append(string[i:j])
#     stuart_score = 0
#     kevin_score = 0
#     for sub_k in kevin:
#         kevin_score += overlapping_count(string, sub_k)
#     for sub_s in stuart:
#         stuart_score += overlapping_count(string, sub_s)
#     if kevin_score > stuart_score:
#         print(f'Kevin {kevin_score}')
#     elif stuart_score > kevin_score:
#         print(f'Stuart {stuart_score}')
#     elif kevin_score == stuart_score:
#         print('Draw')
# def overlapping_count(string, substring):
#     count = 0
#     position = 0
#     flag = False
#     while not flag:
#         position = string.find(substring, position)
#         if position > -1:
#             count += 1
#             position += 1
#         else:
#             flag = True
#     return count
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)
#

def minion_game(string):
        s = string.strip()
        s_length = len(s)
        kevin, stuart = 0, 0
        for i in range(s_length):
            if s[i] in 'AEIOU':
                kevin += s_length - i
            else:
                stuart += s_length - i
        if kevin > stuart:
            print("Kevin", kevin)
        elif kevin < stuart:
            print("Stuart", stuart)
        else:
            print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)