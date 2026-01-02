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
    ans = 0
    A = [list(reversed(a)) for a in A]

    s1 = set()
    s2 = set()
    for i in range(1, N+1):
        if A[i-1]:
            d = A[i-1][-1]
            n = (min(i, d), max(i, d))
            if n not in s1:
                s1.add(n)
            else:
                s2.add(n)
                s1.remove(n)
        
    while True:
        c = 0
        dell = []
        adding = []
        for k in s2:
            a, b = k
            A[a-1].pop()
            if A[a-1]:
                d = A[a-1][-1]
                n = (min(a, d), max(a, d))
                adding.append(n)
            A[b-1].pop()
            if A[b-1]:
                d = A[b-1][-1]
                n = (min(b, d), max(b, d))
                adding.append(n)
            dell.append(k)
            c += 1

        for k in dell:
            s2.remove(k)
        for k in adding:
            if k in s1:
                s2.add(k)
                s1.remove(k)
            else:
                s1.add(k)

        if c == 0:
            break
        else:
            ans += 1


    for a in A:
        if a:
            return -1
    return ans


def main():
    N = read_int()
    A = [read_int_n() for _ in range(N)]
    print(slv(N, A))

    # N = 1000
    # A = []

    # while True:
    #     for i in range(1, N+1):
    #         t = list(range(1, N+1))
    #         t.remove(i)
    #         random.shuffle(t)
    #         A.append(t)
    #     print(slv(N, A))


if __name__ == '__main__':
    main()
