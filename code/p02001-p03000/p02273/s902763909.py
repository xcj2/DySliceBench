from math import cos, sin, pi


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x:.8f} {self.y:.8f}")


def calc_s(p1, p2) -> Point:
    x = p1.x * 2 / 3 + p2.x / 3
    y = p1.y * 2 / 3 + p2.y / 3
    s = Point(x, y)
    return s


def calc_t(p1, p2) -> Point:
    x = p1.x / 3 + p2.x * 2 / 3
    y = p1.y / 3 + p2.y * 2 / 3
    t = Point(x, y)
    return t


def calc_u(s, t) -> Point:
    theta = pi / 3
    x = s.x + (t.x - s.x) * cos(theta) - (t.y - s.y) * sin(theta)
    y = s.y + (t.x - s.x) * sin(theta) + (t.y - s.y) * cos(theta)
    u = Point(x, y)
    return u


def koch(n, p1, p2):
    if n == 0:
        return

    s = calc_s(p1, p2)
    t = calc_t(p1, p2)
    u = calc_u(s, t)

    koch(n - 1, p1, s)
    s.show()

    koch(n - 1, s, u)
    u.show()

    koch(n - 1, u, t)
    t.show()

    koch(n - 1, t, p2)


def main():
    n = int(input())
    p1 = Point(0, 0)
    p2 = Point(100, 0)

    p1.show()
    koch(n, p1, p2)
    p2.show()


if __name__ == "__main__":
    main()

