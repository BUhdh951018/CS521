# The Rectangle class


class Rectangle:

    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)


def main():
    rec1 = Rectangle(4, 40)
    rec2 = Rectangle(3.5, 35.7)
    print("{0:5} {1:6}   {2:6} {3:5}".format("width", "height", "area", "perimeter"))
    print("{0:5} {1:6} {2:6} {3:10}".format(rec1.width, rec1.height, rec1.getArea(), rec1.getPerimeter()))
    print("{0:5} {1:6} {2:6.2f} {3:10}".format(rec2.width, rec2.height, rec2.getArea(), rec2.getPerimeter()))


if __name__ == '__main__':
    main()
