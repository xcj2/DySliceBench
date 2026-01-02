#!/usr/bin/python3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def run(N, A, loc, i):
    for c, d in A:
        if i in loc[c]:
            if d == 'L':
                i -= 1
                if i < 0:
                    return -1
            else:
                i += 1
                if i >= N:
                    return N
    return i


def solve(N, Q, S, A):
    loc = {a: set() for a in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for i, c in enumerate(S):
        loc[c].add(i)

    p0 = run(N, A, loc, 0)
    plast = run(N, A, loc, N - 1)

    if plast == -1:
        return 0
    if p0 == N:
        return 0

    lcnt = 0
    if p0 == -1:
        lb = 0
        ub = N - 1
        while ub - lb > 1:
            mid = (lb + ub) // 2
            p = run(N, A, loc, mid)
            dprint(lb, ub, mid, '=>', p)
            if p == -1:
                lb = mid
            else:
                ub = mid
        dprint(lb, ub)
        lcnt = ub

    rcnt = 0
    if plast == N:
        lb = 0
        ub = N - 1
        while ub - lb > 1:
            mid = (lb + ub) // 2
            p = run(N, A, loc, mid)
            dprint(lb, ub, mid, '=>', p)
            if p == N:
                ub = mid
            else:
                lb = mid
        dprint(lb, ub)
        rcnt = N - ub

    return N - lcnt - rcnt


def main():
    N, Q = [int(e) for e in inp().split()]
    S = inp()
    A = [inp().split() for _ in range(Q)]
    print(solve(N, Q, S, A))


if __name__ == '__main__':
    main()
