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


@mt
def slv(N, K, S):
    s1 = list(map(lambda x: len(x), filter(lambda x: x != '', S.split('0'))))
    s0 = list(map(lambda x: len(x), filter(lambda x: x != '', S.split('1'))))


    if len(s0) <= K:
        return N
    # error_print(N, K)
    # error_print(S)
    # error_print(s1)
    # error_print(s0)

    ans = 0
    s0_top = None
    if S[0] == '0':
        s0_top = s0.pop(0)
        ans = s0_top + sum(s1[:K]) + sum(s0[:K-1])
    
    l1o = 1
    l0o = 0
    l1 = sum(s1[:K+l1o])
    l0 = sum(s0[:K+l0o])
    k = 0
    
    while True:
        tmp = l1 + l0
        # if k == 0 and S[0] == '0':
        #     tmp -= s1[K]
        ans = max(ans, tmp)
        if k+K < len(s1) and k+K < len(s0):
            l1 -= s1[k]
            if k+K+l1o < len(s1):
                l1 += s1[k+K+l1o]
            l0 -= s0[k]
            if k+K+l0o < len(s0):
                l0 += s0[k+K+l0o]
        else:
            break
        k += 1
    

    return ans


def main():
    N, K = read_int_n()
    S = read_str()
    rS = ''.join(['0' if c == '1' else '1' for c in S])
    print(max(slv(N, K, S), slv(N, K-1, rS)))

    # N = 20
    # K = random.randint(1, 10)
    # S = ''.join(random.choices('01', k=N))
    # rS = ''.join(['0' if c == '1' else '1' for c in S])
    # print(max(slv(N, K, S), slv(N, K-1, rS)))

if __name__ == '__main__':
    main()
