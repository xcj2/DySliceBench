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
def slv(N, M, XYZ):
    g = defaultdict(dict)
    for x, y, z in XYZ:
        g[x][y] = z % 2
        g[y][x] = z % 2

    ans = 0
    done = set()
    for i in range(1, N+1):
        if i in done:
            continue
        ans += 1
        q = deque([i])
        while q:
            u = q.popleft()
            done.add(u)
            for v in g[u]:
                if v not in done:
                    q.append(v)
                    done.add(v)
    return ans


def main():
    # N = read_int()
    N, M = read_int_n()
    XYZ = [read_int_n() for _ in range(M)]
    print(slv(N, M, XYZ))

    # N = 10**5
    # XYZ = [random.randint()]


if __name__ == '__main__':
    main()
