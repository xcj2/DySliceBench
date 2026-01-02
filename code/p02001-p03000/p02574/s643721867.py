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

    return p


# error_print(len(P))

@mt
def slv(N, A):
    P = eratosthenes(10**6+1)
    P = set(P)
    # random.shuffle(A)

    for a in A:
        u = set()
        if a in P:
            P.remove(a)
            a = 1

        for p in P:
            if a % p == 0:
                u.add(p)
            while a % p == 0:
                a //= p
            if a == 1:
                break

        if a != 1:
            break
        P -= u
    else:
        return 'pairwise coprime'

    g = 0
    for a in A:
        g = math.gcd(a, g)
    return 'setwise coprime' if g == 1 else 'not coprime'


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))

    # P = eratosthenes(10**6+1)
    # N = len(P)
    # A = P[::-1]

    # error_print(N)
    # print(slv(N, A))


if __name__ == '__main__':
    main()
