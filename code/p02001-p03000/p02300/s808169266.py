import math

EPS = 1e-10

def equals(a, b):
    return abs(a - b) < EPS


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, a):
        return Point(self.x * a, self.y * a)

    def __rmul__(self, a):
        return self * a

    def __truediv__(self, a):
        return Point(self.x / a, self.y / a)

    def norm(self):
        return self.x * self.x + self.y * self.y

    def abs(self):
        return math.sqrt(self.norm())

    def __lt__(self, p):
        if self.x != p.x:
            return self. x < p.x
        else:
            return self.y < p.y

    def __eq__(self, p):
        return equals(self.x, p.x) and equals(self.y, p.y)


def dot(a, b):
    return a.x * b.x + a.y * b.y


def cross(a, b):
    return a.x * b.y - a.y * b.x


COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = 2
ONLINE_FRONT = -2
ON_SEGMENT = 0


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


def andrewScan(s):
    n = len(s)
    if n < 3:
        return s
    u = []
    l = []
    s.sort()
    u.append(s[0])
    u.append(s[1])
    l.append(s[-1])
    l.append(s[-2])

    for i in range(2, n):
        for m in range(len(u), 1, -1):
            if ccw(u[m-2], u[m-1], s[i]) != COUNTER_CLOCKWISE:
                break
            u.pop()
        u.append(s[i])

    for i in range(n-3, -1, -1):
        for m in range(len(l), 1, -1):
            if ccw(l[m-2], l[m-1], s[i]) != COUNTER_CLOCKWISE:
                break
            l.pop()
        l.append(s[i])

    l.reverse()
    l.extend(u[-2:0:-1])
    return l


if __name__ == '__main__':
    n = int(input())
    g = []
    for i in range(n):
        x, y =  [int(v) for v in input().split()]
        g.append(Point(x, y))

    ans = andrewScan(g)

    minv = ans[0]
    mini = 0
    for i in range(1, len(ans)):
        if ans[i].y < minv.y or (ans[i].y == minv.y and ans[i].x < minv.x):
            minv = ans[i]
            mini = i
    ans = ans[mini:] + ans[:mini]

    print(len(ans))
    for v in ans:
        print('{0} {1}'.format(v.x, v.y))
