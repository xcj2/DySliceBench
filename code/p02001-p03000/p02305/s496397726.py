import math
from enum import Enum, auto

class TwoCircle(Enum):
    DISTANT = auto()
    CIRCUMCSCRIBING = auto()
    INTERSECTING = auto()
    INSCRIBING = auto()
    CONTAINING = auto()

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pnt):
        return math.sqrt((self.x - pnt.x)**2 + (self.y - pnt.y)**2)

class Circle():
    def __init__(self, x, y, r):
        self.c = Point(x, y)
        self.r = r

    def is_intersected(self, cir):
        d = self.c.distance(cir.c)
        if d > self.r + cir.r:
            return TwoCircle.DISTANT
        elif d == self.r + cir.r:
            return TwoCircle.CIRCUMCSCRIBING
        elif d == abs(self.r - cir.r):
            return TwoCircle.INSCRIBING
        elif d < abs(self.r - cir.r):
            return TwoCircle.CONTAINING
        else:
            return TwoCircle.INTERSECTING

x1, y1, r1 = list(map(int, input().split(' ')))
x2, y2, r2 = list(map(int, input().split(' ')))
cir1 = Circle(x1, y1, r1)
cir2 = Circle(x2, y2, r2)

judged = cir1.is_intersected(cir2)
if judged == TwoCircle.DISTANT: print(4)
elif judged == TwoCircle.CIRCUMCSCRIBING: print(3)
elif judged == TwoCircle.INTERSECTING: print(2)
elif judged == TwoCircle.INSCRIBING: print(1)
elif judged == TwoCircle.CONTAINING: print(0)
