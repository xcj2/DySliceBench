class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Segment():
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.slope = None
        if self.p1.x == self.p2.x:
            self.slope = float('inf')
        else:
            self.slope = (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)

    def is_intersect(self, seg):
        a = (seg.p1.x - seg.p2.x) * (self.p1.y - seg.p1.y) + (seg.p1.y - seg.p2.y) * (seg.p1.x - self.p1.x)
        b = (seg.p1.x - seg.p2.x) * (self.p2.y - seg.p1.y) + (seg.p1.y - seg.p2.y) * (seg.p1.x - self.p2.x)
        c = (self.p1.x - self.p2.x) * (seg.p1.y - self.p1.y) + (self.p1.y - self.p2.y) * (self.p1.x - seg.p1.x)
        d = (self.p1.x - self.p2.x) * (seg.p2.y - self.p1.y) + (self.p1.y - self.p2.y) * (self.p1.x - seg.p2.x)
        e = (self.p1.x - seg.p1.x)*(self.p2.x - seg.p2.x)
        f = (self.p1.x - seg.p2.x)*(self.p2.x - seg.p1.x)
        g = (self.p1.y - seg.p1.y)*(self.p2.y - seg.p2.y)
        h = (self.p1.y - seg.p2.y)*(self.p2.y - seg.p1.y)
        return a*b <= 0 and c*d <= 0 and (e <= 0 or f <= 0) and (g <= 0 or h <= 0)

q = int(input())
for i in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = list(map(int, input().split(' ')))
    line1, line2 = Segment(x0, y0, x1, y1), Segment(x2, y2, x3, y3)
    if line1.is_intersect(line2):
        print(1)
    else:
        print(0)


