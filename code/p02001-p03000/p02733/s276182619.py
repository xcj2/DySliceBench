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
def slv(H, W, K, S):
    ans = 0
    S = [list(map(int, [c for c in r])) for r in S]
    # for r in S:
    #     print(r)
    # wn = sum([sum(r) for r in S])
    # # print(wn)


    ans = INF
    for p in product([0, 1], repeat=H-1):
        spl = [i+1 for i, v in enumerate(p) if v == 1]
        cand = len(spl)
        spl.append(H)
        rs = []
        p = 0
        for si in spl:
            r = [0] * W
            for j in range(W):
                for k in range(p, si):
                    r[j] += S[k][j]
            rs.append(r)
            p = si
        # print(spl,'------')
        # for r in rs:
        #     print(r)

        sr = [0] * len(rs)
        impossible = False
        for i in range(W):
            if any([sr[j] + rs[j][i] > K for j in range(len(rs))]):
                cand += 1
                for j in range(len(rs)):
                    sr[j] = rs[j][i]
                    if sr[j] > K:
                        impossible = True
            else:
                for j in range(len(rs)):
                    sr[j] += rs[j][i]
        if not impossible:
            ans = min(ans, cand)



    return ans


def main():
    H, W, K = read_int_n()
    S = [read_str() for _ in range(H)]
    print(slv(H, W, K, S))


if __name__ == '__main__':
    main()
