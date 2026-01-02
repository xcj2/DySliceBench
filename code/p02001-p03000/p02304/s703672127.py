from sys import stdin
import math

class Vector:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # can't  apply "number * Vector" but "Vector * number"
    def __mul__(self, k):
        return Vector(self.x * k, self.y * k)

    def __truediv__(self, k):
        return Vector(self.x / k, self.y / k)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.yb

    def __lt__(self, other):
        return self.x < other.x and self.y < other.yb

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

    def rotate(self, theta):
        return Vector(self.x * math.cos(theta)
                               - self.y * math.sin(theta),
                               self.x * math.sin(theta)
                               + self.y * math.cos(theta))

class Point(Vector):
    def __init__(self, *args, **kargs):
        return super().__init__(*args, **kargs)

class Segment:
    def __init__(self, p1=Point(0, 0), p2=Point(1, 1)):
        self.p1 = p1
        self.p2 = p2

class Line(Segment):
    def __init__(self, *args, **kargs):
        return super().__init__(*args, **kargs)

class EndPoint:
    def __init__(self, p1, p2):
        self.point = p1
        self.otherend = p2
        if p1.x == p2.x:
            if p1.y > p2.y:
                self.type = 2 # 'Vertical Top'
            else:
                self.type = 0 # 'Vertical Bottom'
        elif p1.y == p2.y:
            if p1.x < p2.x:
                self.type = 1 # 'Horizontal Left'
            else:
                self.type = 3 # 'Horizontal Right'

def manhattan_geometry(S):
    end_points = []
    count = 0
    for i in S:
        ep1 = EndPoint(i.p1, i.p2)
        ep2 = EndPoint(i.p2, i.p1)
        if ep1.type != 3:
            end_points.append(ep1)
        if ep2.type != 3:
            end_points.append(ep2)

    end_points.sort(key=lambda ep: (ep.point.y, ep.type, ep.point.x))
    T = set({})
    for i in end_points:
        if i.type == 2: # 'Vertical Top'
            T.remove(i.point.x)
        if i.type == 0: # 'Vertical Bottom'
            T.add(i.point.x)
        if i.type == 1: # 'Horizontal Left'
            inclueded_x = {j for j in T if j >= i.point.x and j <= i.otherend.x}
            count = count + len(inclueded_x)
    return count

def read_segments(n):
    S = []
    for _ in range(n):
        line = stdin.readline().strip().split()
        p0 = Vector(int(line[0]), int(line[1]))
        p1 = Vector(int(line[2]), int(line[3]))
        s = Segment(p0, p1)
        S.append(s)
    return S

def __main():
    n = int(input())
    S = read_segments(n)
    count = manhattan_geometry(S)
    print(count)

if __name__ == '__main__':
    __main()
