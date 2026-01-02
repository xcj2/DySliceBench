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
def slv(N, K, A):

    d = defaultdict(list)
    for i, a in enumerate(A):
        d[a].append(i)

    ni = []
    for i, a in enumerate(A):
         ni.append(d[a][bisect.bisect_right(d[a], i) % len(d[a])])

    i = 0
    k = 1
    while True:
        j = ni[i]
        if j <= i:
            k +=1
        i = (j + 1) % N

        if i == 0:
            break

    error_print(k, K % k)
    s = []
    ss = set()

    i = 0
    K %= k
    k = 0
    while k < (K-1):
        j = ni[i % N]
        if j <= i:
            k += 1
        i = j + 1

    i += k * N
    s = []
    ss = set()
    for l in range(i, N*K):
        m = l % N
        a = A[m]
        if a in ss:
            while True:
                b = s.pop()
                ss.remove(b)
                if b == a:
                    break
        else:
            s.append(a)
            ss.add(a)
    return ' '.join(map(str, s))


def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))

    # N = 2*(10**5)
    # # N = 10
    # K = 10**12
    # A = [random.randint(1, N) for _ in range(N)]
    # # print(A)
    # print(slv(N, K, A))


if __name__ == '__main__':
    main()
