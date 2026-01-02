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
def slv(N, C):
    C_ = [-1]
    for c in C:
        if C_[-1] == c:
            continue
        C_.append(c)
    
    C = C_

    mod = 10**9 + 7
    S = defaultdict(lambda: 0)
    ans = 1
    for c in C:
        ans = (ans + S[c]) % mod
        S[c] = ans

    return ans


def main():
    N = read_int()
    C = [read_int() for _ in range(N)]
    print(slv(N, C))


if __name__ == '__main__':
    main()
