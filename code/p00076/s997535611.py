# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0076
"""
import sys
from math import atan, atan2, degrees, pi, cos, sin


Memo = []
def init_memo(n):
    global Memo
    Memo.append((0, 0))
    Memo.append((1, 0))
    for i in range(n):
        x = Memo[-1][0]
        y = Memo[-1][1]
        rad = atan2(-y, -x)
        rad -= pi / 2
        x += cos(rad)
        y += sin(rad)
        Memo.append((x, y))


def solve(n):
    global Memo
    return Memo[n]


def main(args):
    init_memo(1000)
    while True:
        n = int(input())
        if n == -1:
            break
        result = solve(n)
        print('{:.2f}'.format(result[0]))
        print('{:.2f}'.format(result[1]))

if __name__ == '__main__':
    main(sys.argv[1:])