# The game of Nim. This is a well-known game with a number of variants. The following variant
# has an interesting winning strategy. Two players alternately take marbles from a pile. In each
# move, a player chooses how many marbles to take. The player must take at least one but at most
# half of the marbles. Then the other player takes a turn. The player who takes the last marble loses.
# Write a program in which the computer plays against a human opponent. Generate a random
# integer between 10 and 100 to denote the initial size of the pile. Generate a random integer
# between 0 and 1 to decide whether the computer or the human takes the first turn. Generate a
# random integer between 0 and 1 to decide whether the computer plays smart or stupid. In stupid
# mode the computer simply takes a random legal value (between 1 and n/2) from the pile whenever
# it has a turn. In smart mode the computer takes off enough marbles to make the size of the pile a
# power of two minus 1—that is, 3, 7, 15, 31, or 63. That is always a legal move, except when the
# size of the pile is currently one less than a power of two. In that case, the computer makes a
# random legal move. You will note that the computer cannot be beaten in smart mode when it has
# the first move, unless the pile size happens to be 15, 31, or 63. Of course, a human player who
# has the first turn and knows the winning strategy can win against the computer.

import random

totalMarbles = random.randint(10, 100)
print(f"\ntotal number of marbles is : {totalMarbles}")
firstTurn = random.randint(0,1)
smartStupid = random.randint(0,1)
flag = False
listPowersOf2 = []
for i in range (2, 7, 1):
    listPowersOf2.append((2 ** i) - 1)
print("\n", listPowersOf2)

