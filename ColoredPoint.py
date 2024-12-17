class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __str__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"

    def __eq__(self, other):
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return (self.x, self.y, self.color) == (other.x, other.y, other.color)

    def __ne__(self, other):
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.x, self.y, self.color))


if __name__ == "__main__":
    point1 = ColoredPoint(1, 2, 'red')
    point2 = ColoredPoint(1, 2, 'red')
    point3 = ColoredPoint(3, 4, 'blue')

    print(point1)

    print(point1 == point2)
    print(point1 != point3)

    points_dict = {
        point1: "This is point 1",
        point3: "This is point 3"
    }

    print(points_dict[point1])
    print(points_dict[point3])

    print(hash(point1))
