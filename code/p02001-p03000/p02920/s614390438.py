#!/usr/bin/python3

import heapq
import math
import os
import sys


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, S):
    bt = [0] * (2 ** (N + 1) - 1)
    M = len(bt)
    pq = []
    heapq.heappush(pq, (0, 0))

    S.sort(reverse=True)

    i = 0
    while i < len(S):
        v = S[i]
        j = i
        while j < len(S) and v == S[j]:
            j += 1
        c = j - i
        i = j

        if len(pq) < c:
            return False

        pl = [heapq.heappop(pq) for _ in range(c)]
        for level, idx in pl:
            ll = level
            while True:
                assert bt[idx] == 0
                bt[idx] = v
                s = 2 * idx + 1
                t = s + 1
                if s >= M:
                    break
                idx = s
                ll += 1
                heapq.heappush(pq, (ll, t))

    return True


def main():
    N = int(inp())
    S = [int(e) for e in inp().split()]
    print('Yes' if solve(N, S) else 'No')


if __name__ == '__main__':
    main()
