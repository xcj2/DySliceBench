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


def divisor(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


@mt
def slv(N, K, A):
    S = sum(A)
    D = [n for n in divisor(S)]
    D.sort()

    ans = 0
    for d in D:
        r = []
        for a in A:
            r.append(a % d)
        r.sort()
        rr = [d - n for n in r]
        sr = [0]
        srr = [0]
        for i in range(N):
            sr.append(sr[-1] + r[i])
            srr.append(srr[-1] + rr[i])
        
        for i in range(N):
            e = sr[i+1] - sr[0]
            f = srr[N]-srr[i+1]
            if e == f and e <= K:
                ans = max(ans, d)
                break
    return ans



def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))


if __name__ == '__main__':
    main()
