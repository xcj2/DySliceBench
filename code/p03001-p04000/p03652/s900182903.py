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
def slv(N, M, A):
    ans = INF
    s = set(range(1, M+1))
    for _ in range(M):
        c = Counter()
        for a in A:
            for b in a:
                if b in s:
                    c[b] += 1
                    break
        k, v = c.most_common()[0]
        
        ans = min(ans, v)
        s.remove(k)
    return ans


def main():
    N, M = read_int_n()
    A = [read_int_n() for _ in range(N)]
    print(slv(N, M, A))


if __name__ == '__main__':
    main()
