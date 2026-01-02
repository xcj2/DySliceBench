# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 2**62-1


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(H, W, S):
    def edges(v):
        i, j = v
        r = []
        if i > 0 and S[i-1][j] == '.':
            r.append((i-1, j))

        if i < H-1 and S[i+1][j] == '.':
            r.append((i+1, j))

        if j > 0 and S[i][j-1] == '.':
            r.append((i, j-1))

        if j < W-1 and S[i][j+1] == '.':
            r.append((i, j+1))

        return r

    def bfs(s):
        q = deque([s])
        d = {s: 0}
        while q:
            u = q.popleft()
            for v in edges(u):
                if v not in d:
                    d[v] = d[u] + 1
                    q.append(v)
        return max(d.values())

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                l = bfs((i, j))
                ans = max(ans, l)
    return ans


def main():
    H, W = read_int_n()
    S = [read_str() for _ in range(H)]
    print(slv(H, W, S))


if __name__ == '__main__':
    main()
