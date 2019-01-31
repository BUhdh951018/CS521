#Geometry: great circle distance

import math

latitude1, longitude1 = eval(input("Enter point 1 (latitude and longitude) in degrees:\n"))
latitude2, longitude2 = eval(input("Enter point 2 (latitude and longitude) in degrees:\n"))

radius = 6371.01

x1 = math.radians(latitude1)
x2 = math.radians(latitude2)
y1 = math.radians(longitude1)
y2 = math.radians(longitude2)

d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("The distance between the two points is", d, "km")