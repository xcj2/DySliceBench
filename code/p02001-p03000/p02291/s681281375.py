from sys import stdin

class Vector:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # usually cross operation return Vector but it returns scalor
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def norm(self):
        return self.x * self.x + self.y * self.y

    def abs(self):
        return math.sqrt(self.norm())

class Point(Vector):
    def __init__(self, *args, **kargs):
        return super().__init__(*args, **kargs)

class Segment:
    def __init__(self, p1=Point(0, 0), p2=Point(1, 1)):
        self.p1 = p1
        self.p2 = p2

def project(s, p):
    base = s.p2 - s.p1
    hypo = p - s.p1
    r = hypo.dot(base) / base.norm()
    return s.p1 + base * r

def reflect(s, p):
    return p + (project(s, p) - p) * 2

def read_and_print_results(s, n):
    for _ in range(n):
        line = stdin.readline().strip().split()
        p = Vector(int(line[0]), int(line[1]))
        x = reflect(s, p)
        print('{0:0.10f} {1:0.10f}'.format(x.x, x.y))

x1, y1, x2, y2 = input().split()
p1 = Point(int(x1), int(y1))
p2 = Point(int(x2), int(y2))
s = Segment(p1, p2)
n = int(input())
read_and_print_results(s, n)
