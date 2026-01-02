# coding: utf-8
# Your code here!

# coding: utf-8
# Your code here!
import math

EPS = 0.0000000001

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0

IN = 2
ON = 1
OUT = 0

class Point:
    
    global EPS
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
        
    def __add__(a, b):
        s = a.x + b.x
        t = a.y + b.y
        return Point(s, t)
        
    def __sub__(a, b):
        s = a.x - b.x
        t = a.y - b.y
        return Point(s, t)
            
    def __mul__(self, a):
        s = a * self.x
        t = a * self.y
        return Point(s, t)
        
    def __truediv__(self, a):
        s = self.x / a
        t = self.y / a
        return Point(s, t)
            
            
            
            
    def norm(self):
        return self.x * self.x + self.y * self.y
        
    def abs(self):
        return self.norm() ** 0.5
            
    
            
            
    def __eq__(self, other):
        return abs(self.x - other.y) < self.EPS and abs(self.y - other.y) < self.EPS
            
            
            
    def dot(self, b):
        return self.x * b.x + self.y * b.y
        
    def cross(self, b):
        return self.x * b.y - self.y * b.x
    
    
class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Circle:
    def __init__(self, c, r):
        self.c = c
        self.r = r

def project(s, p):
    base = s.p2 - s.p1
    hypo = p - s.p1
    r = hypo.dot(base) / base.norm()
    return s.p1 + base * r

def reflecton(s, p):
    return p + (project(s,p) - p) * 2


def getDistance(a, b):
    return (a-b).abs()

def getDistanceLP(l, p):
    return abs((l.p2-l.p1).cross(p-l.p1)) / ((l.p2-l.p1).abs())

def getDistanceSP(s, p):
    if (s.p2 - s.p1).dot(p-s.p1) < 0:
        return (p-s.p1).abs()
    elif (s.p1 - s.p2).dot(p-s.p2) < 0:
        return (p-s.p2).abs()
    return getDistanceLP(s,p)


def getDistanceSS(s1, s2):
    if intersectS(s1, s2):
        return 0
    return min(getDistanceSP(s1, s2.p1), getDistanceSP(s1, s2.p2), getDistanceSP(s2, s1.p1), getDistanceSP(s2, s1.p2))



def ccw(p0, p1, p2):
    a = p1-p0
    b = p2-p0
    
    if a.cross(b) > 0:
        return COUNTER_CLOCKWISE
    elif a.cross(b) <0:
        return CLOCKWISE
    elif a.dot(b) < 0:
        return ONLINE_BACK
    elif a.abs() < b.abs():
        return ONLINE_FRONT
    else:
        return ON_SEGMENT

def intersect(p1, p2, p3, p4):
    return ccw(p1, p2, p3) *ccw(p1, p2, p4) <=0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0

def intersectS(s1, s2):
    return intersect(s1.p1, s1.p2, s2.p1, s2.p2)


def getCrossPoint(s1, s2):
    base = s2.p2-s2.p1
    a = s1.p1-s2.p1
    b = s1.p2-s2.p1
    
    d1 = abs(a.cross(base))
    d2 = abs(b.cross(base))
    
    t = d1 / (d1+d2)
    return s1.p1 + (s1.p2-s1.p1) * t


def getCrossPointC(c, l):
    pr = project(l, c.c)
    e = (l.p2-l.p1) / (l.p2-l.p1).abs()
    base = (c.r *c.r  - (pr - c.c).norm()) ** 0.5
    return pr - e * base, pr + e * base

def printPoint(p1, p2):
    print(round(p1.x, 8), round(p1.y, 8), round(p2.x, 8), round(p2.y, 8))


def arg(p):
    return math.atan2(p.y ,p.x)

def polar(a, r):
    return Point(a * math.cos(r), a * math.sin(r))

def getCrossPointCC(c1, c2):
    d = (c2.c - c1.c).abs()
    a = math.acos((c1.r * c1.r + d*d - c2.r*c2.r) / (2*c1.r*d))
    b = arg(c2.c-c1.c)
    return c1.c + polar(c1.r, b+a), c1.c + polar(c1.r, b-a)


def contains(g, p):
    n = len(g)
    flg = False
    for i in range(n):
        a = g[i] - p
        b = g[(i+1)%n] - p
        if abs(a.cross(b)) < EPS and a.dot(b) < EPS:
            return ON
        if a.y > b.y:
            a,b = b,a
        if a.y < EPS and EPS < b.y and a.cross(b) > EPS:
            flg = not flg
        
    if flg:
        return IN
    else:
        return OUT




n = int(input())
g = []
for i in range(n):
    nums=list(map(int,input().split()))
    g.append(Point(nums[0], nums[1]))

q = int(input())
for i in range(q):
    nums=list(map(int,input().split()))
    p = Point(nums[0], nums[1])
    result = contains(g, p)
    print(result)








