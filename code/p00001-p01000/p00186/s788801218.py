# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0186

"""
import sys
from sys import stdin
input = stdin.readline


def Cond(q1, b, mid, c1, c2):
    b -= (c1 * mid)
    if b < 0:
        return False
    b -= (c2 * (q1 - mid))
    if b < 0:
        return False
    return True


def solve(q1, b, c1, c2, q2):
    ub = q2
    lb = 1
    aizu_chicken = 0

    while (ub - lb) > 1:
        mid = (ub + lb) // 2
        if Cond(q1, b, mid, c1, c2):
            lb = mid
            aizu_chicken = max(aizu_chicken, mid)
        else:
            ub = mid

    if Cond(q1, b, lb, c1, c2):
        aizu_chicken = max(aizu_chicken, lb)
    if Cond(q1, b, ub, c1, c2):
        aizu_chicken = max(aizu_chicken, ub)

    b -= (aizu_chicken * c1)
    normal_chicken = b // c2
    if normal_chicken < 0 or aizu_chicken == 0:
        return False, 0, 0
    else:
        return True, aizu_chicken, normal_chicken


def main(args):
    while True:
        txt = input().strip()
        if txt[0] == '0':
            break

        q1, b, c1, c2, q2 = map(int, txt.split())
        result, aizu, normal = solve(q1, b, c1, c2, q2)
        if result is False:
            print('NA')
        else:
            print(aizu, normal)


if __name__ == '__main__':
    main(sys.argv[1:])
    