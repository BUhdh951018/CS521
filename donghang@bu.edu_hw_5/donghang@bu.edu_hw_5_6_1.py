# Math: pentagonal numbers


def main():

    for i in range(1, 101):
        print("{0:6d}".format(getPentagonalNumbers(i)), end="")
        if i % 10 == 0:
            print(" ")


def getPentagonalNumbers(n):

    number = n * (3 * n - 1) / 2
    return int(number)


main()
