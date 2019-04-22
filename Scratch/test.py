import time
from Random import Random
from Rander import Rander
import random


def around():
    temp = random.randint(-100, 100)

    # generate numbers around winning number
    if temp < 0:
        temp = 0 - (temp % 4)
    else:
        temp = temp % 4

    # avoid the number as winning number
    if temp == 0:
        temp += 1

    return temp


def check(win, t):
    if t == win[0]:
        t += 1
    elif t == win[1]:
        t += 1
    return t


def main():
    money = {0: '$1', 1: '$2', 2: '$5', 3: '$10', 4: '$20', 5: '$50', 6: '$100', 7: '$200', 8: '$500', 9: '$1000',
             10: '$2000', 11: '$5000', 12: '$10000', 13: '$20000', 14: '$50000'}

    seed1 = Rander()
    seed2 = Rander()
    your_number = []
    winning_number = []
    prize = []

    # generate the first winning number
    win1 = seed1.rander_half(10)
    winning_number.append(win1 % 20)

    # avoid the number is zero
    i = 1
    while i == 1:
        if winning_number[0] > 0:
            break
        else:
            win1 = seed1.rander_half(10)
            winning_number[0] = win1 % 20

    # generate the second winning number
    win2 = seed2.rander_half(10)
    winning_number.append(win2 % 20)
    i = 1
    while i == 1:
        # avoid the second number is same as the first
        if winning_number[1] == winning_number[0] or winning_number[1] == 0:
            win2 = seed2.rander_half(10)
            winning_number[1] = win2 % 20
        else:
            break

    # print(winning_number)

    # whether win or not
    x = Random()
    pro = x.random_LCG()

    if pro < 0.1:
        print("WIN!")
        your_number.append(winning_number[0])
        for j in range(3):
            temp = around()

            temp_your = winning_number[1] + temp
            temp_your = check(winning_number, temp_your)

            for l in your_number:
                while i == 1:
                    if temp_your == l:
                        temp = around()
                        temp_your = winning_number[1] + temp
                        temp_your = check(winning_number, temp_your)
                    else:
                        break

            your_number.append(temp_your)
    else:
        # your_number around the two winning number
        for m in range(2):
            for j in range(2):
                temp = around()

                temp_your = winning_number[m] + temp
                # avoid the number is negative or zero
                if temp_your < 0 or temp_your == 0:
                    temp_your += 3

                temp_your = check(winning_number, temp_your)

                for l in your_number:
                    while i == 1:
                        if temp_your == l:
                            temp = around()
                            temp_your = winning_number[m] + temp
                            # avoid the number is negative or zero
                            if temp_your < 0 or temp_your == 0:
                                temp_your += 3

                            temp_your = check(winning_number, temp_your)
                        else:
                            break

                your_number.append(temp_your)

    # other random your numbers
    for q in range(6):
        oth_your = x.random_LCG()
        oth_your = int(oth_your * 1000000000 % 20)
        # avoid the number is negative or zero
        if oth_your < 0 or oth_your == 0:
            oth_your += 3

        oth_your = check(winning_number, oth_your)

        for l in your_number:
            while i == 1:
                if oth_your == l:
                    oth_your = x.random_LCG()
                    oth_your = int(oth_your * 1000000000 % 20)
                    # avoid the number is negative or zero
                    if oth_your < 0 or oth_your == 0:
                        oth_your += 3

                    oth_your = check(winning_number, oth_your)
                else:
                    break

        your_number.append(oth_your)

    # random winning money
    for p in range(10):
        win_money = x.random_LCG()
        win_money = int(win_money * 1000000000 % 15)
        prize.append(money[win_money])

    print("__________________________________________________________________________")
    print("|\033[4;33;44m 2 ways to PLAY! 2 ways to WIN! \033[0m                                        |")
    print("|\033[4;33;44m 1:Match any of YOUR NUMBERS to either WINNING NUMBERS, win prize shown \033[0m|")
    print("|\033[4;33;44m 2:Match 3 like prize amounts, win that amount \033[0m                         |")

    print("|YOUR NUMBERS                                                            |")
    print("|", end="")
    for i in your_number:
        print("{0:<6}".format(i), end=" ")
    print("  |")
    print("|", end="")
    for j in prize:
        print("{0:6}".format(j), end=" ")
    print("  |")

    print("|WINNING NUMBERS                                                         |")
    print("|", end="")
    for x in winning_number:
        print("\033[0;30;40m {0:<2} \033[0m".format(x), end=" ")
    print("                                                              |")
    print("__________________________________________________________________________")


main()
