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

class Segment:
    def __init__(self, p1=Vector(0, 0), p2=Vector(1, 1)):
        self.p1 = p1
        self.p2 = p2

def is_orthogonal(*args, **kwargs):
    # input two vectors with the startpoint (0, 0)
    if len(args) == 2:
        v1, v2 = args
        return v1.dot(v2) == 0
    # input two vectors with the startpoint (a1, b1) and endpoint (a2, b2)
    elif len(args) == 4:
        a1, a2, b1, b2 = args
        return is_orthogonal(a1 - a2, b1 - b2)
    # input two segments
    elif len(kwargs) == 2:
        v1 = kwargs['s1'].p1 - kwargs['s1'].p2
        v2 = kwargs['s2'].p1 - kwargs['s2'].p2
        return v1.dot(v2) == 0
    else:
        raise ArgsError

def is_parallel(*args, **kwargs):
    # input two vectors with the startpoint (0, 0)
    if len(args) == 2:
        v1, v2 = args
        return v1.cross(v2) == 0
    # input two vectors with the startpoint (a1, b1) and endpoint (a2, b2)
    elif len(args) == 4:
        a1, a2, b1, b2 = args
        return is_parallel(a1 - a2, b1 - b2)
    # input two segments
    elif len(kwargs) == 2:
        v1 = kwargs['s1'].p1 - kwargs['s1'].p2
        v2 = kwargs['s2'].p1 - kwargs['s2'].p2
        return v1.cross(v2) == 0
    else:
        raise ArgsError

from sys import stdin

def read_and_print_results(n):
    for _ in range(n):
        line = stdin.readline().strip().split()
        p0 = Vector(int(line[0]), int(line[1]))
        p1 = Vector(int(line[2]), int(line[3]))
        p2 = Vector(int(line[4]), int(line[5]))
        p3 = Vector(int(line[6]), int(line[7]))
        s1 = Segment(p0, p1)
        s2 = Segment(p2, p3)
        if is_parallel(s1=s1, s2=s2):
            print('2')
        elif is_orthogonal(s1=s1, s2=s2):
            print('1')
        else:
            print('0')

n = int(input())
read_and_print_results(n)
