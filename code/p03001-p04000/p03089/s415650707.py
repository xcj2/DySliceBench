from sys import stdin, stdout
from decimal import Decimal
from random import randint
PEPS = 1e-10
INF = float('inf')


def sqr(a):
    return a * a


def dist(a, b = (0, 0)):
    return sqrt(sqr(a[0] - b[0]) + sqr(a[1] - b[1]))


def s_dist(a, b = (0, 0)):
    return (sqr(a[0] - b[0]) + sqr(a[1] - b[1]))


def dist3(a, b = (0, 0, 0)):
    return sqrt(sqr(a[0] - b[0]) + sqr(a[1] - b[1]) + sqr(a[2] - b[2]))


def s_dist3(a, b = (0, 0, 0)):
    return (sqr(a[0] - b[0]) + sqr(a[1] - b[1]) + sqr(a[2] - b[2]))


def trans(p, al):
    return (p[0] * cos(al) + p[1] * sin(al), - p[0] * sin(al) + p[1] * cos(al))


def get_angle(a, b, c):
    cos_al = (sqr(a) + sqr(b) - sqr(c)) / (2 * a * b)
    return acos(cos_al)


def write_float(ans):
    stdout.write(str('%.13f' % ans) + '\n')


def get_hight(pt1, pt2, pt3):
    a = (pt2[0] - pt1[0], pt2[1] - pt1[1])
    b = (pt3[0] - pt1[0], pt3[1] - pt1[1])
    return abs(a[0] * b[1] - a[1] * b[0]) / dist(pt1, pt2)


def get_square(pt1, pt2, pt3):
    a = (pt2[0] - pt1[0], pt2[1] - pt1[1])
    b = (pt3[0] - pt2[0], pt3[1] - pt2[1])
    return (a[0] * b[-1] - a[1] * b[0]) / 2


def sign(v):
    if v > 0:
        return 1
    elif v < 0:
        return -1
    else:
        return 0


def inn(pt, triangle):
    signs = set()
    signs.add(sign(get_square(triangle[0], triangle[1], pt)))
    signs.add(sign(get_square(triangle[1], triangle[2], pt)))
    signs.add(sign(get_square(triangle[2], triangle[0], pt)))
    return len(signs) == 1


def inter_in(a, b):
    return dist((a[0], a[1]), (b[0], b[1])) < a[-1] + b[-1]


def inter_in3(a, b):
    return dist3(a[:-1], b[:-1]) < a[-1] + b[-1]


def shift(what, wth):
    return (what[0] - wth[0], what[1] - wth[1])


n = int(stdin.readline())
vl = list(map(int, stdin.readline().split()))
ans = []

while len(vl):
    for i in range(len(vl) - 1, -1, -1):
        if vl[i] == i + 1:
            ans.append(i + 1)
            vl = vl[:i] + vl[i + 1:]
            break
    else:
        stdout.write('-1\n')
        break


if len(ans) == n:
    ans = ans[::-1]
    stdout.write('\n'.join(list(map(str, ans))))
