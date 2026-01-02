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
    n = 1
    for _ in range(k-1):
        j = 0
        while True:
            l = 10**j
            t = 0
            t += n + l
            t -= (n+l) % l
            m = (t % (10**(j+1))) // l
            # print(t, j, m)
            for i in range(j-1, -1, -1):
                t += (10 ** i) * max(0, m-(j-i))
            # print(t, j)
            if is_lunlun(t):
                n = t
                break
            else:
                j+=1
            # if j > 5:
            #     break
        # print(n)
    return n



def main():
    K = read_int()
    print(slv(K))



if __name__ == '__main__':
    main()
