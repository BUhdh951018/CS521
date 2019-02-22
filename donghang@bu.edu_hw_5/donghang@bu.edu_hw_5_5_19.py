# Display a pyramid


def main():
    number = eval(input("Enter the number of lines:"))
    n = number
    for i in range(1, number + 1):
        for m in range(n+1, 1, -1):
            print('  ', end="")
        for j in range(i, 1, -1):
            print(j, end=" ")
        for k in range(1, i+1, 1):
            print(k, end=" ")
        print()
        n -= 1
    print()


if __name__ == '__main__':
    main()
