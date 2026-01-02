# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub


import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline
readline = input

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()

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

from fractions import Fraction

@mt
def slv(N, A):
    c = Counter()
    for a in A:
        a += '.0'
        t = a.split('.')
        b = int(t[0]) * 10**9 + int(t[1]) * 10**(9-len(t[1]))
        n5 = 0
        n2 = 0
        while b % 2 == 0:
            n2 += 1
            b //= 2
        while b % 5 == 0:
            n5 += 1
            b //= 5
        c[(n2, n5)] += 1

    ans = 0
    for k, kk in combinations_with_replacement(c.keys(), r=2):
        if k[0] + kk[0] >= 18 and k[1] + kk[1] >= 18:
            if k == kk:
                ans += c[k] * (c[k]-1) // 2
            else:
                ans += c[k] * c[kk]

    return ans



def main():
    N = read_int()
    A = [input() for _ in range(N)]
    print(slv(N, A))



if __name__ == '__main__':
    main()
