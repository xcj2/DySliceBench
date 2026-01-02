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


def BellmanFord(g, s):
    V = list(g.keys())
    for v in g.values():
        V.extend(list(v.keys()))
    V = set(V)

    dist = defaultdict(lambda: sys.maxsize)
    pred = defaultdict(lambda: -1)

    dist[s] = 0

    N = len(V)
    for i in range(N+1):
        for u in g:
            for v in g[u]:
                if dist[v] > dist[u] + g[u][v]:
                    if i == N:
                        return 'inf'
                    dist[v] = dist[u] + g[u][v]
                    pred[v] = u
    return dist



@mt
def slv(H, W, S):
    g = defaultdict(dict)
    for i in range(H):
        for j in range(W):
            for x, y in ((0, 1), (1, 0)):
                if 0 <= i + x < H and 0 <= j+y < W:
                    if S[i][j] == '.' and S[i+x][j+y] == '#':
                        c = 1
                    else:
                        c = 0
                    g[(i, j)][(i+x, j+y)] = c
    g[0][(0, 0)] = 1 if S[0][0] == '#' else 0

    def bfs(s=0):
        q = deque()
        q.append(s)
        d = defaultdict(lambda: sys.maxsize)
        d[s] = 0
        while q:
            u = q.popleft()
            for v, c in g[u].items():
                if d[u] + c < d[v]:
                    d[v] = d[u] + c
                    if c == 0:
                        q.appendleft(v)
                    else:
                        q.append(v)

        return d

    return bfs()[(H-1, W-1)]


def main():
    H, W = read_int_n()
    S = [read_str() for _ in range(H)]
    print(slv(H, W, S))

    # H = 100
    # W = 100
    # S = [''.join(random.choices('.#', k=W)) for _ in range(H)]
    # print(slv(H, W, S))


if __name__ == '__main__':
    main()
