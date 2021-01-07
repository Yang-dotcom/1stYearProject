# A hotel salesperson enters sales in a text file. Each line contains the following,
# separated by semicolons: The name of the client, the service sold (such as Dinner,
# Conference, Lodging, and so on), the amount of the sale, and the date of that event.
# Write a program that reads such a file and displays the total amount for each service
# category. Display an error if the file does not exist or the format is incorrect. [P7.29]

FILE_NAME = 'sales.dda'

def main():
    """Main Entry Point"""
    service_amount = dict()
    try:
        with open(FILE_NAME, 'r') as file1:
            for line in file1:
                temp_list = []
                temp_list = line.rstrip().split("; ")
                service, amount = temp_list[1], int(temp_list[2])
                prev_amount = service_amount.get(service, 0)
                service_amount.setdefault(service, amount)
                service_amount[service] += prev_amount
    except OSError as problem:
        print(f"Error encountered: {problem}")
    except ValueError as error:
        print(f"Wrong value format: {error}")

    for i, k in service_amount.items():
        print(f"{i}: {k}")


if __name__ == '__main__':
    main()