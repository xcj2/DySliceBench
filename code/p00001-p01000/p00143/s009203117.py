class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    @staticmethod
    def cross_product(point1, point2):
        return point1.x * point2.y - point1.y * point2.x


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.point1 = Vector(x1, y1)
        self.point2 = Vector(x2, y2)
        self.point3 = Vector(x3, y3)

    def is_contain(self, point):
        line1 = point - self.point1
        line2 = self.point2 - self.point1
        direct1 = Vector.cross_product(line1, line2)

        line1 = point - self.point2
        line2 = self.point3 - self.point2
        direct2 = Vector.cross_product(line1, line2)

        line1 = point - self.point3
        line2 = self.point1 - self.point3
        direct3 = Vector.cross_product(line1, line2)

        if 0 < direct1 and 0 < direct2 and 0 < direct3:
            return 1
        elif direct1 < 0 and direct2 < 0 and direct3 < 0:
            return 1
        else:
            return -1


for _ in range(int(input())):
    data = [int(item) for item in input().split(" ")]

    triangle = Triangle(data[0], data[1], data[2], data[3], data[4], data[5])
    altair_point = Vector(data[6], data[7])
    vega_point = Vector(data[8], data[9])

    is_contain1 = triangle.is_contain(altair_point)
    is_contain2 = triangle.is_contain(vega_point)
    result = is_contain1 * is_contain2

    if result == -1:
        print("OK")
    else:
        print("NG")

