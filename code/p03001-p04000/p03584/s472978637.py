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
def slv(N, K, AB):
    ans = 0
    for i in range(K.bit_length()-1, -2, -1):
        mask = K
        if i > -1:
            if mask & 1 << i:
                mask -= 1 << i
            else:
                continue
        for j in range(i):
            mask |= 1 << j
        cand = 0
        v = 0
        for a, b in AB:
            if (a | mask) == mask:
                cand += b
                v |= a
        assert v <= K
        ans = max(ans, cand)
    return ans



def main():
    N, K = read_int_n()
    AB = [read_int_n() for _ in range(N)]
    print(slv(N, K, AB))


if __name__ == '__main__':
    main()
