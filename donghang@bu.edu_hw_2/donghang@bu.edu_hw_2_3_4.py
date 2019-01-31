#Geotery: area of a pentagon
import math

side = eval(input("Enter the side:"))

area = (5 * math.pow(side, 2)) / (4 * math.tan(math.pi / 5))

#The textbook show the wrong answer again
print("The area of the pentagon is", area)
