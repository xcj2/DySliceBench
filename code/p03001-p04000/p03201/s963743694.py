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
def slv(N, A):
    bp = list(reversed([2**i for i in range(2, 32)]))
    C = Counter(A)
    ans = 0
    A.sort(reverse=True)
    for k in A:
        if C[k] <= 0:
            continue
        C[k] -= 1
        r = (1 << k.bit_length()) - k
        if C[r] > 0:
            ans += 1
            C[r] -= 1

    return ans


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))

    # N = 2*(10**5)
    # # A = [random.randint(1, 10**9) for _ in range(N)]
    # A = list(range(1, N+1))
    # print(slv(N, A))


if __name__ == '__main__':
    main()
