# Display numbers in a pyramid pattern


def main():
    n = 8
    for i in range(1, 8 + 1):
        for m in range(n+1, 1, -1):
            print('    ', end="")
        for j in range(0, i-1, 1):
            print(format(pow(2, j), ">3"), end=" ")
        for k in range(i-1, -1, -1):
            print(format(pow(2, k), ">3"), end=" ")
        print()
        n -= 1
    print()


if __name__ == '__main__':
    main()
