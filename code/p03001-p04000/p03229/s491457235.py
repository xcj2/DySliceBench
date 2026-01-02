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
def slv(N, A):
    b = deque()
    A.sort()
    for i in range(N//2):
        if i % 2 == 0:
            b.appendleft(A[i])
            b.append(A[N-i-1])
        else:
            b.append(A[i])
            b.appendleft(A[N-i-1])
    if N % 2 !=  0:
        a = A[N//2]
        l = b[0]
        r = b[-1]
        if abs(a-l) > abs(a-r):
            b.appendleft(a)
        else:
            b.append(a)
    
    ans = 0
    for i in range(N-1):
        ans += abs(b[i]-b[i+1])
        
    return ans


def main():
    N = read_int()
    A = [read_int() for _ in range(N)]
    print(slv(N, A))


if __name__ == '__main__':
    main()
