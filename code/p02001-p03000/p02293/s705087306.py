import math

EPS = 1e-10

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        # + 演算子での挙動を指定
        return Point(self.x+point.x, self.y+point.y)

    def __sub__(self, point):
        # - 演算子での挙動を指定
        return Point(self.x-point.x, self.y-point.y)

    def __mul__(self, a):
        # * 演算子での挙動を指定
        return Point(a*self.x, a*self.y)

    def __truediv__(self, a):
        # / 演算子での挙動を指定
        return Point(self.x/a, self.y/a)

    def __abs__(self):
        # abs関数での挙動を指定
        return math.sqrt(self.norm())

    def norm(self):
        return self.x**2+self.y**2

    def __eq__(self, point):
        # == 演算子での挙動を指定
        return abs(self.x-point.x) < EPS and abs(self.y-point.y) <EPS

def dot(a, b):
    return a.x*b.x+a.y*b.y

def cross(a, b):
    return a.x*b.y - a.y*b.x

def isOrthogonal(a, b):
    return dot(a, b) == 0

def isParallel(a, b):
    return cross(a, b) == 0

if __name__ == '__main__':
    from sys import stdin
    input = stdin.readline

    q = int(input())

    for _ in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
        a = Point(x0, y0)-Point(x1, y1)
        b = Point(x2, y2)-Point(x3, y3)
        if isOrthogonal(a, b):
            print(1)
        elif isParallel(a, b):
            print(2)
        else:
            print(0)

