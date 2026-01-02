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
def slv(N, A, B, C, L):
    ans = sys.maxsize
    
    S = (A, B, C)
    for l in product([0, 1, 2, None], repeat=len(L)):
        ta = 0
        s = [A, B, C]
        for i, f in enumerate(l):
            if f is None:
                continue
            if s[f] != S[f]:
                ta += 10
            s[f] -= L[i]

        if any(map(lambda x: x[0] == x[1], zip(s, S))):
            continue
        
        ta += sum(map(abs, s))
        ans = min(ans, ta)

    return ans


def main():
    # N = read_int()
    N, A, B, C = read_int_n()
    L = [read_int() for _ in range(N)]
    print(slv(N, A, B, C, L))


if __name__ == '__main__':
    main()
