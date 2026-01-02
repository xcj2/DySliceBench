import math
import random
import heapq
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING
from functools import lru_cache, reduce
from itertools import combinations_with_replacement, product, combinations


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


def mt(f):
    import time
    import sys

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        print(e - s, 'sec', file=sys.stderr)
        return ret

    return wrap


def root(G, x):
    if G[x] != x:
        G[x] = root(G, G[x])
    return G[x]


def same(G, x, y):
    return root(G, x) == root(G, y)


def union(G, x, y):
    x = root(G, x)
    y = root(G, y)

    if x != y:
        G[x] = y


@mt
def slv(N, M, P, XY):
    P = [-1] + P
    G = [i for i in range(N + 1)]

    for x, y in XY:
        union(G, x, y)

    ans = 0
    for i, p in enumerate(P):
        if same(G, p, i):
            ans += 1

    return ans


def main():
    N, M = read_int_n()
    P = read_int_n()
    XY = []
    for _ in range(M):
        XY.append(read_int_n())

    print(slv(N, M, P, XY))


if __name__ == '__main__':
    main()