# Sum elements column by column


def get_martix():
    matrix = []

    input0 = input("Enter a 3-by-4 matrix row for row 0:").split()
    input1 = input("Enter a 3-by-4 matrix row for row 1:").split()
    input2 = input("Enter a 3-by-4 matrix row for row 2:").split()

    row0 = [eval(x) for x in input0]
    row1 = [eval(x) for x in input1]
    row2 = [eval(x) for x in input2]

    for i in range(1):
        matrix.append(row0)
        matrix.append(row1)
        matrix.append(row2)

    return matrix


def sum(matrix, col):
    sum = 0
    for i in range(3):
        sum += matrix[i][col]

    return sum


def main():

    m = get_martix()
    print("Sum of the elements for column 0 is {0:.1f}".format(sum(m, 0)))
    print("Sum of the elements for column 1 is {0:.1f}".format(sum(m, 1)))
    print("Sum of the elements for column 2 is {0:.1f}".format(sum(m, 2)))
    print("Sum of the elements for column 3 is {0:.1f}".format(sum(m, 3)))


main()
