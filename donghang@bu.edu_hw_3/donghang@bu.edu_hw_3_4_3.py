#Algebra: solve 2 * 2 linear equations

a, b, c, d, e, f= eval(input("Enter a, b, c, d, e, f:"))

temp = a * d - b * c

if temp == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / temp
    y = (a * f - e * c) / temp
    print("x is", x, "and y is", y)