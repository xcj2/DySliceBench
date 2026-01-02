# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations

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
    return input()


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
def slv(H, W, D, A, Q, LR):
    S = [0] * (H * W + 1)
    A_ = {}
    for i, r in enumerate(A):
        for j, c in enumerate(r):
            A_[c] = (i, j)
    
    for i in range(D+1, H*W+1):
        S[i] = S[i-D] + abs(A_[i][0]-A_[i-D][0]) + abs(A_[i][1]-A_[i-D][1])
    
    for l, r in LR:
        # print(H, W, r, l)
        print(S[r]-S[l])
    



def main():
    H, W, D = read_int_n()
    A = [read_int_n() for _ in range(H)]
    Q = read_int()
    LR = [read_int_n() for _ in range(Q)]
    slv(H, W, D, A, Q, LR)


if __name__ == '__main__':
    main()
