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
def slv(N, K, S):
    S = [c for c in S]

    idx = []
    p = (None, -1)
    for i, c in enumerate(S):
        if p[0] != c:
            idx.append([p[0], i-p[1]])
            p = (c, i)
    idx.append([p[0],len(S)-p[1]])
    idx.pop(0)
    
    
    ans = [idx[0]]
    for i in range(1, len(idx)):
        if i % 2 == 0:
            if ans[-1][0] == idx[i][0]:
                ans[-1][1] += idx[i][1]
            else:
                ans.append(idx[i])
        else:
            if K > 0:
                ans[-1][1] += idx[i][1]
                K -= 1
            else:
                ans.append(idx[i])
    a = 0
    for _, v in ans:
        a += v - 1
    return a


def main():
    N, K = read_int_n()
    S = read_str()
    print(slv(N, K, S))


if __name__ == '__main__':
    main()
