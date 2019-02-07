#Algebra: solve quadratic equations
import math

a, b, c = eval(input("Enter a, b, c:"))

#discriminant
dis = math.pow(b, 2) - 4 * a * c

if dis < 0:
    print("The equation has no real roots")
elif dis == 0:
    root = -b / (2 * a)
    print("The root is", root)
else:
    root1 = (-b + math.sqrt(dis)) / (2 * a)
    root2 = (-b - math.sqrt(dis)) / (2 * a)
    print("The roots are", format(root1, ".6f"), "and", format(root2, ".5f"))