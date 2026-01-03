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
def slv(N, S):
    def f(cnd):
        for i in range(1, N):
            if S[i] == 'o' and cnd[i] == 'S':
                cnd.append(cnd[i-1])
            elif S[i] == 'o' and cnd[i] == 'W':
                cnd.append('S' if cnd[i-1] == 'W' else 'W')
            elif S[i] == 'x' and cnd[i] == 'S':
                cnd.append('S' if cnd[i-1] == 'W' else 'W')
            elif S[i] == 'x' and cnd[i] == 'W':
                cnd.append(cnd[i-1])

        cnd.pop()
        for i in range(N):
            if cnd[i] == 'S' and S[i] == 'o':
                if cnd[(i+1) % N] != cnd[i-1]:
                    return None
            elif cnd[i] == 'S' and S[i] == 'x':
                if cnd[(i+1) % N] == cnd[i-1]:
                    return None
            elif cnd[i] == 'W' and S[i] == 'o':
                if cnd[(i+1) % N] == cnd[i-1]:
                    return None
            elif cnd[i] == 'W' and S[i] == 'x':
                if cnd[(i+1) % N] != cnd[i-1]:
                    return None
        return ''.join(cnd)
    # SS
    ans = f(['S', 'S'])
    if ans:
        return ans

    # SW
    ans = f(['S', 'W'])
    if ans:
        return ans

    # WS
    ans = f(['W', 'S'])
    if ans:
        return ans

    # WW
    ans = f(['W', 'W'])
    if ans:
        return ans

    return -1


def main():
    N = read_int()
    S = read_str()
    print(slv(N, S))


if __name__ == '__main__':
    main()
