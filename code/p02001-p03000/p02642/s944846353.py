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
    t = [True] * n

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if t[i]:
            p.append(i)
            for j in range(2*i, n, i):
                t[j] = False

    for j in range(i+1, n):
        if t[j]:
            p.append(j)

    return p, t

P, T = eratosthenes(int(math.sqrt(10**6))+1)

def e(n):
    c = []
    for p in P:
        while n % p == 0:
            # c[p] += 1
            c.append(p)
            n //= p
        if n == 1:
            break
    if n != 1:
        # c[n] += 1
        c.append(n)
    return c


@mt
def slv(N, A):
    ans = 0
    A.sort()
    ac = Counter(A)
    for i in range(N):
        # print(i)
        a = A[i]
        if ac[a] >= 2:
            continue
        c = e(a)
        for j in range(len(c)):
            f = False
            for i in combinations(c, r=j):
                m = reduce(mul, i, 1)
                # error_print(a, m)
                if ac[m] >= 1:
                    # error_print('b', a)
                    break
            else:
                f = True
            if not f:
                break
        else:
            ans += 1

    return ans


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))

    # from random import randint
    # N = 2* (10**5)
    # A = [randint(1, 10**6) for _ in range(N)]
    # print(slv(N, A))


if __name__ == '__main__':
    main()
