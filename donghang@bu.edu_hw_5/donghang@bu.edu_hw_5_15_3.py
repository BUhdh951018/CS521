# Compute greatest common divisor using recursion


def gcd(m, n):
    m = int(m)
    n = int(n)
    temp = m % n
    if temp == 0:
        return n
    else:
        return gcd(n, temp)


def main():

    number = input("Please enter teo integers:").split()
    lst = []
    for i in number:
        lst.append(i)
    print("The gcd of the numbers is {0:d}".format(gcd(lst[0], lst[1])))


main()
