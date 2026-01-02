class Vector:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, x):
        return self.__class__(self.x * x, self.y * x)

    def __truediv__(self, x):
        return self.__class__(self.x / x, self.y / x)

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


def dot(u, v):
    return u.x * v.x + u.y * v.y


x1, y1, x2, y2 = map(float, input().split())
p1, p2 = Vector(x1, y1), Vector(x2, y2)
n = (p2 - p1) / (p2 - p1).norm()

q = int(input())

for _ in range(q):
    p = Vector(*map(float, input().split()))
    p_prj = p1 + n * dot(p - p1, n)
    p_ref = p_prj * 2 - p
    print('{:.10f} {:.10f}'.format(p_ref.x, p_ref.y))

