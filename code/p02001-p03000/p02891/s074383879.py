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
def slv(S, K):
    ans = 0
    S = [c for c in S]
    if K < 4:
        S = S * K
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                ans += 1
                S[i+1] = '-'
        return ans
    
    N = len(S)
    S = S * (4 if K % 2 == 0 else 5)
    a = [0] * (4 if K % 2 == 0 else 5)
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            a[(i+1)//N] += 1
            S[i+1] = '-'

    o = math.ceil((K-2) / 2)
    e = (K-2) // 2
    return a[0] + a[-1] + a[1] * o + a[2] * e


def main():
    S = read_str()
    K = read_int()
    print(slv(S, K))


if __name__ == '__main__':
    main()
