class Point(object):
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, s: int):
        return Point(self.x * s, self.y * s)

    def project(self, vector: "Vector") -> "Point":
        return (vector * (Vector(vector.p1, self).dot(vector) / vector.norm)).p2

    def reflect(self, vector: "Vector") -> "Point":
        return self + (self.project(vector) - self) * 2


class Vector(object):
    __slots__ = ["p1", "p2", "x", "y", "norm", "abs"]

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y
        self.norm = self.x ** 2 + self.y ** 2
        self.abs = abs(self.x + self.y)

    def __mul__(self, s):
        return Vector(self.p1, Point(self.p1.x + self.x * s, self.p1.y + self.y * s))

    def __lt__(self, other: "Vector"):
        return other.abs > self.abs

    def __gt__(self, other: "Vector"):
        return other.abs < self.abs

    def dot(self, other: "Vector"):
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector"):
        return self.x * other.y - self.y * other.x


if __name__ == "__main__":
    a = list(map(int, input().split()))
    p1, p2 = Point(*a[:2]), Point(*a[2:])
    vector1 = Vector(p1, p2)
    for p3 in (Point(*map(int, input().split())) for _ in [0]*int(input())):
        vector2 = Vector(p1, p3)
        if vector1.cross(vector2) > 0:
            print("COUNTER_CLOCKWISE")
        elif vector1.cross(vector2) < 0:
            print("CLOCKWISE")
        elif vector1.dot(vector2) < 0:
            print("ONLINE_BACK")
        elif vector1 < vector2:
            print("ONLINE_FRONT")
        else:
            print("ON_SEGMENT")
