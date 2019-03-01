# Financial application: compute furture tuituion


def main():
    tuition = 10000
    increase = 1.05
    ten_tuition(tuition, increase)
    four_worth(tuition, increase)


def ten_tuition(tuition, increase):
    year_tuition = tuition
    for i in range(10):

        print("The tuition of the {0:2} year is {1:.2f}".format(i+1, year_tuition))
        year_tuition = year_tuition * increase


def four_worth(tuition, increase):
    worth = tuition * (1 + increase + increase**2 + increase**3)
    print("The total cost of four years' worth of tuition is {0}".format(worth))


if __name__ == '__main__':
    main()
