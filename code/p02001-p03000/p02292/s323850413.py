import math


class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector2(self.x+v.x, self.y+v.y)

    def __sub__(self, v):
        return Vector2(self.x-v.x, self.y-v.y)

    def __mul__(self, v):
        return Vector2(self.x*v, self.y*v)

    def __truediv__(self, v):
        return Vector2(self.x/v, self.y/v)

    def __abs__(self):
        return math.sqrt(float(self.x*self.x+self.y*self.y))

    def dot(self, v):
        return self.x*v.x+self.y*v.y

    def cross(self, v):
        return self.x*v.y-self.y*v.x

    def norm(self):
        d = abs(self)
        return Vector2(self.x/d, self.y/d)


def distanceLP(v1, v2, p):
    '''
    v1 -> v2の直線とpとの距離
    '''
    return abs((v2-v1).cross(p-v1))/abs(v2-v1)


def distanceSP(v1, v2, p):
    '''
    v1 -> v2の線分とpとの距離
    '''
    if (v2-v1).dot(p-v1) < 0.0:
        return abs(p-v1)
    if (v1-v2).dot(p-v2) < 0.0:
        return abs(p-v2)
    return distanceLP(v1, v2, p)


def intersect(p1, p2, p3, p4):
    '''
    p1p2とp3p4の交差判定
    '''
    t1 = (p1.x-p2.x)*(p3.y-p1.y)+(p1.y-p2.y)*(p1.x-p3.x)
    t2 = (p1.x-p2.x)*(p4.y-p1.y)+(p1.y-p2.y)*(p1.x-p4.x)
    t3 = (p3.x-p4.x)*(p1.y-p3.y)+(p3.y-p4.y)*(p3.x-p1.x)
    t4 = (p3.x-p4.x)*(p2.y-p3.y)+(p3.y-p4.y)*(p3.x-p2.x)
    return (t1*t2) < 0.0 and (t3*t4) < 0.0


def distance(a1, a2, b1, b2):
    '''
    線分a1a2とb1b2の距離
    '''
    if intersect(a1, a2, b1, b2):
        return 0.0
    return min([
        min([distanceSP(a1, a2, b1), distanceSP(a1, a2, b2)]),
        min([distanceSP(b1, b2, a1), distanceSP(b1, b2, a2)])
    ])


p0x, p0y, p1x, p1y = map(int, input().split())
p0 = Vector2(p0x, p0y)
p1 = Vector2(p1x, p1y)
q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    p2 = Vector2(x, y)
    c = (p1-p0).cross(p2-p0)
    if math.isclose(c, 0.0):
        d = (p1-p0).dot(p2-p0)
        if d < 0.0:
            print("ONLINE_BACK")
        else:
            d1 = abs(p1-p0)
            d2 = abs(p2-p0)
            if d1 < d2:
                print("ONLINE_FRONT")
            else:
                print("ON_SEGMENT")
    elif c < 0.0:
        print("CLOCKWISE")
    else:
        print("COUNTER_CLOCKWISE")

