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
def slv(D, G, PC):

    ans = sys.maxsize
    PC = list(reversed(PC))
    for i in product([0, 1], repeat=D):
        g = G
        p = 0
        for j, v in enumerate(i):
            if v == 0:
                continue
            p += PC[j][0]
            g -= PC[j][1] + PC[j][0] * (D-j) * 100
        if g > 0 and 0 in i:
            j = i.index(0)
            for _ in range(PC[j][0]-1):
                p += 1
                g -= (D-j)*100
                if g <= 0:
                    break
        if g <= 0:
            ans = min(ans, p)

    return ans


def main():
    D, G = read_int_n()
    PC = [read_int_n() for _ in range(D)]
    print(slv(D, G, PC))


if __name__ == '__main__':
    main()
