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

sys.setrecursionlimit(50000)


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
def slv(N, CN, D, C):
    # for d in D:
    #     error_print(d)
    # for c in C:
    #     error_print(c)

    T = [[], [], []]
    for i, r in enumerate(C):
        for j, c in enumerate(r):
            T[(i + j) % 3].append((i, j, c))
    TC = [[], [], []]
    for j, t in enumerate(T):
        for i in range(CN):
            s = 0
            for c in t:
                s += D[c[2] - 1][i - 1]
            TC[j].append(s)

    ans = sys.maxsize
    for i, j, k in permutations(range(CN), 3):
        ans = min(ans, sum([TC[0][i], TC[1][j], TC[2][k]]))

    return ans


def main():

    N, CN = read_int_n()
    D = [read_int_n() for _ in range(CN)]
    C = [read_int_n() for _ in range(N)]
    print(slv(N, CN, D, C))


if __name__ == '__main__':
    main()
