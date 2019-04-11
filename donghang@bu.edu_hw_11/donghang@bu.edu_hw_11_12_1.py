# The Triangle class
import math


class GeometricObject:

    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + \
               " and filled: " + str(self.__filled)


class Triangle(GeometricObject):

    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def getSide2(self):
        return self.__side2

    def getSide3(self):
        return self.__side3

    def getArea(self):
        p = (self.getSide1() + self.getSide2() + self.getSide3()) / 2
        return math.pow(p * (p - self.getSide1()) * (p - self.getSide2()) * (p - self.getSide3()), 0.5)

    def getPerimeter(self):
        return self.getSide1() + self.getSide2() + self.getSide3()

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + \
        str(self.__side2) + " side3 = " + str(self.__side3)


def main():
    side1, side2, side3 = eval(input("Please enter three sides of a triangle:"))
    color = input("Please enter a color:")
    isfilled = int(input("Is the triangle filled?(0/1):"))

    tri = Triangle(side1, side2, side3)
    tri.setColor(color)
    tri.setFilled(isfilled)

    print("Area:", tri.getArea())
    print("Perimeter:", tri.getPerimeter())
    print("color:", tri.getColor())

    if tri.isFilled():
        print("Is filled: true")
    else:
        print("Is filled: false")


if __name__ == '__main__':
    main()
