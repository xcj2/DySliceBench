import math

class Point():
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inner_product(self, vec):
        return self.x*vec.x + self.y*vec.y

    def outer_product(self, vec):
        return self.x*vec.y - self.y*vec.x

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

n = int(input())
points = []
for i in range(n):
    x, y = list(map(int, input().split(' ')))
    points.append(Point(x, y))
points.extend(points[0:2])

is_convex = True
for i in range(1, n+1):
    a, b, c = points[i-1:i+2]
    vec1, vec2 = Vector(a.x - b.x, a.y - b.y), Vector(c.x - b.x, c.y - b.y)
    theta = math.degrees(math.atan2(vec2.outer_product(vec1), vec2.inner_product(vec1)))
    if theta < 0:
        is_convex = False
        break

if is_convex:
    print(1)
else:
    print(0)
