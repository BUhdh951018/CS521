#Geometry: area of a regular polygon
import math

number = eval(input("Enter the number of sides:"))
side = eval(input("Enter the side:"))

area = (number * math.pow(side, 2)) / (4 * math.tan(math.pi / number))
#The textbook shows the wrong answer the third times
print("The area of the polygon is", area)