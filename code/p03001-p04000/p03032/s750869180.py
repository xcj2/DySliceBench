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
def slv(N, K, V):
    ans = 0
    for k in range(min(K, N)+1):
        for i in range(k+1):
            l = V[:i]
            r = V[N-(k-i):]
            # print(l, r)
            lr = l + r
            lr.sort(reverse=True)

            for _ in range(K-k):
                if lr and lr[-1] < 0:
                    lr.pop()
                else:
                    break
            ans = max(ans, sum(lr))

    return ans


def main():
    N, K = read_int_n()
    V = read_int_n()
    print(slv(N, K, V))


if __name__ == '__main__':
    main()
