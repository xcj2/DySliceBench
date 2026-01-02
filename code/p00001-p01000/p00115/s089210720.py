# -*- coding: utf-8 -*-

import sys
import os
import math
import random

# refs
# https://shikousakugo.wordpress.com/2012/06/27/ray-intersection-2/

def det(a, b, c):
    return + a[0] * b[1] * c[2] \
           + a[2] * b[0] * c[1] \
           + a[1] * b[2] * c[0] \
           - a[2] * b[1] * c[0] \
           - a[1] * b[0] * c[2] \
           - a[0] * b[2] * c[1]

def sub(v0, v1):
    # v0 - v1
    return (v0[0] - v1[0], v0[1] - v1[1], v0[2] - v1[2])

# me
p0 = list(map(int, input().split()))

# enemy
p1 = list(map(int, input().split()))

# barrier
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

def solve(p0, p1, A, B, C):
    a = sub(p1, p0)
    b = sub(A, B)
    c = sub(A, C)
    d = sub(A, p0)

    EPS = 0.0000001
    lower = -EPS
    upper = 1 + EPS

    denom = det(a, b, c)

    if denom != 0:
        t = det(d, b, c) / denom
        u = det(a, d, c) / denom
        v = det(a, b, d) / denom

        if t < lower:
            return 'HIT'

        # hit barrier
        elif lower < t < upper and lower <= u <= upper and lower <= v <= upper and lower <= u + v <= upper:
            return 'MISS'

        else:
            return 'HIT'
    else:
        return 'HIT'

def correct_solve(p0, p1, A, B, C):
    from fractions import Fraction
    def gauss(a):
        if not a or len(a) == 0: return None
        n = len(a)
        for i in range(n):
            if a[i][i] == 0:
                for j in range(i + 1, n):
                    if a[j][i] != 0:
                        for k in range(i, n + 1): a[i][k] += a[j][k]
                        break
                else:
                    return None
            for j in range(n):
                if i != j:
                    r = Fraction(a[j][i], a[i][i])
                    for k in range(i, n + 1): a[j][k] = a[j][k] - a[i][k] * r
        for i in range(n):
            x = Fraction(a[i][i], 1)
            for j in range(len(a[i])):
                a[i][j] /= x
        return a


    uaz = p0
    enemy = [0] + [-x + y for x, y in zip(p1, uaz)]
    b0 = [1] + [x - y for x, y in zip(A, uaz)]
    b1 = [1] + [x - y for x, y in zip(B, uaz)]
    b2 = [1] + [x - y for x, y in zip(C, uaz)]
    sol = gauss(list(map(list, zip(b0, b1, b2, enemy, [1, 0, 0, 0]))))
    if sol and all(0 <= e[-1] <= 1 for e in sol):
        return 'MISS'
    else:
        return 'HIT'

def rand_v():
    return (random.randrange(-100, 100), random.randrange(-100, 100), random.randrange(-100, 100))

if __name__ == '__main__':
    res = solve(p0, p1, A, B, C)
    print(res)


    # while True:
    #     p0 = rand_v()
    #     p1 = rand_v()
    #     A = rand_v()
    #     B = rand_v()
    #     C = rand_v()
    #     result0 = solve(p0, p1, A, B, C)
    #     result1 = correct_solve(p0, p1, A, B, C)
    #
    #     if result0[0] != result1[0]:
    #         print(p0, p1, A, B, C)
    #         print(result0)
    #         print(result1)
    #     else:
    #         print('same')