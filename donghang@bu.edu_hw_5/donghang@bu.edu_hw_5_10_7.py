# Count single digits
import random


def main():
    ra_list = []
    for i in range(1000):
        ra_list.append(random.randint(0, 9))
    count_numbers(ra_list)


def count_numbers(list):
    count_list = []
    for j in range(10):
        count_list.append(list.count(j))
        print("The number of {0:d} is {1:d}".format(j, count_list[j]))


if __name__ == '__main__':
    main()
