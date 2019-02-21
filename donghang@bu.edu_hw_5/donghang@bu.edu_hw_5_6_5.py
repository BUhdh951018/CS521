# Sort three numbers


def displaySortedNumbers(num1, num2, num3):
    if num1 > num2:
        temp = num1
        num1 = num2
        num2 = temp
    if num1 > num3:
        temp = num1
        num1 = num3
        num3 = temp
    if num2 > num3:
        temp = num2
        num2 = num3
        num3 = temp

    print("The sorted numbers are {0:.2f} {1:.2f} {2:.2f}".format(num1, num2, num3))


def main():
    num1, num2, num3 = eval(input("Enter three numbers:"))
    displaySortedNumbers(num1, num2, num3)


main()
