import math


def eq(x, y):
    return abs(x - y) <= 10e-10


def get_r(_a, _b, _c):
    return math.acos((-_a ** 2 + _b ** 2 + _c ** 2) / (2 * _b * _c))


def _len(_ax, _ay, _bx, _by):
    return math.sqrt((_ax - _bx) ** 2 + (_ay - _by) ** 2)

try:
    while 1:

        xa,ya,xb,yb,xc,yc,xd,yd = map(float, input().split(','))

        ab = _len(xa,ya,xb,yb)
        bc = _len(xc,yc,xb,yb)
        cd = _len(xc,yc,xd,yd)
        ad = _len(xa,ya,xd,yd)

        bd = _len(xd,yd,xb,yb)
        ac = _len(xa,ya,xc,yc)

        A = get_r(bd, ab, ad)
        B = get_r(ac, ab, bc)
        C = get_r(bd, bc, cd)
        D = get_r(ac, ad, cd)

        if eq(A + B + C + D, 2 * math.pi):
            print("YES")
        else:
            print("NO")

except:
    pass