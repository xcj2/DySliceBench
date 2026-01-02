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
def slv(N, C, STC):
    tbl = [0] * (2*int(1e+5) + 2)
    ST = defaultdict(list)
    for s, t, c in STC:
        ST[c].append((s, t))
    for st in ST.values():
        st.sort()
        for i, (s, t) in enumerate(st):
            if i > 0 and st[i-1][1] == st[i][0]:
                tbl[2*(st[i][0])] += 1
                tbl[2*(st[i][1])] -= 1
            else:
                tbl[2*st[i][0]-1] += 1
                tbl[2*st[i][1]] -= 1

    for i in range(1, len(tbl)):
        tbl[i] += tbl[i-1]
    ans = max(tbl)
    return ans


def main():
    N, C = read_int_n()
    STC = [read_int_n() for _ in range(N)]
    print(slv(N, C, STC))


if __name__ == '__main__':
    main()
