# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub


import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()

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
def slv(N, M, A):
    b_lcm = 1


    d2 = set()
    for a in A:
        b = a // 2
        b_lcm = b_lcm//math.gcd(b_lcm, b) * b
        for i in range(100000000):
            if a % 2 == 0:
                a //= 2
            else:
                d2.add(i)
                break

    return -(-(M // b_lcm)//2) if len(d2) == 1 else 0





def main():
    N, M = read_int_n()
    A = read_int_n()
    print(slv(N, M, A))


if __name__ == '__main__':
    main()
