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
def slv(N, S):
    idx = defaultdict(list)
    for i, s in enumerate(S):
        idx[int(s)].append(i)

    ans = 0
    for i in range(0, 10):
        if not idx[i]:
            continue
        l = idx[i][0]
        for j in range(0, 10):
            if not idx[j]:
                continue
            ll = bisect.bisect_right(idx[j], l)
            if ll == len(idx[j]):
                continue
            ll = idx[j][ll]
            for k in range(0, 10):
                if not idx[k]:
                    continue
                lll = bisect.bisect_right(idx[k], ll)
                if lll != len(idx[k]):
                    ans += 1

    return ans


def main():
    N = read_int()
    S = read_str()
    print(slv(N, S))

    # N = 300000
    # S = '0123456789' * (N //10)
    # print(slv(N, S))


if __name__ == '__main__':
    main()
