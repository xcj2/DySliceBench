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
def slv(N, Q, S, TD):
    def reachable(i):
        if i < 0:
            return -1
        elif i >= N:
            return 1
        for t, d in TD:
            if S[i] == t:
                if d == 'L':
                    i -= 1
                else:
                    i += 1
            if i == -1:
                return -1
            elif i == N:
                return 1
        return 0
    ans = N
    lo = 0
    hi = N
    while lo < hi:
        mid = (lo+hi)//2
        if reachable(mid) < 0: lo = mid+1
        else: hi = mid
    ans -= lo


    lo = 0
    hi = N
    while lo < hi:
        mid = (lo+hi)//2
        if 0 < reachable(mid): hi = mid
        else: lo = mid+1
    ans -= N - lo
    return ans



def main():
    N, Q = read_int_n()
    S = read_str()
    TD = [read_str_n() for _ in range(Q)]
    print(slv(N, Q, S, TD))



if __name__ == '__main__':
    main()
