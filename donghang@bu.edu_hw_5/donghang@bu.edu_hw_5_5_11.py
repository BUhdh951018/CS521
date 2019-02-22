# Find the two highest scores


def main():
    number = eval(input("Please enter the number of the students:"))

    score = input("Please enter the score of each students:").split()
    lst = [eval(x) for x in score]

    get_order(lst)

    print(lst[number - 1], lst[number - 2])


def get_order(list):
    n = len(list)

    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


if __name__ == '__main__':
    main()
