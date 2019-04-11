# Geometry: n-sided regular polygon
import math


class RegularPolygon:

    def __init__(self, n=3, side=1.0, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y


    def getN(self):
        return self.__n

    def setN(self, n):
        self.__n = n

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getPerimeter(self):
        return self.getSide() * self.getN()

    def getArea(self):
        return (self.getN() * math.pow(self.getSide(), 2)) / (4 * math.tan(math.pi/self.getN()))


def main():
    poly1 = RegularPolygon(6, 4)
    poly2 = RegularPolygon(10, 4, 5.6, 7.8)
    print("first polygon perimeter:{0} area:{1:.2f}".format(poly1.getPerimeter(), poly1.getArea()))
    print("second polygon perimeter:{0} area:{1:.2f}".format(poly2.getPerimeter(), poly2.getArea()))


if __name__ == '__main__':
    main()
