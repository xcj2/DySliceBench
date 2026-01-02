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

    tmp = [a-(i+1) for i, a in enumerate(A)]

    
    def sk(b):
        s = 0
        for i, a in enumerate(A):
            s += abs(a-(b+i+1))
        return s

    # for i in range(-10, 10):
    #     print(i, sk(i))

    s = -int(1e+10)
    e = int(1e+10)
    ssk = sk(s)
    esk = sk(e)
    # print(s, ssk)
    # print(e, esk)
    while abs(s - e) > 1:
        m = (s+e)//2
        msk = sk(m)
        # print(m, msk)
        if ssk < esk:
            esk = msk
            e = m
        else:
            ssk = msk
            s = m
    
    return min(sk(s), sk(e))


def main():
    N = read_int()
    A = read_int_n() 
    print(slv(N, A))


if __name__ == '__main__':
    main()
