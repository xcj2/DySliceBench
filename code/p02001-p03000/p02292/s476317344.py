import math

EPS = 1e-10

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0

class Segment():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

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

def project(s, p):
    #s: Segment(), p: Point()
    base = s.p2 - s.p1
    r = dot(p-s.p1, base)/base.norm()
    return s.p1+base*r

def reflect(s, p):
    return p+(project(s, p)-p)*2

def get_distance(a, b):
    return abs(a-b)

def get_distance_lp(l, p):
    return abs(cross(l.p2-l.p1, p-l.p1)/abs(l.p2-l.p1))

def get_distance_sp(s, p):
    if dot(s.p2-s.p1, p-s.p1) < 0:
        return abs(p-s.p1)
    if dot(s.p1-s.p2, p-s.p2) < 0:
        return abs(p-s.p2)
    return get_distance_lp(s, p)

def intersect(s1, s2):
    return True
    
def get_distance(s1, s2):
    if intersect(s1, s2):
        return 0
    return min([get_distance_sp(s1, s2.p1), get_distance_sp(s1, s2.p2),
                get_distance_sp(s2, s1.p1), get_distance_sp(s2, s1.p2)])

def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if cross(a, b) > EPS:
        return COUNTER_CLOCKWISE
    if cross(a, b) < -EPS:
        return CLOCKWISE
    if dot(a, b) < -EPS:
        return ONLINE_BACK
    if a.norm() < b.norm():
        return ONLINE_FRONT
    return ON_SEGMENT


if __name__ == '__main__':
    from sys import stdin
    input = stdin.readline

    x0, y0, x1, y1 = map(int, input().split())
    p0 = Point(x0, y0)
    p1 = Point(x1, y1)

    q = int(input())
    for _ in range(q):
        x2, y2 = map(int, input().split())
        p2 = Point(x2, y2)
        # このccw関数の書き方は、この問題では冗長な書き方となるが、
        # 今後のために上記のような形にしている。
        ans = ccw(p0, p1, p2)
        if ans == -2:
            print('ONLINE_FRONT')
        if ans == -1:
            print('CLOCKWISE')
        if ans == 0:
            print('ON_SEGMENT')
        if ans == 1:
            print('COUNTER_CLOCKWISE')
        if ans == 2:
            print('ONLINE_BACK')

