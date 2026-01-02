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


def eratosthenes(n):
    p = []
    t = [0] * n

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if t[i] == 0:
            p.append(i)
            t[i] = i
            for j in range(2*i, n, i):
                if t[j] == 0:
                    t[j] = i

    for j in range(i+1, n):
        if t[j] == j or t[j] == 0:
            p.append(j)
            t[j] = j

    return p, t


@mt
def slv(N, A):
    _, T = eratosthenes(10**6+1)

    used = set()
    for a in A:
        while a != 1:
            p = T[a]
            if p in used:
                break
            while a % p == 0:
                a //= p
            used.add(p)
        if a != 1:
            break

    else:
        return 'pairwise coprime'

    return 'setwise coprime' if reduce(math.gcd, A) == 1 else 'not coprime'


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))


if __name__ == '__main__':
    main()
