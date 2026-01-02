import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product


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

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        print(e - s, 'sec', file=sys.stderr)
        return ret

    return wrap


@mt
def slv(N, A):

    if A[0] != 0:
        return -1

    for i in range(N - 1):
        if A[i + 1] - A[i] > 1:
            return -1

    ans = A[-1]
    for i in range(N - 1):
        if A[i] >= A[i + 1]:
            ans += A[i]
    return ans


def main():
    N = read_int()
    A = [read_int() for _ in range(N)]

    print(slv(N, A))


if __name__ == '__main__':
    main()
