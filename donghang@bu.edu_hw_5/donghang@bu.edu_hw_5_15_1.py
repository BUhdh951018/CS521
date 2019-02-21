# Sum the digits in an integer using recursion


def sumDigits(n):
    sum = 0

    if len(str(n)) == 1:
        return n
    else:
        return sum + (n % 10) + sumDigits(n // 10)


def main():
    number = input("Please enter an integer:")
    print("The sum of the digits is {0}".format(sumDigits(int(number))))


main()
