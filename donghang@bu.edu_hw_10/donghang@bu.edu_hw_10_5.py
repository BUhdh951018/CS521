# upgrade bubble sort


def sort_list(x):
    for i in range(0, len(x)):
        for j in range(i, len(x)):
            first = x[i]
            second = x[j]
            if first > second:
                first, second = second, first
                x[i] = first
                x[j] = second
    return x


def rearrange(x):
    j = -1
    n = 0
    for i in range(len(x)):
        if x[i] > 0:
            j += 1
            x[j], x[i] = x[i], x[j]
    for m in x:
        if m < 0:
            break
        n += 1
    temp = len(x) - n
    for p in range(temp):
        for q in range(0, temp-p-1):
            if x[q+n] > x[q+n+1]:
                x[q+n], x[q+n+1] = x[q+n+1], x[q+n]
    return x


def main():
    arr = input("Please enter numbers(Separate by spaces):")
    x_list = list(arr.split())
    j = 0
    for i in x_list:
        x_list[j] = int(i)
        j = j + 1
    print("Input:", x_list)
    arr = sort_list(x_list)
    x_arr = rearrange(arr)
    print("Output:", x_arr)


if __name__ == '__main__':
    main()
