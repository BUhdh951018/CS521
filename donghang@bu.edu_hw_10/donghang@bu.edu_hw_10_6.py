# DNA sequence


def complementary(x, y):
    dict = {'A': 'T', 'C': 'G', "G": "C", "T": "A"}
    re_x = []
    for i in x:
        re_x.append(dict[i])
    rex_str = "".join(re_x)
    if rex_str == y[::-1]:
        return True
    else:
        return False


def main():
    s_str = input("Please enter two DNA sequence seperated by space:").split()
    x = s_str[0]
    y = s_str[1]
    if complementary(x, y):
        print("{0:4} and {1:4} are complementary".format(x, y))
    else:
        print("{0:4} and {1:4} are not complementary".format(x, y))


if __name__ == '__main__':
    main()
