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
def slv(H, W, M):
    def ok(i, j):
        f = False
        if i > 0 and M[i - 1][j] == '#':
            f = True
        if i < H - 1 and M[i + 1][j] == '#':
            f = True

        if j > 0 and M[i][j - 1] == '#':
            f = True

        if j < W - 1 and M[i][j + 1] == '#':
            f = True
        return f

    for i in range(H):
        for j in range(W):
            if M[i][j] == '#' and not ok(i, j):
                return 'No'

    return 'Yes'


def main():
    H, W = read_int_n()
    M = [read_str() for _ in range(H)]
    print(slv(H, W, M))


if __name__ == '__main__':
    main()