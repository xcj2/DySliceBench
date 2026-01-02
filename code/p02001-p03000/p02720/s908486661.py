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

sys.setrecursionlimit(1000000)
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

def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

def slv(k):
    if k <= 9:
        return k
    lunlun = list(range(1, 10))
    q = deque(lunlun)

    while True:
        n = q.popleft()
        for i in (-1, 0, 1):
            d = n % 10
            if 0 <= d + i <= 9:
                l = n * 10 + d+i
                q.append(l)
                lunlun.append(l)
                if len(lunlun) == k:
                    return lunlun[-1]




def main():
    K = read_int()
    print(slv(K))



if __name__ == '__main__':
    main()
