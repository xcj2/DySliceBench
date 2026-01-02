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
def slv(N, M, KS, P):

    ans = 0
    for s in product((0, 1), repeat=N):
        for j, ks in enumerate(KS):
            k = ks[0]
            c = 0
            for i in range(1, k+1):
                c += s[ks[i]-1]
            if c % 2 != P[j]:
                break
        else:
            ans += 1
    return ans


def main():
    N, M = read_int_n()
    KS = [read_int_n() for _ in range(M)]
    P = read_int_n()
    print(slv(N, M, KS, P))


if __name__ == '__main__':
    main()
