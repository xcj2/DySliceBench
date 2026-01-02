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
def slv(N, M, A, B, C):
    d = defaultdict(lambda : sys.maxsize)
    # @lru_cache(maxsize=None)
    def f(t, v):
        if v >= d[t]:
            return sys.maxsize
        else:
            d[t] = v
        n = None
        for i in range(N):
            if  (1 << i) & t == 0:
                n = i + 1
                break
        else:
            return v

        ret = sys.maxsize
        for i, c in enumerate(C):
            if n in c:
                t_  = t
                for j in c:
                    t_ |= 1 << (j-1)
                ret = min(ret, f(t_, v + A[i]))
        return ret
    ans = f(0, 0)
    return  ans if ans != sys.maxsize else -1


def main():
    N, M = read_int_n()
    A = []
    B = []
    C = []
    for _ in range(M):
        a, b = read_int_n()
        A.append(a)
        B.append(b)
        C.append(set(read_int_n()))

    print(slv(N, M, A, B, C))

    # N = 12
    # M = 10**3
    # A = [random.randint(1, 10**5) for _ in range(M)]
    # B = [random.randint(1, N) for _ in range(M)]
    # C = [set([random.randint(1, N)]) for _ in range(M)]
    # print(slv(N, M, A, B, C))


if __name__ == '__main__':
    main()
