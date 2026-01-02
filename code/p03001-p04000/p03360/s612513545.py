import math
import random
import heapq
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING
from functools import lru_cache, reduce
from itertools import combinations_with_replacement, product, combinations


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


def mt(f):
    import time
    import sys

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        print(e - s, 'sec', file=sys.stderr)
        return ret

    return wrap


@mt
def slv(A, B, C, K):

    ans = sum([A, B, C])
    m = max([A, B, C])
    ans -= m
    for i in range(K):
        m *= 2
    return ans + m


def main():
    A, B, C = read_int_n()
    K = read_int()
    print(slv(A, B, C, K))


if __name__ == '__main__':
    main()