# -*- coding: utf-8 -*-
"""
D - Christmas
https://atcoder.jp/contests/abc115/tasks/abc115_d

"""
import sys


def create_burger(n):
    if n == 0:
        return 'P'
    return 'B' + create_burger(n-1) + 'P' + create_burger(n-1) + 'B'


def solve(N, X):
    def eat_p(level, x):
        if level == 0:
            return 0 if x <= 0 else 1
        elif x <= 1 + T[level-1]:
            return eat_p(level-1, x-1)
        else:
            return P[level-1] + 1 + eat_p(level-1, x-2-T[level-1])

    T, P = [1], [1]
    for _ in range(N):
        T.append(T[-1] * 2 + 3)
        P.append(P[-1] * 2 + 1)

    return eat_p(N, X)


def main(args):
    N, X = map(int, input().split())
    ans = solve(N, X)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
