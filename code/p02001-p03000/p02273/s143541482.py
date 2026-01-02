import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x:.8f} {self.y:.8f}"


def koch(d, l, r):
    if d == 0:
        return

    s = Point()
    t = Point()
    u = Point()
    s.x = (2*l.x + 1*r.x) / (1 + 2)
    s.y = (2*l.y + 1*r.y) / (1 + 2)
    t.x = (1*l.x + 2*r.x) / (2 + 1)
    t.y = (1*l.y + 2*r.y) / (2 + 1)
    u.x = (t.x - s.x) * math.cos(math.radians(60)) - (t.y - s.y) * math.sin(math.radians(60)) + s.x
    u.y = (t.x - s.x) * math.sin(math.radians(60)) + (t.y - s.y) * math.cos(math.radians(60)) + s.y

    koch(d - 1, l, s)
    print(s)
    koch(d - 1, s, u)
    print(u)
    koch(d - 1, u, t)
    print(t)
    koch(d - 1, t, r)

n = int(input())
l, r = Point(), Point(100.0, 0.0)
print(l)
koch(n, l, r)
print(r)
