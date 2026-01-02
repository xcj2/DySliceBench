def print8f(xy):
    from decimal import Decimal, ROUND_HALF_UP
    acc = Decimal("0.00000001")
    x, y = xy
    x = Decimal(str(x)).quantize(acc, rounding=ROUND_HALF_UP)
    y = Decimal(str(y)).quantize(acc, rounding=ROUND_HALF_UP)
    print("{:.8f} {:.8f}".format(x, y))


def kochCurve(p1p2, n, ang):
    from math import sin, cos, radians, sqrt
    if n == 0:
        print8f(p1p2[1])
        return
    p1, p2 = p1p2
    xd3 = (p2[0] - p1[0]) / 3
    yd3 = (p2[1] - p1[1]) / 3
    s = [p1[0] + xd3, p1[1] + yd3]
    t = [p2[0] - xd3, p2[1] - yd3]
    st = sqrt((s[0] - t[0])**2 + (s[1] - t[1])**2)
    u = [s[0] + cos(radians(ang + 60)) * st,
         s[1] + sin(radians(ang + 60)) * st]

    kochCurve([p1, s], n - 1, ang)
    kochCurve([s, u], n - 1, ang + 60)
    kochCurve([u, t], n - 1, ang - 60)
    kochCurve([t, p2], n - 1, ang)


def resolve():
    n = int(input())
    p1p2 = [[0, 0], [100, 0]]
    print8f(p1p2[0])
    kochCurve(p1p2, n, 0)


resolve()

