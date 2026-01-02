import math


def matrix_mul(mx1, mx2):
    n = len(mx1)
    m = len(mx1[0])
    _m = len(mx2)
    l = len(mx2[0])
    if m != _m:
        print("[!] Invalid Matrix Size.")
        return - 1

    ans = [[None] * l for _ in range(n)]

    for i in range(n):
        for j in range(l):
            _e = 0
            for k in range(m):
                _e += mx1[i][k] * mx2[k][j]
            ans[i][j] = _e

    return ans


def roll(p1, p2, r: int):
    """r must be radian"""
    _tmp = [[p2[0] - p1[0]], [p2[1] - p1[1]]]
    rad = math.pi*r/180
    matrix = [[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]]
    _tmp = matrix_mul(matrix, _tmp)
    return [p1[0]+_tmp[0][0], p1[1]+_tmp[1][0]]


def print_point(p):
    print("%.8f %.8f" % (p[0], p[1]))


def koch_curve(p1, p2, d: int):
    """p1: start point, p2: end point, d: depth of recursive"""
    if d == 0:
        print_point(p2)
    else:
        s = [p1[0] + (p2[0] - p1[0])/3, p1[1] + (p2[1] - p1[1])/3]
        t = [p1[0] + (p2[0] - p1[0])*2/3, p1[1] + (p2[1] - p1[1])*2/3]
        u = roll(s, t, 60)
        koch_curve(p1, s, d - 1)
        koch_curve(s, u, d - 1)
        koch_curve(u, t, d - 1)
        koch_curve(t, p2, d - 1)


n = int(input())
p1, p2 = [0.0, 0.0], [100.0, 0.0]
print_point(p1)
koch_curve(p1, p2, n)

