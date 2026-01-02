# coding: utf-8
# Your code here!

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0

EPS = 0.0000000001

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



        
n = int(input())
for i in range(n):
    nums=list(map(int,input().split()))
    p1 = Point(nums[0], nums[1])
    p2 = Point(nums[2], nums[3])
    p3 = Point(nums[4], nums[5])
    p4 = Point(nums[6], nums[7])
    s1 = Segment(p1, p2)
    s2 = Segment(p3, p4)
    if intersectS(s1, s2):
        print(1)
    else:
        print(0)



