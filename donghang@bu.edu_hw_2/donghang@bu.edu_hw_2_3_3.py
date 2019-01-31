#Geography: estimate areas

import math

la1 = 33.74
x1 = math.radians(la1)
lo1 = -84.55
y1 = math.radians(lo1)
la2 = 28.41
x2 = math.radians(la2)
lo2 = -81.52
y2 = math.radians(lo2)
la3 = 32.17
x3 = math.radians(la3)
lo3 = -81.20
y3 = math.radians(lo3)
la4 = 35.21
x4 = math.radians(la4)
lo4 = -80.96
y4 = math.radians(lo4)
radius = 6371.01


def d(x1, x2, y1, y2):
    return radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))


d1_4 = d(x1, x4, y1, y4)
d1_2 = d(x1, x2, y1, y2)
d1_3 = d(x1, x3, y1, y3)
d2_3 = d(x2, x3, y2, y3)
d3_4 = d(x3, x4, y3, y4)


def area(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return math.sqrt(s * (s - s1) * (s - s2) * (s - s3))


area1 = area(d1_2, d1_3, d2_3)
area2 = area(d1_4, d3_4, d1_3)
sum = area1 + area2

print("The area is", sum)