if smartStupid == 0 and firstTurn == 0:
    print("\nthe PC goes first and it's stupid.")
    while not flag:
        if not totalMarbles == 1:
            robbedMarblesPC = random.randint(1, totalMarbles//2)
            totalMarbles -= robbedMarblesPC
            print(f"\nPc takes away {robbedMarblesPC} marbles, remaining pool is {totalMarbles} marbles")
            if totalMarbles == 0:
                print("\nyou win")
                flag = True
                break
        else:
            flag = True
            print("\nyou lost")
            break
        if not totalMarbles == 1:
            robbedMarblesUser = int(input(f"\nthe pool of remaining marbles is {totalMarbles}. choose number of marbles to take between 1 and {totalMarbles//2}: "))
            totalMarbles -= robbedMarblesUser
            print(f"\nmarbles left after your turn: {totalMarbles}")
            if totalMarbles == 0:
                print("\nyou lost")
                flag = True
        else:
            print("\nyou lost")
            flag = True

if smartStupid == 0 and firstTurn == 1:
    print("\nyou go first.")
    while not flag:
        if not  totalMarbles == 1:
            robbedMarblesUser = int(input(f"\nthe pool of remaining marbles is {totalMarbles}. choose number of marbles to take between 1 and {totalMarbles//2}: "))
            totalMarbles -= robbedMarblesUser
            print(f"\nmarbles left after your turn: {totalMarbles}")
            if totalMarbles == 0:
                print("\nyou lost")
                flag = True
        else:
            flag = True
            print("\nyou lost")
            break
        if not totalMarbles == 1:
            robbedMarblesPC = random.randint(1, totalMarbles//2)
            totalMarbles -= robbedMarblesPC
            print(f"\nPc takes away {robbedMarblesPC} marbles, remaining pool is {totalMarbles} marbles")
            if totalMarbles == 0:
                print("\nyou win")
                flag = True
                break
        else:
            flag = True
            print("\nyou win")
if smartStupid == 1 and firstTurn == 0:
    while not flag:
        if not totalMarbles == 1:
            if not totalMarbles in listPowersOf2 and totalMarbles > 2:
                distance = [0, 0, 0, 0, 0]
                for i in range (len(listPowersOf2)):
                    difference = totalMarbles - listPowersOf2[i]
                    if difference > 0:
                        distance[i] = difference
                robbedMarblesPC = min(m for m in distance if m > 0)
                totalMarbles -= robbedMarblesPC
            else:
                robbedMarblesPC = random.randint(1, totalMarbles // 2)
                totalMarbles -= robbedMarblesPC
            print(f"\nPc takes away {robbedMarblesPC} marbles, remaining pool is {totalMarbles} marbles")
            if totalMarbles == 0:
                print("\nyou win")
                flag = True
                break
        else:
                flag = True
                print("\nyou win")
                break
        if not totalMarbles == 1:
            robbedMarblesUser = int(input(f"\nthe pool of remaining marbles is {totalMarbles}. choose number of marbles to take between 1 and {totalMarbles//2}: "))
            totalMarbles -= robbedMarblesUser
            print(f"\nmarbles left after your turn: {totalMarbles}")
            if totalMarbles == 0:
                print("\nyou lost")
                flag = True
        else:
            print("\nyou lost")
            flag = True
if smartStupid == 1 and firstTurn == 1:
    while not flag:
        if not totalMarbles == 1:
            robbedMarblesUser = int(input(f"\nthe pool of remaining marbles is {totalMarbles}. choose number of marbles to take between 1 and {totalMarbles//2}: "))
            totalMarbles -= robbedMarblesUser
            print(f"\nmarbles left after your turn: {totalMarbles}")
            if totalMarbles == 0:
                print("\nyou lost")
                flag = True
                break
        else:
            print("\nyou lost")
            flag = True
            break
        if not totalMarbles == 1:
                if not totalMarbles in listPowersOf2 and totalMarbles > 2:
                  distance = [0, 0, 0, 0, 0]
                  for i in range (len(listPowersOf2)):
                      difference = totalMarbles - listPowersOf2[i]
                      if difference > 0:
                          distance[i] = difference
                  robbedMarblesPC = min(m for m in distance if m > 0)
                  totalMarbles -= robbedMarblesPC
                else:
                    robbedMarblesPC = random.randint(1, totalMarbles // 2)
                    totalMarbles -= robbedMarblesPC
                print(f"\nPc takes away {robbedMarblesPC} marbles, remaining pool is {totalMarbles} marbles")
                if totalMarbles == 0:
                  print("\nyou win")
                  flag = True
        else:
            flag = True
            print("\nyou win")

#How Nech did it:
#import random

#
# player = input("Player,Enter your name:")
# play_again = True
# pile = 0
# mode = 0
# turn = 0
#
#
# while play_again:
#     generating = False
#     number = []
#     computer_move = 0
#
#     game = input("Start the game[y/n]").lower()
#
#     if game[0] == "y":
#         generating = True
#     else:
#         print("\n:(")
#         play_again = False
#         break
#
#     if generating:
#         print("\nNow it's going to generate a number between 10 and 100 corresponding to initial size of the pile")
#         pile = random.randint(10, 100)
#         print(f"\nThe pile has {pile} marbles")
#
#         print("\nNow it'll be chosen a mode for you, between hard and easy")
#         mode = random.randint(0, 1)
#         if mode == 0:
#             print("\nLucky for you: it's ez mode")
#         else:
#             print("\nIt's hard mode, you are going to lose soon")
#
#         print("\nIt'll chosen be who'll start first")
#         turn = random.randint(0, 1)
#         if turn == 1:
#             player_turn = True
#             computer_turn = False
#             print(f"\n{player} will go first.")
#         else:
#             player_turn = False
#             computer_turn = True
#             print("\nComputer will go first.")
#
#
#     while pile != 0:
#         for i in range(1, 7):
#             z = 2**i-1
#             if z <= pile:
#                 number.append(z)
#         if player_turn:
#             player_move = int(input("\nPlease enter a number of marbles to remove:"))
#             while player_move > pile//2 and player_move <= 0:
#                 print("\nIllegal move")
#                 player_move = int(input("\nPlease enter a number of marbles to remove:"))
#             pile = pile - player_move
#         else:  # computer move
#             if mode == 0:
#                 computer_move = random.randint(1, pile//2)
#             else:
#                 if pile not in number:
#                     computer_move = pile - number[-1]
#                 else:
#                     computer_move = random.randint(1, pile//2)
#
#             print(f"The computer removes {computer_move} marbles")
#             pile = pile - computer_move
#
#         print(f"\nThe number of marbles is {pile}")
#         # switch
#         player_turn = not player_turn
#         computer_move = not computer_turn
#         # for i in range(len(number)):            non serve resettare la lista, si resetta automaticamente
#         #     number.pop(0)
#
#
#         if player_turn:
#             if pile == 1:
#                 winner = "Computer"
#                 break
#
#         if computer_turn:
#             if pile == 1:
#                 winner = player
#                 break
#
#     if winner == player:
#         print(f"\n{player} you won")
#     else:
#         print(f"The computer won")
#
#     restart = input("\nWould like to play again?").lower()
#     if restart[0] == "n" or restart[0] != "y":
#         play_again = False
#         print("\n:(")








