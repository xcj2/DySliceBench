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
def slv(N, M, X):
    D = defaultdict(list)
    for x in X:
        D[x%M].append(x)
    ans = 0
    for i in range(1, M//2+1):
        j = M - i
        if i == j:
            continue
        if len(D[i]) == len(D[j]):
            ans += len(D[i])
        else:
            l = D[i]
            s = D[j]
            if len(l) < len(s):
                l, s = s, l
            C = list(Counter(l).values())
            h = []
            for c in C:
                if c % 2 == 1:
                    h.append(1)
                    c -= 1
                if c != 0:
                    h.append(c)
            heapq.heapify(h)
            s = len(s)
            while h and s > 0:
                c = heapq.heappop(h)
                if c == 1:
                    ans +=1
                    s -= 1
                else:
                    if s >= c:
                        ans += c
                        s -= c
                    else:
                        ans += s
                        heapq.heappush(h, c-s)
                        s = 0
            while h:
                c = heapq.heappop(h)
                ans += c // 2
    ans += len(D[0]) // 2
    if M % 2 == 0:
        ans += len(D[M//2]) // 2
    return ans


def main():
    N, M = read_int_n()
    X = read_int_n()
    print(slv(N, M, X))


if __name__ == '__main__':
    main()
