def main():
    contacts = dict()
    for i in range(len(customers)):
        name, phone, entry, exit = customers[i].split(",")
        contacts[name] = (phone, int(entry), int(exit))
    for i in suspicious:
        m = i.strip()
        print(f"* Customer contacts:{m}*")
        entry, exit = contacts[m][1], contacts[m][2]
        possible_suspects = 0
        contacts.pop(m)
        for k in sorted(contacts.keys()):
            stay = set(i for i in range(contacts[k][1], contacts[k][2]+1) if entry <= i <= exit)
            if any(stay):
                possible_suspects += 1
                print(f"Contact with {k}, phone{contacts[k][0]}")
        if possible_suspects == 0:
            print(f"The customer {m} had no contact")


if __name__ == '__main__':
    with open('attendance.txt', "r") as f:
        customers = f.readlines()
    with open('suspicious.txt', "r") as f:
        suspicious = f.readlines()
    main()