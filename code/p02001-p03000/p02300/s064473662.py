from collections import deque
from functools import singledispatch
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

class Circle():
    def __init__(self, c, r):
        self.c = c
        self.r = r

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

    def __lt__(self, p):
        # < 演算子での挙動を指定、これによってsortで並び替えが可能になる。
        # boolean = 
        return (self.x < p.x) if (self.x != p.x) else (self.y < p.y)

    def __eq__(self, p):
        # == 演算子での挙動を指定
        return abs(self.x-p.x) < EPS and abs(self.y-p.y) <EPS

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

@singledispatch
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
    
@get_distance.register(Segment)
def _(s1, s2):
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

@singledispatch
def intersect(p1, p2, p3, p4):
    return (ccw(p1, p2, p3)*ccw(p1, p2, p4) <= 0
            and ccw(p3, p4, p1)*ccw(p3, p4, p2) <= 0)

@intersect.register(Segment)
def _(s1, s2):
    return intersect(s1.p1, s1.p2, s2.p1, s2.p2)

def get_cross_point(s1, s2):
    base = s2.p2 - s2.p1
    d1 = abs(cross(base, s1.p1-s2.p1))
    d2 = abs(cross(base, s1.p2-s2.p1))
    t = d1/(d1+d2)
    return s1.p1 + (s1.p2-s1.p1)*t

def get_cross_points(c, l):
    # 次の行のコメントのコードは、新しいintersect関数を作る必要があり(おそらくpython3.7以上必須)、手間取るので割愛します。
    # assert(intersect(c, l))
    pr = project(l, c.c)
    e = (l.p2 - l.p1)/abs(l.p2-l.p1)
    base = (c.r**2-(pr-c.c).norm())**0.5
    return (pr+e*base, pr-e*base)

def arg(p):
    return math.atan2(p.y, p.x)

def polar(a, r):
    return Point(math.cos(r)*a, math.sin(r)*a)

def get_cross_points_(c1, c2):
    # 関数名かぶるので、_つけました。
    # python3.7以上でsingledispatchを使えば同じ関数名も可能ですが、
    # atcoderのpython3.4も想定しているため、関数名を変えておきます。
    # assert(intersect(c, c))
    d = abs(c1.c-c2.c)
    a = math.acos((c1.r**2+d**2-c2.r**2)/(2*c1.r*d))
    t = arg(c2.c-c1.c)
    return (c1.c+polar(c1.r, t+a), c1.c+polar(c1.r, t-a))

def contains(g, p):
    # gは多角形の頂点を順番に並べたリスト/タプル
    n = len(g)
    x = False
    for i in range(n):
        a = g[i]-p
        b = g[(i+1)%n]-p
        if abs(cross(a, b)) < EPS and dot(a, b) < EPS:
            return 1
        if a.y > b.y:
            a, b = b, a
        if a.y < EPS and EPS < b.y and cross(a, b) > EPS:
            x = not x
    return 2 if x else 0

def andrewScan(s):
    u = deque()     # Polygonクラスはキューで代用可能
    l = deque()
    if len(s) < 3:
        if ccw(s[0], s[1], s[2]) != CLOCKWISE:
            s.reverse()
        return s
    s.sort()    # Pointクラスで<演算子が使えるようにしてあるので、sortができる
    u.append(s[0])
    u.append(s[1])
    l.append(s[-1])
    l.append(s[-2])

    for i in range(2, len(s)):
        for n in range(len(u), 1, -1):
            if ccw(u[n-2], u[n-1], s[i]) != CLOCKWISE:
                break
            u.pop()
        u.append(s[i])
    
    for i in range(len(s)-3, -1, -1):
        for n in range(len(l), 1, -1):
            if ccw(l[n-2], l[n-1], s[i]) != CLOCKWISE:
                break
            l.pop()
        l.append(s[i])
    
    l.reverse()
    u = list(u)
    for i in range(len(u)-2, 0, -1):
        l.append(u[i])
    return l



if __name__ == '__main__':
    from sys import stdin
    input = stdin.readline

    n = int(input())
    points = [0]*n
    for i in range(n):
        points[i] = Point(*map(int, input().split()))

    l = andrewScan(points)
    l.reverse()    # 反時計回りにする
    l = list(l)    # deqeuのままだと処理が面倒なのでリストに
    min_index = l.index(min(l, key=lambda p: (p.y, p.x)))
    print(len(l))
    for i in l[min_index:]:
        print(i.x, i.y)
    for i in l[:min_index]:
        print(i.x, i.y)
    
