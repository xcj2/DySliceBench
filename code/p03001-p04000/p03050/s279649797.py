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


def eratosthenes(n):
    p = []
    t = [True] * n

    t[1] = True
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if t[i]:
            p.append(i)
            for j in range(2*i, n, i):
                t[j] = False

    for j in range(i+1, n):
        if t[j]:
            p.append(j)

    return p


def divisor(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


@mt
def slv(N):
    ans = 0
    for i in divisor(N):
        m = i-1
        if m == 0:
            continue
        if N//m == N % m:
            ans += m
    return ans


def slv2(N):
    ans = 0
    for m in range(1, N+1):

        if N//m == N % m:
            # print(m)
            print(m, N//m, N % m)
            ans += m
    return ans


def main():
    N = read_int()
    # print(slv2(N))
    print(slv(N))


if __name__ == '__main__':
    main()
