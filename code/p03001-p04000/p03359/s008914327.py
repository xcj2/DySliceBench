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
def slv(a, b):

    c = a - 1

    if b >= a:
        c += 1
    return c


def main():
    a, b = read_int_n()
    print(slv(a, b))


if __name__ == '__main__':
    main()