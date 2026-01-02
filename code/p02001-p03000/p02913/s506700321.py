#!/usr/bin/python3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


MOD = 10 ** 9 + 7
BASE = 29


def has_dup(V, sz):
    N = len(V)

    h = 0
    p = 1
    for i in range(sz):
        h *= BASE
        h += V[i]
        h %= MOD

        p *= BASE
        p %= MOD

    h2i = {h: [0]}
    for i in range(sz, N):
        j = i - sz + 1
        h *= BASE
        h += V[i]
        h += MOD - ((p * V[i - sz]) % MOD)
        h %= MOD
        if h not in h2i:
            h2i[h] = []
        h2i[h].append(j)

    for a in h2i.values():
        alen = len(a)
        for i in range(alen):
            ii = a[i]
            for j in range(i + 1, alen):
                ji = a[j]
                if ji - ii < sz:
                    continue
                if V[ii:ii + sz] == V[ji:ji + sz]:
                    return True

    return False


def solve(N, S):
    if N <= 26:
        has_ans = False
        for v in range(ord('a'), ord('z') + 1):
            ch = chr(v)
            if S.count(ch) >= 2:
                has_ans = True
                break
        if not has_ans:
            return 0

    V = [ord(c) - ord('a') for c in S]

    lb = 1
    ub = N // 2 + 1
    while ub - lb > 1:
        mid = (lb + ub) // 2
        if has_dup(V, mid):
            lb = mid
        else:
            ub = mid

    return lb


def main():
    N = int(inp())
    S = inp()
    print(solve(N, S))


if __name__ == '__main__':
    main()
