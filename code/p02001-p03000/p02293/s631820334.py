class Point(object):
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector(object):
    __slots__ = ["p1", "p2", "x", "y"]

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y

    def dot(self, other: "Vector"):
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector"):
        return self.x * other.y - self.y * other.x


if __name__ == "__main__":
    import sys
    answer = []
    append = answer.append
    input()
    for x1, y1, x2, y2, x3, y3, x4, y4 in (map(int, l.split()) for l in sys.stdin):
        vector1 = Vector(Point(x1, y1), Point(x2, y2))
        vector2 = Vector(Point(x3, y3), Point(x4, y4))
        if vector1.dot(vector2) == 0:
            append(1)
        elif vector1.cross(vector2) == 0:
            append(2)
        else:
            append(0)

    print(*answer, sep="\n")
