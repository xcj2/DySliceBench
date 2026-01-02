from math import sin, cos, atan2

def sgn(x, eps=1e-10):
    if x < -eps: return -1
    if -eps <= x <= eps: return 0
    if eps < x: return 1

class Vector():
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def arg(self):
        return atan2(self.y, self.x)

    def norm(self):
        return (self.x**2 + self.y**2)**0.5

    def rotate(self, t):
        nx = self.x * cos(t) - self.y * sin(t)
        ny = self.x * sin(t) + self.y * cos(t)
        return Vector(nx, ny)

    def counter(self):
        nx = -self.x
        ny = -self.y
        return Vector(nx, ny)

    def times(self, k):
        nx = self.x * k
        ny = self.y * k
        return Vector(nx, ny)

    def unit(self):
        norm = self.norm()
        nx = self.x / norm
        ny = self.y / norm
        return Vector(nx, ny)

    def normal(self):
        norm = self.norm()
        nx = -self.y / norm
        ny = self.x / norm
        return Vector(nx, ny)

    def add(self, other): #Vector, Vector -> Vector
        nx = self.x + other.x
        ny = self.y + other.y
        return Vector(nx, ny)

    def sub(self, other):
        nx = self.x - other.x
        ny = self.y - other.y
        return Vector(nx, ny)

    def dot(self, other): #Vector, Vector -> int
        return self.x * other.x + self.y * other.y

    def cross(self, other): #Vector, Vector -> int
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return '{:.9f}'.format(self.x) + ' ' + '{:.9f}'.format(self.y)

class Line():
    def __init__(self, bgn=Vector(), end=Vector()):
        self.bgn = bgn
        self.end = end

    def build(self, a, b, c): #ax + by == 1
        assert sgn(a) != 0 or sgn(b) != 0
        if sgn(b) == 0:
            self.bgn = Vector(-c / a, 0.0)
            self.end = Vector(-c / a, 1.0)
        else:
            self.v = Vector(0, -c / b)
            self.u = Vector(1.0, -(a + b) / b)

    def vec(self):
        return self.end.sub(self.bgn)

    def projection(self, point):
        v = self.vec()
        u = point.sub(self.bgn)
        k = v.dot(u) / v.norm()
        h = v.unit().times(k)
        return self.bgn.add(h)

    def refrection(self, point):
        proj = self.projection(point)
        return proj.sub(point).times(2).add(point)

    def is_orthogonal(self, other):
        v = self.vec()
        u = other.vec()
        if sgn(v.dot(u)) == 0:
            return True
        else:
            return False

    def is_parallel(self, other):
        v = self.vec()
        u = other.vec()
        if sgn(v.cross(u)) == 0:
            return True
        else:
            return False

q = int(input())
for _ in range(q):
    xp0, yp0, xp1, yp1, xp2, yp2, xp3, yp3 = map(int, input().split())
    p0 = Vector(xp0, yp0)
    p1 = Vector(xp1, yp1)
    p2 = Vector(xp2, yp2)
    p3 = Vector(xp3, yp3)
    s1 = Line(p0, p1)
    s2 = Line(p2, p3)
    if s1.is_parallel(s2):
        print(2)
    elif s1.is_orthogonal(s2):
        print(1)
    else:
        print(0)
