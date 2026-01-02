# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul

sys.setrecursionlimit(10000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


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
    # g = defaultdict(list)
    # for i, r in enumerate(S):
    #     for j, c in enumerate(r):
    #         if c == '.':
    #             if i > 0 and j > 0:
    #                 g[(i, j)].append((i-1, j-1))
    #     # g[u].append((v, (a, b)))
    #     # g[v].append((u, (a, b)))

    def d(s):
        dist = defaultdict(lambda : sys.maxsize)
        q =[]
        dist[s] = 0
        heapq.heappush(q, (dist[s], s))
        while q:
            c, u = heapq.heappop(q)
            if dist[u] > c:
                continue
            i, j = u
            g = []            
            if i > 0 and S[i-1][j] == '.':
                g.append((i-1, j))

            if j > 0 and S[i][j-1] == '.':
                g.append((i, j-1))

            if i < H-1 and S[i+1][j] == '.':
                g.append((i+1, j))

            if j < W-1 and S[i][j+1] == '.':
                g.append((i, j+1))
            
            for v in g:
                alt = dist[u] + 1
                if dist[v] > alt:
                    dist[v] = alt
                    heapq.heappush(q, (alt, v))
        return dist

    dist = d((0, 0))[(H-1, W-1)]
    if dist == sys.maxsize:
        return -1
    return (H * W - sum(map(lambda x: x.count('#'), reduce(add, S)))) - dist - 1


def main():
    H, W = read_int_n()
    S = [read_str() for _ in range(H)]

    
    print(slv(H, W, S))


if __name__ == '__main__':
    main()
