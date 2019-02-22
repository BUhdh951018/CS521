# Statistics: compute deviation
import math


# Compute the standard deviation of values
def deviation(x):
    m = mean(x)
    sum = 0
    for i in range(len(x)):
        sum += math.pow(x[i] - m, 2)
    d = math.sqrt(sum / (len(x) - 1))
    print("The standard deviation is {0:.5f}".format(d))


# Compute the mean of a list of values
def mean(x):
    n = len(x)
    sum = 0
    for i in range(n):
        sum += x[i]
    print("The mean is {0:.2f}".format(sum / n))
    return sum / n


def main():
    number = input("Enter number:").split()
    lst = [eval(x) for x in number]
    deviation(lst)


if __name__ == '__main__':
    main()