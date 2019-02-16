# Count occurrence of numbers


def main():
    end_of_input = False

    while not end_of_input:
        number = input("Enter integers between 1 and 100(end with 0):").split()
        lst = [eval(x) for x in number]

        for i in lst:
            if i == 0:
                end_of_input = True

        get_order(lst)

        c = 0
        for element in lst:
            m = get_count(lst, element)
            if m > 1:
                str = 'times'
            else:
                str = 'time'

            if c == 0:
                print("{0} occurs {1} {2}".format(element, m, str))
                c += 1
            elif c > 0:
                if lst[c] == lst[c-1]:
                    c += 1
                else:
                    print("{0} occurs {1} {2}".format(element, m, str))
                    c += 1


def get_count(list, n):
    return list.count(n)


def get_order(list):

    n = len(list)

    for i in range(n-1):
        for j in range(0, n-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


main()
