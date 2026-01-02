
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


def fs(n):
    f = Counter()
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if i > n:
            break
        while n % i == 0:
            f[i] += 1
            n /= i
    if int(n) != 1:
        f[int(n)] = 1
    return f

@mt
def slv(N, M):
    ans = 1
    for m in range(1, math.ceil(math.sqrt(M))+1):
        if M % m != 0:
            continue
        
        if  N*m <= M:
            ans = max(ans, m)
        if  N*(M//m) <= M:
            ans = max(ans, M//m)

    return ans


def main():
    N, M = read_int_n()
    print(slv(N, M))


if __name__ == '__main__':
    main()


