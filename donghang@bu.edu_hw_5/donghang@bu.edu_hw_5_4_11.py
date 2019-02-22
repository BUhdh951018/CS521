# Find the number of days in a month


days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
names = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]


def main():
    month = eval(input("Please enter the month:"))
    year = eval(input("Please enter the year:"))

    days_month = days[month - 1]

    if month == 2:
        if isleap(year):
            days_month += 1

    print("{0:s} {1:d} has {2:d} days".format(names[month - 1], year, days_month))


def isleap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()