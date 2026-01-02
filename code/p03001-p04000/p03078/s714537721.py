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
def slv(A, B, C, K):
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    def s(i, j, k):
        return A[i] + B[j] + C[k]
    used = set()
    
    cand = []
    heapq.heappush(cand, (-s(0, 0, 0), (0, 0, 0)))
    for _ in range(K):
        v, i = heapq.heappop(cand)
        print(-v)
        
        ti = (i[0]+1, i[1], i[2])
        if ti[0] < len(A) and ti not in used:
            heapq.heappush(cand, (-s(*ti), ti))
            used.add(ti)
        
        ti = (i[0], i[1]+1, i[2])
        if ti[1] < len(B) and ti not in used:
            heapq.heappush(cand, (-s(*ti), ti))
            used.add(ti)
        
        ti = (i[0], i[1], i[2]+1)
        if ti[2] < len(C) and ti not in used:
            heapq.heappush(cand, (-s(*ti), ti))
            used.add(ti)



def main():
    # for _ in range(1000):
    #     K = 3000
    #     A = [random.randint(1, 10000000000) for _ in range(random.randint(1, 1000))]
    #     B = [random.randint(1, 10000000000) for _ in range(random.randint(1, 1000))]
    #     C = [random.randint(1, 10000000000) for _ in range(random.randint(1, 1000))]
    #     K = min(K, len(A) + len(B) + len(C))
    #     slv(A,B,C,K)
    # N = read_int()
    X, Y, Z, K = read_int_n()
    A = read_int_n()
    B = read_int_n()
    C = read_int_n()
    (slv(A, B, C, K))


if __name__ == '__main__':
    main()
