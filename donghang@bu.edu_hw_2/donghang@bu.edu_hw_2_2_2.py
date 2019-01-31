#Compute the volume of a cylinder

import math

radius, length = eval(input("Enter the radius and length of a cylinder:"))

area = radius * radius * math.pi
volume = area * length

#There is mistake on the textbook the answer of the area should be
# 95.0332 in four digital number
print("The area is", "%.4f" % area)
print("The volume is", "%.1f" % volume)