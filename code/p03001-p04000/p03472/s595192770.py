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
from operator import add, mul

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
def slv(N, H, AB):
    ma = max(AB, key=lambda x: x[0])[0]
    AB.sort(key=lambda x: x[1], reverse=True)

    ans = 0
    i = 0
    while H > 0:
        if i < N and AB[i][1] >= ma:
            H -= AB[i][1]
            i += 1
            ans += 1
        else:
            n = int(math.ceil(H / ma))
            H -= ma * n
            ans += n

    return ans


def main():
    N, H = read_int_n()
    AB = [read_int_n() for _ in range(N)]
    print(slv(N, H, AB))


if __name__ == '__main__':
    main()
