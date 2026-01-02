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

sys.setrecursionlimit(10000)


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
def slv(N, A):
    # ans = 0
    ans = sys.maxsize

    S = [0] * (N+1)
    for i in range(0, N):
        S[i+1] = A[i] + S[i]
    
    lj = 1
    left_diffs = {}
    for i in range(2, N-1):
        left_diff = (sys.maxsize, 0, 0)
        for j in range(lj, i):
            a = S[j]-S[0]
            b = S[i]-S[j]
            # print(j, A[0:j], A[j:i], a, b, abs(a-b))
            if left_diff[0] > abs(a-b):
                left_diff = (abs(a-b), a, b)
            else:
                break
        lj = j-1 if j-1 > 0 else 1
        left_diffs[i] = left_diff

    right_diffs = {}
    rj = N-1
    for i in range(N-1-1, 2-1, -1):
        right_diff = (sys.maxsize, 0, 0)
        # for j in range(i+1, N):
        for j in range(rj, i, -1):
            c = S[j]-S[i]
            d = S[-1]-S[j]
            # print(j, A[i:j], A[j:], c, d, abs(c-d))
            if right_diff[0] > abs(c-d):
                right_diff = (abs(c-d), c, d)    
            else:
                break
        rj = j+1 if j+1 < N else N-1
        right_diffs[i] = right_diff
    
    for i in range(2, N-1): 
        _, a, b = left_diffs[i]
        _, c, d = right_diffs[i]
        # print(a, b, c, d)
        ans = min(ans, (max(a, b, c, d) - min(a, b, c, d)))
    return ans
     

def main():
    N = read_int()
    A = read_int_n() 

    # N = int(2.0e+5)
    # A = [random.randint(1, int(1e+9)) for _ in range(N)]
    print(slv(N, A))


if __name__ == '__main__':
    main()
