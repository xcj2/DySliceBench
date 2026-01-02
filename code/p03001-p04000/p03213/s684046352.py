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
    p = [1]
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


@mt
def slv(N):
    ps = eratosthenes(100)
    ps.pop(0)
    c = Counter()
    for i in range(2, N+1):
        n = i
        while n not in ps:
            for p in ps:
                if n % p == 0:
                    c[p] += 1
                    n //= p
                    break
        c[n] += 1

    c2 = len(list(filter( lambda x: x>=2, c.values())))
    c4 = len(list(filter( lambda x: x>=4, c.values())))
    c14 = len(list(filter( lambda x: x>=14, c.values())))
    c24 = len(list(filter( lambda x: x>=24, c.values())))
    c74 = len(list(filter( lambda x: x>=74, c.values())))
    ans = 0
    if c2 >= 3 and c4 >= 2:
        ans += (c4*(c4-1)//2) * (c2-2)
    if c4 > 0 and c14 > 0:
        ans += (c4-1) * c14
    
    if c2 > 0 and c24 > 0:
        ans += (c2-1) * c24
    if c74 > 0:
        ans += c74
    return ans


def main():
    N = read_int()
    print(slv(N))


if __name__ == '__main__':
    main()
