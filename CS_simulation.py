# this is an example of answer filling
# files attendance.txt and suspicious.txt are available, just open them
def main():
    dict_name = dict()
    suspect_contacts_dict = dict()
    with open('attendance.txt', 'r') as attendance, open('suspicious.txt', 'r') as suspiscious:
        for line in attendance:
            name_list = line.strip().split(', ', 1)
            objct_list = name_list[1].split(',')
            dict_name[name_list[0]] = objct_list
        # dict_name[key][0] to access phone number
        for line in suspiscious:
            start_day = int(dict_name[line.strip()][1])
            end_day = int(dict_name[line.strip()][2])
            suspect_contacts_dict[line.strip()] = contact_suspect(dict_name, start_day, end_day)
    for key in suspect_contacts_dict:
        if len(suspect_contacts_dict[key]) != 0:
            suspect_contacts_dict[key] = sorted(suspect_contacts_dict[key])
            print(f"** Customer contacts: 1 {key} **")
            for i in range(len(suspect_contacts_dict[key])):
                print(f"Contact with {suspect_contacts_dict[key][i]}, phone {dict_name[suspect_contacts_dict[key][i]][0]}")
        else:
            print(f"** Customer contacts: 2 {key}: **")
            print(f"The customer {suspect_contacts_dict[key]} had no contact")


def contact_suspect(dict_name, start_day, end_day):
    sus_cont_list = list()
    flag = 0
    for key in dict_name:
        contact_days = [m for m in range(int(dict_name[key][1]), int(dict_name[key][2]))]
        while flag >= 0 and flag < len(contact_days):
            print(contact_days[flag])
            if contact_days[flag] in range(start_day, end_day):
                sus_cont_list.append(key)
                flag = -1
            else:
                flag += 1
    if len(sus_cont_list) == 0:
        sus_cont_list.append(0)
    return sus_cont_list
# finish

if __name__ == '__main__':
    main()
