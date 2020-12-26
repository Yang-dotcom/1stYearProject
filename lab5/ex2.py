# When you use an automated teller machine (ATM) with your bank card, you need to
# use a personal identification number (PIN) to access your account. If a user fails
# more than three times when entering the PIN, the machine will block the card.
# Assume that the user’s PIN is “1234” and write a program that asks the user for the
# PIN no more than three times, and does the following:
# • If the user enters the right number, print a message saying, “Your PIN is
# correct”, and end the program.
# • If the user enters a wrong number, print a message saying, “Your PIN is
# incorrect” and, if you have asked for the PIN less than three times, ask for it
# again.
# • If the user enters a wrong number three times, print a message saying “Your
# bank card is blocked” and end the program. [P3.39]

pin = "1234"
tryTimes = 3

while tryTimes > 0:
    userInput = input("enter PIN: ")
    if userInput == pin:
        print("your PIN is correct")
        tryTimes = -1
    else:
        print("your PIN is incorrect")
        tryTimes -= 1

if tryTimes == 0:
    print("your bank card is blocked")
