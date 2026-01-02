from math import sin, cos, pi


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x:.8f} {self.y:.8f}"


def kock(n, p1: Point, p2: Point):
    if n == 0:
        return
    s = Point(
        x=(2*p1.x + p2.x)/3,
        y=(2*p1.y + p2.y)/3
    )
    t = Point(
        x=(p1.x + 2*p2.x)/3,
        y=(p1.y + 2*p2.y)/3
    )
    u = Point(
        x=(t.x - s.x) * cos(pi / 3) - (t.y - s.y) * sin(pi / 3) + s.x,
        y=(t.x - s.x) * sin(pi / 3) + (t.y - s.y) * cos(pi / 3) + s.y
    )
    kock(n - 1, p1, s)
    print(s)
    kock(n - 1, s, u)
    print(u)
    kock(n - 1, u, t)
    print(t)
    kock(n - 1, t, p2)


def main():
    n = int(input())
    p1 = Point(0.0, 0.0)
    p2 = Point(100.0, 0.0)
    print(p1)
    kock(n, p1, p2)
    print(p2)

main()
